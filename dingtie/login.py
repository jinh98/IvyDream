from urllib import request, parse
import requests 

auth = {
    'username': 'wjy421421@gmail.com',
    'password': 'wjy421317',
    'autologin': 'on',
    'login': '登录'
}

s = requests.Session()
resp = s.post('https://www.chineseinla.com/f/page_login.html', data=auth)
# print(resp.headers)
resp = s.post('https://www.chineseinla.com/index3.php?option=com_v2_forum&task=repost&topic_id=1433169')
print(resp.text)

# auth = parse.urlencode(auth).encode()
# req =  request.Request('https://www.chineseinla.com/f/page_login.html', data=auth) # this will make the method "POST"
# resp = request.urlopen(req)

# cookie = resp.headers.get('Set-Cookie')
# print(cookie)

# charset_encoding = resp.info().get_content_charset()
# thepage = resp.read().decode(charset_encoding)
# # print(thepage)

# # handle refresh request
# req2 =  request.Request('https://www.chineseinla.com/index3.php?option=com_v2_forum&task=repost&topic_id=1433169') # this will make the method "POST"
# req2.add_header('cookie', cookie)
# resp2 = request.urlopen(req2)
# cookie2 = resp2.headers.get('Set-Cookie')
# print(cookie2)

# charset_encoding = resp2.info().get_content_charset()
# thepage2 = resp2.read().decode(charset_encoding)
# print(thepage2)


