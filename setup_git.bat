@echo off
title Git Repository Initialization and Commit
echo ========================================================
echo         Resonator Survey Repository Setup
echo ========================================================
echo.

:: Clean up old files from the root directory if they exist
echo [1/4] Cleaning up old root files...
del /q ben_find_peaks.py 2>nul
del /q fitresonance.py 2>nul
del /q frsurvey.py 2>nul
del /q guessResonanceFrequenciesBen.py 2>nul
del /q quickanalysis1.py 2>nul
del /q widesurvey.py 2>nul
del /q main.py 2>nul
del /q widesurvey_aSi80s_20240913.npz 2>nul
echo Done.

:: Stage all files
echo [2/4] Staging all files...
git add .
if %errorlevel% neq 0 (
    echo Error: Failed to stage files. Is Git installed?
    pause
    exit /b %errorlevel%
)

:: Commit files
echo [3/4] Committing files...
git commit -m "Initial commit of resonator-survey project with src/ and data/ structure"
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

echo [4/4] Setting branch to main...
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
