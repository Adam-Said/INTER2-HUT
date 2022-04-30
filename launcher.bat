@echo off
:start
powershell -Command "& {python main.py;}"
SET /p end="Appuyez sur entrer pour relancer"
GOTO start