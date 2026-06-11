@echo off
title Git Repository Initialization and Commit
echo ========================================================
echo         Resonator Survey Repository Setup
echo ========================================================
echo.

:: Stage all files
echo [1/3] Staging all files...
git add .
if %errorlevel% neq 0 (
    echo Error: Failed to stage files. Is Git installed?
    pause
    exit /b %errorlevel%
)

:: Commit files
echo [2/3] Committing files...
git commit -m "Initial commit of resonator-survey project"
if %errorlevel% neq 0 (
    echo.
    echo Note: If Git asks for your user.name/user.email, please configure them:
    echo   git config --global user.name "Your Name"
    echo   git config --global user.email "your.email@example.com"
    echo and run this script again.
    echo.
    pause
    exit /b %errorlevel%
)

echo [3/3] Setting branch to main...
git branch -M main

echo.
echo ========================================================
echo Success: Git repository initialized and committed locally!
echo ========================================================
echo.

set /p PUSH="Would you like to push to GitHub now? (y/n): "
if /i "%PUSH%"=="y" (
    set /p REPO_URL="Enter your GitHub Repository URL (e.g., https://github.com/username/repo-name.git): "
    if not "%REPO_URL%"=="" (
        echo Adding remote origin...
        git remote add origin %REPO_URL% 2>nul
        if %errorlevel% neq 0 (
            echo Remote origin already exists. Updating URL...
            git remote set-url origin %REPO_URL%
        )
        echo Pushing to GitHub...
        git push -u origin main
    ) else (
        echo Repo URL was empty. Skipping push.
    )
)

echo.
echo Setup script complete.
pause
