# /bin/etc/env Python
# -*- coding: utf-8 -*-
import requests

headers = {'user-agent': 'my-app/0.0.1'}
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', headers=headers)
r = requests.post('http://httpbin.org/post', headers=headers, data=payload)
print("显示返回字段", r.text)
print("显示返回状态码", r.status_code)
print("通过响应码抛出异常", r.raise_for_status())
print("显示响应头", r.headers)
print("显示Cookie", r.cookies)
print("显示网站编码", r.encoding)
