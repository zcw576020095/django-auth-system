from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .forms import UserRegisterForm, UserLoginForm, UserChangePasswordForm
import logging
import json

# 获取users应用的日志记录器
logger = logging.getLogger('users')


def register(request):
    """用户注册视图"""
    # 检查是否为HTMX请求
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if request.method == 'GET':
        if is_htmx:
            # HTMX GET请求：返回注册内容片段
            return render(request, 'users/register_content.html')
        else:
            # 普通GET请求：返回完整注册页面
            form = UserRegisterForm()
            return render(request, 'users/register.html', {'form': form})
    
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            logger.info(f'新用户注册成功: {username}')
            
            if is_htmx:
                # HTMX请求：返回登录页面内容
                return render(request, 'users/login_content.html')
            else:
                messages.success(request, f'账户创建成功！欢迎您，{username}！')
                return redirect('login')
        else:
            # 表单验证失败
            if is_htmx:
                # HTMX请求：返回错误消息HTML
                error_html = '<div class="alert alert-danger animate__animated animate__headShake"><strong><i class="fas fa-exclamation-circle me-2"></i>注册失败：</strong><ul class="mb-0 mt-2">'
                
                for field, errors in form.errors.items():
                    field_name = {
                        'username': '用户名',
                        'email': '邮箱',
                        'password1': '密码',
                        'password2': '确认密码'
                    }.get(field, field)
                    
                    for error in errors:
                        error_html += f'<li>{field_name}: {error}</li>'
                
                error_html += '</ul></div>'
                
                response = HttpResponse(error_html)
                response['HX-Retarget'] = '#register-messages'
                response['HX-Reswap'] = 'innerHTML'
                return response
            else:
                # 普通请求：重新显示表单
                return render(request, 'users/register.html', {'form': form})


def user_login(request):
    """用户登录视图"""
    # 检查是否为HTMX请求
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if request.method == 'GET':
        if is_htmx:
            # HTMX GET请求：返回登录内容片段
            return render(request, 'users/login_content.html')
        else:
            # 普通GET请求：返回完整登录页面
            form = UserLoginForm()
            return render(request, 'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f'用户登录成功: {username}')
                
                if is_htmx:
                    # HTMX请求：返回主页内容模板
                    return render(request, 'users/home_content.html', {'user': user})
                else:
                    messages.success(request, f'欢迎回来，{username}！')
                    return redirect('home')
            else:
                logger.warning(f'用户登录失败: {username} - 认证失败')
                error_msg = '用户名或密码错误！'
                
                if is_htmx:
                    # HTMX请求：返回错误消息HTML，使用特殊的swap方式
                    response = HttpResponse(f'''
                        <div class="alert alert-danger animate__animated animate__headShake">
                            <strong><i class="fas fa-exclamation-circle me-2"></i>错误：</strong> {error_msg}
                        </div>
                    ''')
                    response['HX-Retarget'] = '#login-messages'
                    response['HX-Reswap'] = 'innerHTML'
                    return response
                else:
                    messages.error(request, error_msg)
                    form = UserLoginForm()
                    return render(request, 'users/login.html', {'form': form})
        else:
            error_msg = '请填写用户名和密码！'
            if is_htmx:
                response = HttpResponse(f'''
                    <div class="alert alert-warning animate__animated animate__headShake">
                        <strong><i class="fas fa-exclamation-triangle me-2"></i>提示：</strong> {error_msg}
                    </div>
                ''')
                response['HX-Retarget'] = '#login-messages'
                response['HX-Reswap'] = 'innerHTML'
                return response
            else:
                messages.warning(request, error_msg)
                form = UserLoginForm()
                return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    """用户退出登录视图"""
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        logger.info(f'用户退出登录: {username}')
        messages.success(request, '您已成功退出登录！')
    return redirect('login')


@login_required
def home(request):
    """主页视图，需要登录才能访问"""
    # 检查是否为HTMX请求
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if is_htmx:
        # HTMX请求：返回内容片段
        return render(request, 'users/home_content.html')
    else:
        # 普通请求：返回完整页面
        return render(request, 'users/home.html')


@login_required
def change_password(request):
    """修改密码视图"""
    # 检查是否为HTMX请求
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if request.method == 'GET':
        if is_htmx:
            # HTMX GET请求：返回修改密码内容片段
            return render(request, 'users/change_password_content.html')
        else:
            # 普通GET请求：返回完整修改密码页面
            form = UserChangePasswordForm(request.user)
            return render(request, 'users/change_password.html', {'form': form})
    
    elif request.method == 'POST':
        form = UserChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 更新会话，防止用户被登出
            update_session_auth_hash(request, user)
            logger.info(f'用户修改密码成功: {user.username}')
            
            if is_htmx:
                # HTMX 请求，返回主页内容并触发成功消息
                response = render(request, 'users/home_content.html', {
                    'user': request.user,
                    'success_message': '密码修改成功！'
                })
                # 使用正确的HTMX触发器语法
                response['HX-Trigger'] = json.dumps({
                    'showMessage': {
                        'message': '密码修改成功！',
                        'type': 'success'
                    }
                })
                return response
            else:
                messages.success(request, '密码修改成功！')
                return redirect('home')
        else:
            # 表单验证失败
            if is_htmx:
                # HTMX请求：返回错误消息HTML
                error_html = '<div class="alert alert-danger animate__animated animate__headShake"><strong><i class="fas fa-exclamation-circle me-2"></i>密码修改失败：</strong><ul class="mb-0 mt-2">'
                
                for field, errors in form.errors.items():
                    field_name = {
                        'old_password': '当前密码',
                        'new_password1': '新密码',
                        'new_password2': '确认新密码',
                    }.get(field, field)
                    
                    for error in errors:
                        error_html += f'<li>{field_name}: {error}</li>'
                
                error_html += '</ul></div>'
                
                response = HttpResponse(error_html)
                response['HX-Retarget'] = '#change-password-messages'
                response['HX-Reswap'] = 'innerHTML'
                return response
            else:
                # 普通请求：使用Django消息框架
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
                form = UserChangePasswordForm(request.user)
                return render(request, 'users/change_password.html', {'form': form})