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
        params = web.input(act='',x=0,y=0,w=0,nc=False)
        return self.doAct(params)

    def POST(self):
        web.header('content-type', 'text/json;charset=utf-8')
        params = web.input(act='',x=0,y=0,w=0,nc=False)
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

        # 动作分发
        global clientInfo, isFree, countTime, intervalTime
        rst = False
        print(act, clientInfo, isFree, countTime, intervalTime)
        if act == 'click':
            rst = self.check(params)
            if not rst:
                return self.error('客户端正在工作中, 请稍后再试')
            intervalTime = int(time.time())
            rst = Mouse.click(x, y)
        elif act == 'flush':
            rst = self.check(params)
            if not rst:
                return self.error('客户端正在工作中, 请稍后再试')
            intervalTime = int(time.time())
            rst = Mouse.flush(x, y)
        elif act == 'slider':
            rst = self.check(params)
            if not rst:
                return self.error('客户端正在工作中, 请稍后再试')
            intervalTime = int(time.time())
            countTime = countTime + 1;
            # 持续大于50 先行跳过
            rst = Mouse.slider(x, y, w)
            if countTime >= int(random.randint(0, 10) + 15):
                self.clearInfo()
                return self.error('尝试次数过多, 请稍后再试', -4)
        elif act == 'start':
            rst = self.check(params)
            if not rst:
                return self.error('客户端正在工作中, 请稍后再试')
            isFree = False
            intervalTime = int(time.time())
            clientInfo['extid'] = params['extid']
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