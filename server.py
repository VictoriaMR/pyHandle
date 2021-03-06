# -*- coding: utf-8 -*-
import web
import json
import time
import random
from mouse import Mouse

# url 映射
urls = ('/', 'index')
clientInfo = {'extid':''}
isFree = True
countTime = 0
intervalTime = 0
app = web.application(urls,globals())

class index:
    def GET(self):
        web.header('content-type', 'text/json;charset=utf-8')
        params = web.input(act='',x=0,y=0,w=0,nc=False,value='',extid='')
        return self.doAct(params)

    def POST(self):
        web.header('content-type', 'text/json;charset=utf-8')
        params = web.input(act='',x=0,y=0,w=0,nc=False,value='',extid='')
        return self.doAct(params)

    def error(self, msg='', code=-1):
        return json.dumps({'code':code,'data':'','msg':msg})

    def success(self, data, msg='',code=0):
        return json.dumps({'code':code,'data':data,'msg':msg})

    def check(self, params):
        if not params['action'] == 'end':
            global clientInfo, isFree, intervalTime
            if 'extid' in params:
                if not clientInfo['extid'] == '':
                    if not params['extid'] == clientInfo['extid']:
                        if intervalTime > 0 and intervalTime - int(time.time()) > 60:
                            self.clearInfo()
                            return True
                        return False
        return True

    def clearInfo(self):
        print('重置参数')
        global clientInfo, isFree, countTime, intervalTime
        clientInfo['extid'] = ''
        isFree = True
        rst = True
        countTime = 0
        intervalTime = 0
        return True

    def doAct(self, params):
        act = params['action']
        x = float(params['x'])
        y = float(params['y'])
        w = float(params['w'])
        value = params['value']

        # 动作分发
        global clientInfo, isFree, countTime, intervalTime
        rst = False
        print(act, clientInfo, isFree, countTime, intervalTime)

        if act != 'end':
            rst = self.check(params)
            if not rst:
                return self.error('客户端正在工作中, 请稍后再试')

        countTime = countTime + 1;

        if countTime >= int(random.randint(0, 10) + 10):
            self.clearInfo()
            return self.error('尝试次数过多, 请稍后再试', -4)

        intervalTime = int(time.time())

        # 点击动作
        if act == 'click':
            rst = Mouse.click(x, y)
        # 刷新动作
        elif act == 'flush':
            rst = Mouse.flush(x, y)
        # 拖动动作
        elif act == 'slider':
            rst = Mouse.slider(x, y, w)
        # 输入动作
        elif act == 'input':
            rst = Mouse.input(x, y, value)
        # 获得开始锁
        elif act == 'start':
            self.clearInfo()
            isFree = False
            clientInfo['extid'] = params['extid']
        # 释放锁
        elif act == 'end':
            if clientInfo['extid'] == params['extid']:
                self.clearInfo()

        if rst:
            return self.success(rst, '操作成功')
        else:
            return self.error('不能正确解析动作')

# 程序执行入口
if __name__ == '__main__':
    app.run()