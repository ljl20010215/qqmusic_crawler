import requests
import execjs
import time
import json
import sys

url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'

Headers = {
    'authority': 'u.y.qq.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

with open('../js/get_searchid.js','r', encoding='utf-8') as file:
        searchid_js = execjs.compile(file.read())

with open('../js/get_sign.js','r', encoding='utf-8') as file:
        sign_js = execjs.compile(file.read())

def getSongList(search_name,cookies):
    if len(search_name)==0:
           return None
    t = str(int(time.time()*1000))
    data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":614949458,"g_tk_new_20200303":949623890,"g_tk":949623890},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"61529521097619507","search_type":0,"query":"%s","page_num":1,"num_per_page":10}}}'%(search_name)
    search_id = searchid_js.call('get_searchid')
    # print(search_id)
    data = data.replace('61529521097619507',str(search_id))
    # print(data)
    sign = sign_js.call('get_sign',data)
    params = {
        '_' : t,
        'sign' : sign
    }
    req = requests.session().post(url=url,headers=Headers,params=params,data=data.encode(),cookies=cookies)
    jsons = json.loads(req.text)

    songs = jsons['req_1']['data']['body']['song']['list']
    return songs

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(getSongList(sys.argv[1]))
    else:
        print('该函数接收一个参数')
    # songs = getSongList('honey')
    # print(songs[1].keys())
    # ['act', 'action', 'album', 'bpm', 'content', 'desc', 'desc_hilight', 'docid', 'eq', 'es', 'file', 'fnote', 'genre', 
    # 'grp', 'hotness', 'href3', 'id', 'index_album', 'index_cd', 'interval', 'isonly', 'ksong', 'label', 'language', 'lyric', 
    # 'lyric_hilight', 'mid', 'mv', 'name', 'newStatus', 'ov', 'pay', 'protect', 'sa', 'singer', 'status', 'subtitle', 'tag', 'tid', 
    # 'time_public', 'title', 'title_hilight', 'type', 'url', 'version', 'volume', 'vs']