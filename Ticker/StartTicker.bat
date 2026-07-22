@echo off
cd /d %~dp0
start "" py ticker.py
start "" py -m http.server 8080
echo Open ticker.html in OBS as a Browser Source using Local File.
pause
