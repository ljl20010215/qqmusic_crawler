import SongList
import Song
import sys

cookies = {
    'pgv_pvid': '6501256227',
    'fqm_pvqid': 'd0e8555d-abfe-47a0-9f12-6939f903cb63',
    'ts_refer': 'cn.bing.com/',
    'ts_uid': '8880615270',
    'RK': 'kVv5oji5Q+',
    'ptcz': '7ff3e8251724607a85acfcbc13ab30f84c4bb21bcdbd503a0b4c1c01b9b23a16',
    'tmeLoginType': '2',
    'euin': '7w6PNKvq7e4F',
    'fqm_sessionid': '8dda6bb8-2087-4951-87c0-47a44196884a',
    'pgv_info': 'ssid=s6364341926',
    '_qpsvr_localtk': '0.15678888757639364',
    'login_type': '1',
    'qm_keyst': 'Q_H_L_5i5C77nNjR5oct5qO2QGSOBpZh_FoICNyyEc46tGC-7OOUK4ekaFuvw',
    'psrf_access_token_expiresAt': '1697383259',
    'psrf_qqrefresh_token': 'C8F3FD3BB25B48DBBBB6CB025EF72583',
    'qqmusic_key': 'Q_H_L_5i5C77nNjR5oct5qO2QGSOBpZh_FoICNyyEc46tGC-7OOUK4ekaFuvw',
    'qm_keyst': 'Q_H_L_5i5C77nNjR5oct5qO2QGSOBpZh_FoICNyyEc46tGC-7OOUK4ekaFuvw',
    'psrf_musickey_createtime': '1689607259',
    'psrf_qqopenid': 'B29900A43763EF9B9E42F3D2657EA2E7',
    'psrf_qqaccess_token': '6309FCF45040ECABC7536C1E9A9F2703',
    'wxunionid': '',
    'wxrefresh_token': '',
    'psrf_qqunionid': 'C62217DF90B6E6A9D05A75AEDC45F914',
    'uin': '614949458',
    'wxopenid': '',
    'ts_last': 'y.qq.com/n/ryqq/search',
}

def qqmusic(song_name,index = 0):
    songList = SongList.getSongList(song_name,cookies)
    song_url, lyric = Song.getSongInfo(songList,index,song_name,cookies)
    return song_url,lyric

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url,lyric = qqmusic(sys.argv[1])
        print('音乐下载地址为：'+ url)
        print('歌词为：')
        print(lyric)
    elif len(sys.argv) == 3:
        url,lyric = qqmusic(sys.argv[1],sys.argv[2])
        print('音乐下载地址为：'+ url)
        print('歌词为： ')
        print(lyric)
    else:
        print('请输入两个参数')
