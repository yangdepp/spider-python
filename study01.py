import urllib.request

response = urllib.request.urlopen('https://cs.zbj.com')
# 输出python官网的源代码
print(response.read().decode('utf-8'))
print('-'*50)
# 利用type()方法输出响应的类型
# <class 'http.client.HTTPresponse'>
print(type(response))
print('-'*50)

# 把返回的赋值给一个response对象，这个对象拥有以下方法
print(response.status)  # 返回的状态码200
print(response.getheaders())  # 响应头信息
print(response.getheader('Server'))  # server是nginx

#---------------------------------------------------------
