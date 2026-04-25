@echo off
title F1 Mapping Converter
echo Checking Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please install Python from https://python.org
    pause
    exit /b
)
echo Installing required package...
pip install customtkinter --quiet
echo Launching F1 Mapping Converter...
python "%~dp0F1-Mapping-Converter.py"
