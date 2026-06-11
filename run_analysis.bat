@echo off
title Resonator Survey Analysis
echo ========================================================
echo          Running Resonator Survey Analysis
echo ========================================================
echo.

:: Check if uv is installed
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: uv is not installed. Please install it first.
    echo Read README.md for installation instructions.
    pause
    exit /b %errorlevel%
)

:: Sync environment using copy mode to bypass cloud drive (OneDrive) hardlink errors
echo Syncing uv environment (copy mode)...
uv sync --link-mode=copy
if %errorlevel% neq 0 (
    echo Error: Failed to sync environment.
    pause
    exit /b %errorlevel%
)

:: Run analysis
echo.
echo Running analysis...
uv run --link-mode=copy src/quickanalysis1.py

echo.
echo Analysis complete. Plots are saved in the plots/ directory.
pause
