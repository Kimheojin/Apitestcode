# 네이버 책 소개글 검색
import os
import sys
import urllib.request

#발급받은거
client_id = "아이디"
client_secret = "비번"

encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/book_adv.json?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim&d_isbn=9791191859836" + encText # JSON 결과

request = urllib.request.Request(url)


request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)