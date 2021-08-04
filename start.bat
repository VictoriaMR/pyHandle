@echo off
rem 默认打开网址
set url=https://erp.baycheer.com/login/qrcode
rem 配置文件路径
set config_path=config.ini
rem 谷歌浏览器安装路径
set chrome="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
rem python执行路径
set python="C:\WebService\Python\python.exe"

if not exist %config_path% (
	echo %config_path% file was not exist!
	pause
	exit
)

rem 设置拼接变量
setlocal enableDelayedExpansion
set currarea=""
set cmd=''
rem 逐行读取配置文件内容
echo "chrome starting..."
for /f "tokens=1,2 delims==" %%a in (%config_path%) do (
	set aa=%%a
	set bb=%%b
	if "!aa:~0,1!" == "[" (
		if not !currarea! == "" (
			set currarea=!currarea! --no-default-browser-check --disable-popup-blocking
			start "" !currarea! 
			timeout 1 > nul
		)
		set currarea=%chrome% "%url%"
	) else (
		set currarea=!currarea! !aa!="!bb!"
	)
)
if not !currarea! == "" (
	set currarea=!currarea! --no-default-browser-check --disable-popup-blocking
	start "" !currarea!
	echo !currarea!
	timeout 1 > nul
)
setlocal disableDelayedExpansion
echo "chrome started"
timeout 2 > nul
echo "python start..."
RunHiddenConsole.exe %python% server.py 12306
echo "python started"
timeout 2 > nul