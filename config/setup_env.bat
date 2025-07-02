@echo off
echo [*] Creating virtual environment...
python -m venv env
call env\Scripts\activate.bat
echo [*] Installing dependencies...
pip install -r requirements.txt
echo [✓] Done. Use 'env\Scripts\activate' to activate environment next time.
pause
