import requests
# **********放在execjs模块之前，解决execjs执行js产生的乱码报错************
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# ********************************************************************
import execjs
import SongList
import time

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

with open('../js/get_guid.js','r', encoding='utf-8') as file:
    guid_js = execjs.compile(file.read())

with open('../js/get_sign.js','r', encoding='utf-8') as file:
    sign_js = execjs.compile(file.read())

with open('../js/decode_lyric.js','r',encoding='utf-8') as file:
    decode_lyric_js = execjs.compile(file.read())

def getSongInfo(songList,index,name,cookies):
    if str(type(songList)).split(' ')[1][1:-2] != 'list' or len(songList) == 0:
        songList = SongList.getSongList(name)

    song = songList[index]
    songmid = song['mid']
    songtype = '['  + str(song['type']) + ']'
    id = song['id']
    album_mid = song['album']['mid']
    t = str(int(time.time()*1000))
    data = '''{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":614949458,"g_tk_new_20200303":949623890,"g_tk":949623890},
    "req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6959513748","songmid":["%s"],"songtype":%s,"uin":"614949458","loginflag":1,"platform":"20"}},
    "req_2":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["%s"]}},
    "req_3":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"%s","songID":%d}},
    "req_4":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"%d","biz_sub_type":0}]}},
    "req_5":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"%s"}},
    "req_6":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7514346228","songmid":["%s"],"songtype":%s,"uin":"614949458","loginflag":1,"platform":"20"}},
    "req_7":{"module":"music.trackInfo.UniformRuleCtrl","method":"CgiGetTrackInfo","param":{"ids":[%d],"types":%s}}}'''%(songmid,songtype,songmid,songmid,id,id,album_mid,songmid,songtype,id,songtype)

    guid = guid_js.call('get_A')
    data = data.replace('6959513748',guid)
    guid = guid_js.call('get_A')
    data = data.replace('7514346228',guid)

    sign = sign_js.call('get_sign',data)

    params = {
        '_': t,
        'sign': sign,
    }
    req = requests.post(url=url,headers=Headers,params=params,cookies=cookies,data=data.encode())
    jsons = req.json()
    song_url = 'https://dl.stream.qqmusic.qq.com/'+jsons['req_6']['data']['midurlinfo'][0]['purl']
    lyric = jsons['req_3']['data']['lyric']
    lyric = decode_lyric_js.call('get_lyric',lyric)
    return song_url,lyric


if __name__ == '__main__':
    song_url,lyric = getSongInfo([],0,'那年夏天宁静的海')
    print(lyric)