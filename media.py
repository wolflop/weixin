# -*- coding: utf-8 -*-
# filename:media.py
from basic import Basic
import urllib
import json
import poster3.encode
from poster3.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        register_openers()
    #上传图片
    def upload(self, accessToken, filepath, mediaType):
        openFile = open(filepath, 'rb')
        param = {'media' : openFile}
        postData, postHeaders = poster3.encode.multipart_encode(param)
        postUrl = "https://api.webixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToke
n, mediaType)
        request = urllib.request.Request(postUrl, postData, postHeaders)
        urlResp = urllib.request.urlopen(request)
        print(urlRest.read())

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToke
n, mediaId)
        urlResp = urllib.request.urlopen(postUrl)
        print(urlResp)
        headers = urlResp.info().__dict__['headers']
        if ("Content-Type: application/json\r\n" in headers) or ('Content-Type: text/plain\r\n' in header
s):
            jsonDict = json.loads(urlResp.read())
            print(jsonDict)
        else:
            buffer = urlResp.read() # 素材的二进制
            mediaFile = file("test_meida.jpg", "wb")
            meidaFile.write(buffer)
            print("get successful")

if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "/home/ubuntu/1.jpg"
    mediaType = "image"
    myMedia.upload(accessToken, filePath, mediaType)
    #mediaType = "news"
    #mediaId = "2ZsPnDj9XIQlGfws31MUfR5Iuz-rcn7F6LkX3NRCsw7nDpg2268e-dbGB67WWM-N"
    #myMedia.get(accessToken, mediaId)
