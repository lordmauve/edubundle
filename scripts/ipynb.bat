@echo off

set PATH=%~dp0;%~dp0\Scripts;%PATH%
cd %~dp0\..\notebooks
%~dp0\Scripts\jupyter.exe notebook
