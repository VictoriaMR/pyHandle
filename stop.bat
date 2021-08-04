@echo off

echo chrome stoping...
taskkill /F /IM chrome.exe > nul
echo chrome stop

echo.

echo python stoping...
taskkill /F /IM python.exe > nul
echo python stop

timeout 2 > NUL