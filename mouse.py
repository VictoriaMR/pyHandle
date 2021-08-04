# -*- coding: utf-8 -*-
import pyautogui
import random
import time

class Mouse:
	def __init__(self):
		self.size = pyautogui.size();

	def click(x, y):
		time.sleep(Mouse.time())
		rst = Mouse.moveTo(x, y)
		if not rst:
			return False
		time.sleep(Mouse.time())
		pyautogui.click()
		return True

	def moveTo(x, y):
		if not pyautogui.onScreen(x, y):
			return False
		# 移动到目标鼠标位置
		while True:
			# 获取鼠标当前坐标
			mx, my = pyautogui.position()
			if mx > x:
				mx = mx - random.randint(30, 100)
				if mx < x:
					mx = x
			else:
				mx = mx + random.randint(30, 100)
				if mx > x:
					mx = x

			if my > y:
				my = my - random.randint(30, 100)
				if my < y:
					my = y
			else:
				my = my + random.randint(30, 100)
				if my > y:
					my = y

			if random.randint(0, 10) >= 6:
				pyautogui.moveTo(mx, my, Mouse.time(random.randint(2200,4400)), Mouse.getMoveType())
			else:
				pyautogui.moveTo(mx, my, Mouse.time(random.randint(2200,4400)))

			if mx == x and my == y:
				break
		return True

	def getMoveType():
		moveList = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInElastic]
		moveLen = len(moveList) - 1
		return moveList[random.randint(0, moveLen)]

	def flush(x, y):
		time.sleep(Mouse.time());

		arr = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5];
		index = random.randint(0, len(arr) - 1)
		count = arr[index];

		if random.randint(0, 5) >= 2:
			ctrl = False;

			if random.randint(0, 5) >= 2:
				ctrl = True

			if ctrl:
				pyautogui.keyDown('ctrl')
				time.sleep(Mouse.time())

			while count > 0:
				pyautogui.press('f5');
				time.sleep(Mouse.time())
				count = count - 1

			if ctrl:
				pyautogui.keyUp('ctrl')
				time.sleep(Mouse.time())
		else:
			Mouse.moveTo(x, y);
			time.sleep(Mouse.time())

			while count > 0:
				pyautogui.click()
				time.sleep(Mouse.time())
				count = count - 1

		return True

	def slider(x, y, w):
		time.sleep(Mouse.time())

		# 移动到目标鼠标位置
		rst = Mouse.moveTo(x, y)
		if not rst:
			return False

		time.sleep(Mouse.time())

		# 左键按下
		pyautogui.mouseDown(button='left')

		time.sleep(Mouse.time(500))

		# 鼠标位移
		relx = x;
		while True:
			x = x + random.randint(14, w//1)
			y = y + random.randint(-2, 3)

			if x - relx > w:
				x = relx + w

			if random.randint(0, 10) >= 5:
				pyautogui.moveTo(x, y, Mouse.time(random.randint(112, 582)), Mouse.getMoveType())
			else:
				pyautogui.moveTo(x, y, Mouse.time(random.randint(64, 782)))

			if x - relx >= w - 5:
				break

		time.sleep(Mouse.time(40))

		# 鼠标释放
		pyautogui.mouseUp(button='left')

		return True

	def time(time=100):
		return random.randint(0, 100)/time