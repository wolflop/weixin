#-*- coding: utf-8 -*-
#filename:main.py

import web
from handle import Handle

#指定url，并指定handle的类
urls = (
        '/wx', 'Handle',
)

if __name__ =='__main__':
    app = web.application(urls, globals()) #创建web实例  
    app.run()        #运行

