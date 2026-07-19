@echo off
REM ============================================================
REM ChipPeek 极致瘦身打包脚本
REM 排除未使用的标准库模块和二进制扩展
REM ============================================================

echo 正在打包 ChipPeek...

REM 关闭正在运行的 ChipPeek
taskkill /F /IM ChipPeek.exe >nul 2>&1

REM 删除旧的构建目录
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist

python -m PyInstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs\lhm\lib\net472\LibreHardwareMonitorLib.dll;libs\lhm\lib\net472" --add-data "app.ico;." --add-data "i18n;i18n" --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" --exclude-module "setuptools" --exclude-module "pip" --exclude-module "packaging" --exclude-module "ensurepip" --exclude-module "venv" --exclude-module "lib2to3" --exclude-module "py_compile" --exclude-module "runpy" --exclude-module "asyncio" --exclude-module "multiprocessing" --exclude-module "concurrent" --exclude-module "concurrent.futures" --exclude-module "ssl" --exclude-module "_ssl" --exclude-module "urllib" --exclude-module "http" --exclude-module "http.server" --exclude-module "http.cookiejar" --exclude-module "xmlrpc" --exclude-module "ftplib" --exclude-module "poplib" --exclude-module "imaplib" --exclude-module "nntplib" --exclude-module "telnetlib" --exclude-module "smtplib" --exclude-module "smtpd" --exclude-module "email" --exclude-module "xml" --exclude-module "xml.etree" --exclude-module "xml.dom" --exclude-module "xml.sax" --exclude-module "xml.parsers" --exclude-module "pyexpat" --exclude-module "_elementtree" --exclude-module "sqlite3" --exclude-module "_sqlite3" --exclude-module "_zstd" --exclude-module "_lzma" --exclude-module "lzma" --exclude-module "_bz2" --exclude-module "bz2" --exclude-module "gzip" --exclude-module "tarfile" --exclude-module "_decimal" --exclude-module "decimal" --exclude-module "fractions" --exclude-module "statistics" --exclude-module "numbers" --exclude-module "pickle" --exclude-module "_compat_pickle" --exclude-module "csv" --exclude-module "mimetypes" --exclude-module "quopri" --exclude-module "plistlib" --exclude-module "_pyrepl" --exclude-module "code" --exclude-module "codeop" --exclude-module "rlcompleter" --exclude-module "tty" --exclude-module "pdb" --exclude-module "profile" --exclude-module "pstats" --exclude-module "tracemalloc" --exclude-module "unittest" --exclude-module "pydoc" --exclude-module "pydoc_data" --exclude-module "test" --exclude-module "difflib" --exclude-module "pprint" --exclude-module "tkinter.test" --exclude-module "tkinter.dialog" --exclude-module "tkinter.colorchooser" --exclude-module "tkinter.font" --exclude-module "tkinter.messagebox" --exclude-module "tkinter.scrolledtext" --exclude-module "tkinter.simpledialog" --exclude-module "tkinter.tix" --exclude-module "tkinter.dnd" --exclude-module "tkinter.filedialog" --exclude-module "turtle" --exclude-module "turtledemo" --exclude-module "idlelib" --exclude-module "curses" --exclude-module "_curses" main.py

echo.
echo 打包完成！EXE 位于 dist\ChipPeek.exe
dir dist\ChipPeek.exe
pause
