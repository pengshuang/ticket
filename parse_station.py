# coding: utf-8

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url, verify=False)
# 我们只想要所有车站的拼音和大写字母的代号信息
stations = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys()))
pprint(stations, indent=4)


