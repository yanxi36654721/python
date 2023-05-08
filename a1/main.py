import requests
import re
import json

url = 'https://manbo.hongdoulive.com/Activecard/episode?id=1522073681973477405&radioDramaId=1509120515875274832&t=1679236181766'  # 任意一集的链接，不能是剧集链接！
episode_id = url.split('id=')[1][:19]
radio_id = url.split('DramaId=')[1][:19]
new_url = "https://manbo.hongrenshuo.com.cn/api/v207/radio/drama/set/h5/detail?radioDramaSetId=%s&radioDramaId=%s" % (
episode_id, radio_id)
r = requests.get(new_url)
res = json.loads(r.content)
episode = []
num = str(r.content).count('vipFree')
for i in range(1, num):
    temp = str(res['b']).split("setId': ")[i]
    if 'vipFree' not in temp:
        continue
    if temp.split("'payType': ")[1][0] == '1' or temp.split("'vipFree': ")[1][0] == '1':
        episode.append(str(res['b']).split("setId': ")[i][:19])

danmu = []
for each in set(episode):
    next_url = "https://manbo.hongrenshuo.com.cn/api/v11/radio/drama/set/danmaku/h5/pull?radioDramaSetId=%s&startTime=0&endTime=10000000" % each
    r = requests.get(next_url)
    res = json.loads(r.content)['b']
    for j in res['danmakuList']:
        danmu.append(j['eid'])

print("付费集ID数：%d" % len(set(danmu)))
print("付费集弹幕数：%d" % len(danmu))
