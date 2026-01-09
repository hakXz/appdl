@echo off
setlocal EnableDelayedExpansion

echo ===============================
echo FFmpeg automatic installer ~ hak
echo ===============================
echo.

:: Yönetici kontrolü
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script must be run as Administrator.
    echo Right click and select "Run as administrator".
    pause
    exit /b
)

set FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
set INSTALL_DIR=C:\ffmpeg
set ZIP_FILE=%TEMP%\ffmpeg.zip

echo Downloading FFmpeg...
powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%ZIP_FILE%'" || (
    echo Download failed.
    pause
    exit /b
)

echo Extracting FFmpeg...
powershell -Command "Expand-Archive -Force '%ZIP_FILE%' '%TEMP%\ffmpeg_extracted'" || (
    echo Extraction failed.
    pause
    exit /b
)

echo Installing to %INSTALL_DIR% ...
if exist "%INSTALL_DIR%" rmdir /s /q "%INSTALL_DIR%"
mkdir "%INSTALL_DIR%"

for /d %%D in ("%TEMP%\ffmpeg_extracted\ffmpeg-*") do (
    xcopy "%%D\*" "%INSTALL_DIR%\" /E /I /H /Y
)

echo Cleaning up...
del "%ZIP_FILE%"
rmdir /s /q "%TEMP%\ffmpeg_extracted"

echo Adding FFmpeg to system PATH...

setx PATH "%PATH%;%INSTALL_DIR%\bin" /M >nul

echo.
echo ===============================
echo FFmpeg installation complete
echo ===============================
echo.
echo Please RESTART your computer.
echo After restart, test with:
echo ffmpeg -version
echo.

pause
endlocal
