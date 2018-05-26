import urllib.parse
import urllib.request

# 传递了一个参数word，值是hello，它需要被转码成bytes（字节流）类型。
# 其中转字节流采用了bytes()方法，该方法的第一个参数需要是str类型，需要用urllib.parse模块里的urlencode()方法将参数字典 转化为字符串
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')   #data = b'world=hello'
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())