from urllib import request, parse

data = {
'authority': 'www.chineseinla.com',
'method': 'POST',
'path': '/index3.php?option=com_v2_forum&task=repost&topic_id=1433169',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'content-length': '0',
'cookie': '__atuvc=1%7C12; usercookie[username]=101english; usercookie[password]=4dcabe09d4afd00ec5e621eca58f06f9; OSS=5; bidkc=238; PHPSESSID=ar6ver0nqthrd6ou4kkdugc6q9; __utmc=125619416; __utmz=125619416.1588456180.6.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=125619416.876524916.1584302150.1588456180.1588459988.7; ChineseInLA_data=a%3A2%3A%7Bs%3A11%3A%22autologinid%22%3Bs%3A33%3A%2212696608455eadfb3b250b13.62504565%22%3Bs%3A6%3A%22userid%22%3Bi%3A551616%3B%7D; ChineseInLA_sid=ebc33e64df41a9f33072d234f83afa29; __utmt=1; 1162d0aafa419e168e822590aec845fe=cbd5b08a32358c4466c962f6bdf925e2; ChineseInLA_t=a%3A1%3A%7Bi%3A1433169%3Bi%3A1588461623%3B%7D; __utmb=125619416.7.10.1588459988; b9afd5446abb1cde865304652e2c04b9=87754101b25ef296edc28f518fa62cf0; bidks=462',
'origin': 'https://www.chineseinla.com',
'referer': 'https://www.chineseinla.com/f/page_viewtopic/t_1433169.html',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}

data = parse.urlencode(data).encode()
req =  request.Request('https://www.chineseinla.com/index3.php?option=com_v2_forum&task=repost&topic_id=1433169') # this will make the method "POST"
resp = request.urlopen(req)

charset_encoding = resp.info().get_content_charset()
thepage = resp.read().decode(charset_encoding)
print(thepage)

cookie = resp.headers.get('Set-Cookie')
print(cookie)
