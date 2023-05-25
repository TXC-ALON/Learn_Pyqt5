# -*- coding: utf-8 -*-
'''
    【简介】
	查询城市天气数据
    
'''

import requests
"""
现在中国天气网的api不免费开放了,寄
https://blog.csdn.net/qq_38161040/article/details/88674203
"""
rep = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
rep.encoding = 'utf-8'

print('返回结果: %s' % rep.json() ) 
print('城市: %s' % rep.json()['weatherinfo']['city'] )
print('风向: %s' % rep.json()['weatherinfo']['WD'] )
print('温度: %s' % rep.json()['weatherinfo']['temp'] + " 度")
print('风力: %s' % rep.json()['weatherinfo']['WS'] )
print('湿度: %s' % rep.json()['weatherinfo']['SD'] )


