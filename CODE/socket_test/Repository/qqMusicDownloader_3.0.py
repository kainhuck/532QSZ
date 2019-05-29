import requests
import json
import os

class QQ_music_spider():
    def __init__(self, songName):
        self.songName = songName
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
        self.get_mid()
        self.get_findUrl()
        self.get_music_url()
        self.download()

    def get_mid(self):
        url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62271055844917057&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w="+self.songName+"&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"
        r = requests.get(url, headers=self.headers)
        dict_ = json.loads(r.text)

        # 打印信息
        index = 0
        for eachSong in dict_["data"]["song"]["list"]:
            singer = ""
            for eachone in eachSong["singer"]:
                singer = singer + eachone["name"] + "/"
            singer = singer[:-1]
            print(index, eachSong["title"], singer)
            index += 1
        choose = int(input("请选择歌曲:"))

        # 获取歌手名字
        singer = ""
        for each in dict_["data"]["song"]["list"][choose]["singer"]:
            singer = singer + each["name"] + "/"
        singer = singer[:-1]

        self.filename = dict_["data"]["song"]["list"][choose]["title"] + "-" + singer
        self.songmid = dict_["data"]["song"]["list"][choose]["mid"]

    def get_findUrl(self):
        songvkey = "8495737995507689"
        dict_ = {
            "req": {
                "module": "CDN.SrfCdnDispatchServer",
                "method": "GetCdnDispatch",
                "param": {
                    "guid": "4787729008",
                    "calltype": 0,
                    "userip": ""
                }
            },
            "req_0": {
                "module": "vkey.GetVkeyServer",
                "method": "CgiGetVkey",
                "param": {
                    "guid": "4787729008",
                    "songmid": [str(self.songmid)],
                    "songtype": [0],
                    "uin": "0",
                    "loginflag": 1,
                    "platform": "20"
                }
            },
            "comm": {
                "uin": 0,
                "format": "json",
                "ct": 24,
                "cv": 0
            }
        }
        dict_ = json.dumps(dict_)
        self.findUrl = "https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey"+str(songvkey)+"&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data="+dict_

    def get_music_url(self):
        r = requests.get(self.findUrl, headers=self.headers)
        dict_ = json.loads(r.text)
        music_url = dict_["req_0"]["data"]["midurlinfo"][0]["purl"]
        music_url = "http://124.89.197.22/amobile.music.tc.qq.com/" + music_url
        self.music_url = music_url
        print(music_url)

    def download(self):
        r = requests.get(self.music_url, headers=self.headers)
        name = "QQmusic/" + self.filename + ".mp3"
        with open(name, "wb") as f:
            f.write(r.content)

if __name__ == '__main__':
    if not os.path.exists("QQmusic"):
        os.mkdir("QQmusic")
    songName = input("请输入想听的歌:")
    qq = QQ_music_spider(songName)
    print("下载结束")
