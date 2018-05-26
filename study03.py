import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME　OUT')

#除了data参数和timeout参数之外，还有context参数，必须是ssl.SSLContext类型，用来制定SSL设置
#cafile和capath这两个参数分别指定CA证书和它的路径，请求https链接时用
