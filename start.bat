@echo off
echo.

python main.py
echo Please check output.xlsx
SET /P _inputname= if you want to open the output file press y:
IF "%_inputname%"=="y" start output.xlsx

goto end

echo.
echo file no found
:end