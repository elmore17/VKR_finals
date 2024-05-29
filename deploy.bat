@echo off

:: Переменные
set FRONTEND_DIR=C:\Users\Acer\Desktop\VKR_finals\frontend
set BACKEND_DIR=C:\Users\Acer\Desktop\VKR_finals\backend

:: Настройка и запуск бэкенда
cd /d %BACKEND_DIR%
call venv\Scripts\activate
set FLASK_APP=app.py
start cmd /k "cd /d %BACKEND_DIR% && venv\Scripts\activate && flask run"

:: Настройка и запуск фронтенда
start cmd /k "cd /d %FRONTEND_DIR% && npm install && npm run serve"
