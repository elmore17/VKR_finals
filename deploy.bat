@echo off

:: Переменные
set FRONTEND_DIR=path_to_vue_app
set BACKEND_DIR=path_to_flask_app
set DB_NAME=your_database_name
set DB_USER=your_database_user
set DB_PASS=your_database_password

:: Функция для запуска PostgreSQL
echo Starting PostgreSQL...
pg_ctl start -D "C:\Program Files\PostgreSQL\<version>\data"

:: Настройка базы данных
echo Setting up PostgreSQL database...
psql -U postgres -c "CREATE DATABASE %DB_NAME%;"
psql -U postgres -c "CREATE USER %DB_USER% WITH PASSWORD '%DB_PASS%';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE %DB_NAME% TO %DB_USER%;"

:: Настройка и запуск бэкенда
cd /d %BACKEND_DIR%
call venv\Scripts\activate
set FLASK_APP=app.py
start cmd /k "flask run"

:: Настройка и запуск фронтенда
cd /d %FRONTEND_DIR%
npm install
start cmd /k "npm run serve"

echo Application is running. Frontend is available at http://localhost:8080
pause