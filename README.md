# 需要安装的扩展
pip3 install web.py
pip3 install pyautogui

# 启动方式
python service.py 12306

# 多开chrome
必须指定多个chrome, 而非在同一个chrome内使用不同用户
eg. --user-data-dir="D:\chromeData\user1" --user-data-dir="D:\chromeData\user2"
使用的是完全隔离模式, 而非用户隔离模式