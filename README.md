.
# Guide
## Setup theo docker
```bash
bash dk_build.sh
bash dk_run.sh
```
## Setup theo cài môi trường local
```bash
pip install -r requirements.txt
```

## Khởi chạy ứng dụng với Uvicorn
```bash
PYTHONPATH=. uvicorn app.main:app --reload
```

```bash
# Khởi chạy với .env truyền theo tham số
ENV_FILE=./.env PYTHONPATH=. uvicorn app.main:app --reload
```

## Các lệnh thao tác
```bash
# Kiểm tra tiến trình chiếm port
lsof -i :8000
```

```bash
# Script kill_port_8000.sh (đảm bảo đã có quyền thực thi)
chmod +x ./script/kill_port_8000.sh
./script/kill_port_8000.sh
```

```bash
# Tạo sơ đồ thư mục
sudo snap install tree
tree -I "__pycache__|*.pyc|*.db" > README_STRUCTURE.md
```

```bash
# Định dạng mã nguồn tự động
chmod +x scripts/format.sh
./scripts/format.sh
```

# Cấu trúc thư mục

```
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── app
│   ├── api
│   │   ├── deps.py
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── admin.py
│   │       ├── auth.py
│   │       ├── __init__.py
│   │       ├── todos.py
│   │       └── users.py
│   ├── core
│   │   ├── config.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── todo.py
│   │   └── user.py
│   ├── schemas
│   │   ├── auth.py
│   │   ├── __init__.py
│   │   ├── todo.py
│   │   └── user.py
│   ├── services
│   │   ├── admin_service.py
│   │   ├── auth_service.py
│   │   ├── __init__.py
│   │   ├── todo_service.py
│   │   └── user_service.py
│   └── utils
├── data
├── dk_build.sh
├── dk_run.sh
├── docker-compose.yml
├── Dockerfile
├── __init__.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── scripts
│   ├── format.sh
│   ├── generate_tests.py
│   └── kill_port_8000.sh
├── test
│   ├── api
│   │   ├── test_deps.py
│   │   └── v1
│   │       ├── test_admin.py
│   │       ├── test_auth.py
│   │       ├── test_todos.py
│   │       └── test_users.py
│   ├── core
│   │   ├── test_config.py
│   │   └── test_database.py
│   ├── models
│   │   ├── test_todo.py
│   │   └── test_user.py
│   ├── schemas
│   │   ├── test_auth.py
│   │   ├── test_todo.py
│   │   └── test_user.py
│   └── services
│       ├── test_admin_service.py
│       ├── test_auth_service.py
│       ├── test_todo_service.py
│       └── test_user_service.py
├── t_e_s_t_example
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_basic_ops.py
│   └── test_class.py
```

# Tài liệu và tiện ích
- Notion nội bộ: https://www.notion.so/FastAPI-22472b24fd9b80aa9ba2d6f48a3b718f
- Extension VSCode: Material Icon Theme để dễ phân biệt thư mục / tệp.