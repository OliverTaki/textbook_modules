@echo off
cd /d "C:\Users\punch\Desktop\KnowledgeMapProject"
set GIT="C:\Program Files\Git\cmd\git.exe"

echo === Removing leftover untracked dirs ===
if exist "modules\" rmdir /s /q "modules"
if exist "logs\" rmdir /s /q "logs"

echo.
echo === stage all changes (including deletions) ===
%GIT% add -A

echo.
echo === status after staging ===
%GIT% status --short

echo.
echo === commit ===
%GIT% commit -m "restructure: separate public db from internal production"

echo.
echo === push ===
%GIT% push origin main

echo.
echo === final log ===
%GIT% log --oneline -5

echo.
echo DONE
