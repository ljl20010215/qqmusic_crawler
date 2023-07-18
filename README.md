# qqmusic_crawler
a project including python scripts and javascripts to get qqmusic's url to download songs and lyric of songs

项目包含4个js脚本和3个python脚本文件，js脚本通过js逆向获得。
* decode_lyric.js
  用以对从qq音乐服务器获取到的歌词进行解码，获得中文歌词，从而便于展示。
* get_guid.js
  通过js算法获得guid，guid是利用时间获取到的。
* get_searchid.js
  利用js算法获得searchid参数，这个参数参与后面sign参数的加密，同样的，searchid也会利用时间戳生成。
* get_sign.js
  利用js逆向获得该脚本，该脚本会对传向服务器的data进行加密处理，服务器只能响应加密后的数据
* SongList.py
  可以通过搜索歌曲名称，获得qq音乐所搜结果的前十首歌的信息。效果相当于在搜索框中搜索歌名，得到第一页的结果。
  ![image](https://github.com/ljl20010215/qqmusic_crawler/assets/59340055/e20e6d89-896f-48b2-8571-7d1720def0bb)
  ![image](https://github.com/ljl20010215/qqmusic_crawler/assets/59340055/bcd15a86-8bd1-43ba-8674-77ee8c1c0fcb)
* Song.py
  获得十首歌中任意一首歌的信息，并利用这些信息结合js文件获得vkey等信息，最终利用获得的这些信息拼凑成可以获取音乐文件的url,除了url，还可以获得歌词等信息，该脚本实现了获取歌词的功能，若想获得其它信息，可以分析发送到服务器的各个request，对该脚本进行功能扩展。
  ![image](https://github.com/ljl20010215/qqmusic_crawler/assets/59340055/57368604-abe4-4120-a632-da527c6efa79)
* qqmusic.py
  是对SongList.py和Song.py的整合，实现最终的功能。

使用
```python
python SongList.py songName
```
可以单独运行SongList.py脚本获得前十首歌的信息。
使用
```python
python qqmusic.py songName [index]
```
可以获取前十首歌的信息,并通过index指定其中一首获得url和歌词。

该项目是一个小demo，可以集成到任意需要的项目当中去。
