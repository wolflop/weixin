# -*- coding: utf-8 -*-
#filename:handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "ieee158800ciqujingnian"
            li = [token, timestamp, nonce]
            li.sort()
            sha1 = hashlib.sha1()
            sha1.update(li[0].encode("utf-8"))
            sha1.update(li[1].encode("utf-8"))
            sha1.update(li[2].encode("utf-8"))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument
    def POST(self):
        try:
            webData = web.data()
            print('Handle Post webdata is ', webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                print('this is a text message')
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "你好，这是平平的背包，现在在试验阶段。"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                #print(replyMsg)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'image':
                print('this is a image mesage')
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                mediaId = recMsg.MediaId
                #picUrl = recMsg.PicUrl
                #print('the message from ', toUser)
                #print('the message to ', fromUser)
                #print('the MediaID is', mediaId)
                #print('the picUrl is ', picUrl)
                #content = "你好，这是平平的背包，现在在试验阶段。"
                #replyMsg = reply.TextMsg(toUser, fromUser, content)
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                #print(replyMsg)
                return replyMsg.send()
            else:
                print ("暂且不处理")
                return "success"
        except Exception as Argment:
            return Argment
