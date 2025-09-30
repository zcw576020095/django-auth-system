# Django 用户认证系统

一个基于 Django 的现代化用户认证系统，提供用户注册、登录、个人资料管理等功能，采用 HTMX 技术实现无刷新页面交互。

## 🚀 功能特性

- ✅ 用户注册与登录
- ✅ 用户个人资料管理
- ✅ 响应式设计，支持移动端
- ✅ HTMX 无刷新页面交互
- ✅ Bootstrap 5 现代化 UI
- ✅ 表单验证与错误处理
- ✅ 安全的密码管理
- ✅ 日志记录系统

## 🛠️ 技术栈

- **后端**: Django 5.2.6
- **前端**: HTML5, CSS3, JavaScript
- **UI框架**: Bootstrap 5
- **交互技术**: HTMX
- **数据库**: SQLite (开发环境)
- **图标**: Font Awesome

## 📋 系统要求

- Python 3.11.9 (推荐 3.11+)
- Django 5.2+
- 现代浏览器 (Chrome, Firefox, Safari, Edge)

## 🔧 安装与配置

### 1. 克隆项目

```bash
git clone https://github.com/zcw576020095/django-auth-system.git
cd django-auth-system
```

### 2. 创建虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置数据库

#### 使用 SQLite (开发环境，默认)
```bash
# 创建数据库迁移文件
python manage.py makemigrations

# 执行数据库迁移
python manage.py migrate
```

#### 使用 PostgreSQL (生产环境推荐)
```bash
# 安装 PostgreSQL 驱动
pip install psycopg2-binary

# 在 settings.py 中配置数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_database_name',
#         'USER': 'your_database_user',
#         'PASSWORD': 'your_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# 执行迁移
python manage.py makemigrations
python manage.py migrate
```

#### 使用 MySQL
```bash
# 安装 MySQL 驱动
pip install mysqlclient

# 在 settings.py 中配置数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'your_database_name',
#         'USER': 'your_database_user',
#         'PASSWORD': 'your_password',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

### 5. 创建超级用户 (可选)

```bash
python manage.py createsuperuser
```

### 6. 运行开发服务器

```bash
python manage.py runserver
```

访问 `http://127.0.0.1:8000` 查看应用。

## 🧪 快速测试

### 测试用户注册流程
1. 访问 `http://127.0.0.1:8000`
2. 点击导航栏的"注册"按钮
3. 填写用户信息并提交
4. 验证注册成功后的页面跳转

### 测试用户登录流程
1. 点击导航栏的"登录"按钮
2. 使用注册的账号信息登录
3. 验证登录成功后的用户状态

### 测试 HTMX 功能
- 所有页面切换都应该是无刷新的
- 表单提交时会显示加载动画
- 错误信息会实时显示

## 🔧 开发环境配置

### 启用调试模式
确保 `settings.py` 中的配置：
```python
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

### 查看日志
```bash
# 实时查看日志
tail -f logs/django.log

# Windows 用户可以直接打开文件查看
# logs/django.log
```

### 数据库管理
```bash
# 查看数据库结构
python manage.py dbshell

# 创建数据库备份
python manage.py dumpdata > backup.json

# 恢复数据库
python manage.py loaddata backup.json
```

## 📁 项目结构

```
django-auth-system/
├── auth_project/          # 项目配置
│   ├── __init__.py
│   ├── settings.py        # Django 设置
│   ├── urls.py           # 主路由配置
│   └── wsgi.py           # WSGI 配置
├── users/                # 用户应用
│   ├── __init__.py
│   ├── admin.py          # 管理后台配置
│   ├── apps.py           # 应用配置
│   ├── forms.py          # 表单定义
│   ├── models.py         # 数据模型
│   ├── urls.py           # 用户路由
│   └── views.py          # 视图函数
├── templates/            # 模板文件
│   ├── base.html         # 基础模板
│   └── users/            # 用户相关模板
├── static/               # 静态文件
│   └── css/              # 样式文件
├── logs/                 # 日志文件
├── manage.py             # Django 管理脚本
├── requirements.txt      # 项目依赖
└── README.md            # 项目说明
```

## 🎨 界面展示

### 用户登录页面
![用户登录页面](screenshots/login.png)

用户登录界面采用现代化设计，具有以下特点：
- 简洁清晰的登录表单
- 响应式设计，适配各种设备
- 友好的用户体验
- 安全的认证机制

### 用户注册页面
![用户注册页面](screenshots/register.png)

用户注册界面功能：
- 完整的用户信息收集表单
- 实时表单验证
- 密码强度检查
- 友好的错误提示

### 登录成功主页
![登录成功主页](screenshots/index.png)

用户登录成功后的主页展示：
- 现代化的导航栏设计
- 个性化的用户欢迎界面
- 清晰的功能导航
- 响应式布局，适配各种设备

### 密码修改页面
![密码修改页面](screenshots/change_password.png)

密码修改页面提供：
- 安全的密码更新功能
- 密码强度验证
- 用户友好的操作界面
- 完善的安全提示

## 🔐 安全特性

- CSRF 保护
- 密码哈希存储
- 会话管理
- XSS 防护
- SQL 注入防护

## 📝 API 文档

### 用户相关接口

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | 主页 |
| `/users/register/` | GET/POST | 用户注册 |
| `/users/login/` | GET/POST | 用户登录 |
| `/users/logout/` | POST | 用户登出 |
| `/users/home/` | GET | 用户主页 (需要登录) |
| `/users/change-password/` | GET/POST | 修改密码 (需要登录) |

## 🧪 测试

### 运行单元测试
```bash
# 运行所有测试
python manage.py test

# 运行特定应用的测试
python manage.py test users

# 运行特定测试类
python manage.py test users.tests.UserModelTest

# 显示详细输出
python manage.py test --verbosity=2
```

### 测试覆盖率
```bash
# 安装覆盖率工具
pip install coverage

# 运行测试并生成覆盖率报告
coverage run --source='.' manage.py test
coverage report
coverage html  # 生成HTML报告
```

### 手动测试清单
- [ ] 用户注册功能
- [ ] 用户登录/登出功能
- [ ] 表单验证
- [ ] HTMX 无刷新交互
- [ ] 响应式设计
- [ ] 错误处理
- [ ] 日志记录

## 📊 日志

应用日志存储在 `logs/django.log` 文件中，包含：
- 用户操作记录
- 错误信息
- 系统运行状态

## 🚀 部署

### 本地开发部署
```bash
# 1. 克隆项目后进入目录
cd django-auth-system

# 2. 创建并激活虚拟环境
python -m venv django-auth-system
# Windows
django-auth-system-venv\Scripts\activate
# macOS/Linux
source django-auth-system-venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量（可选）
# 创建 .env 文件
echo "DEBUG=True" > .env
echo "SECRET_KEY=your-secret-key-here" >> .env

# 5. 数据库初始化
python manage.py makemigrations
python manage.py migrate

# 6. 创建超级用户（可选）
python manage.py createsuperuser

# 7. 启动服务
python manage.py runserver
```

### 生产环境部署

#### 环境变量配置
```bash
export DEBUG=False
export SECRET_KEY='your-production-secret-key'
export ALLOWED_HOSTS='your-domain.com,www.your-domain.com'
export DATABASE_URL='postgresql://user:password@localhost:5432/dbname'
```

#### 使用 Gunicorn + Nginx
```bash
# 安装 Gunicorn
pip install gunicorn

# 收集静态文件
python manage.py collectstatic --noinput

# 启动 Gunicorn
gunicorn auth_project.wsgi:application --bind 0.0.0.0:8000
```

#### Nginx 配置示例
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Docker 部署 (可选)

```dockerfile
# Dockerfile 示例
FROM python:3.11.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## ❗ 常见问题

### Q: 启动服务器时出现端口被占用错误
```bash
# 查看占用8000端口的进程
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # macOS/Linux

# 使用其他端口启动
python manage.py runserver 8001
```

### Q: 数据库迁移失败
```bash
# 重置迁移文件
python manage.py migrate --fake-initial

# 或者删除迁移文件重新生成
# 删除 users/migrations/ 下除 __init__.py 外的所有文件
python manage.py makemigrations users
python manage.py migrate
```

### Q: 静态文件无法加载
```bash
# 确保 settings.py 中配置正确
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']

# 开发环境下确保 DEBUG=True
# 生产环境需要收集静态文件
python manage.py collectstatic
```

### Q: HTMX 功能不工作
- 检查浏览器控制台是否有JavaScript错误
- 确保 HTMX 库正确加载
- 验证 CSRF token 配置

### Q: 虚拟环境问题
```bash
# 重新创建虚拟环境
deactivate  # 如果已激活
rm -rf venv  # 删除旧环境
python -m venv venv  # 创建新环境
# 重新激活并安装依赖
```

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

### MIT 许可证说明

MIT 许可证是一个宽松的开源许可证，允许：

✅ **商业使用** - 可以用于商业项目  
✅ **修改** - 可以修改源代码  
✅ **分发** - 可以分发原始或修改后的代码  
✅ **私人使用** - 可以私人使用  
✅ **许可证和版权声明** - 在分发时需要包含原始许可证和版权声明  

❌ **责任** - 作者不承担任何责任  
❌ **保证** - 不提供任何保证

## 👨‍💻 作者

- **zcw576020095** - *Initial work* - [zcw576020095](https://github.com/zcw576020095)

## 🙏 致谢

- Django 社区
- Bootstrap 团队
- HTMX 开发者
- Font Awesome

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 邮箱: 13613527283@163.com
- GitHub Issues: [项目问题页面](https://github.com/zcw576020095/django-auth-system/issues)

## 🔄 更新日志

### v1.0.0 (2025-01-27)
- 初始版本发布
- 基础用户认证功能
- HTMX 集成
- 响应式设计

---

⭐ 如果这个项目对你有帮助，请给它一个星标！