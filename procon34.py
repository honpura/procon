import requests
import json

# URLの設定
urlGetMatch = "http://localhost:3000/"
urlGetStatus = "http://localhost:3000/" + str(id)
urlPost = "http://localhost:3000/" + str(id)

API_TOKEN = "hongo8963580c45b8202fc1d89917f4c83f268b78a26668753c0e05c66d58be9" #　事前に配布されるトークンを設定

# API接続
responceMatch = requests.get(urlGetMatch,
                        params={
                            "token": API_TOKEN
                            }
                        )

if 'json' in responceMatch.headers.get('content-type'):
    matchData = responceMatch.json()
    print(matchData)
else:
    matchData = responceMatch.text
    print(matchData)

responceStatus = requests.get(urlGetStatus,
                          params={
                              "token": API_TOKEN
                            }
                        )

if 'json' in responceStatus.headers.get('content-type'):
    statusData = responceStatus.json()
    print(statusData)
else:
    statusData = responceStatus.text
    print(statusData)

payload = {
    "turn": 1,
    "actions": [
        {
            "type": [],
            "dir": []
        }
    ]
}

# 試合の情報を取得
# integer
id = matchData['matches'][0]['id'] # 試合のID
turns = matchData['matches'][0]['turns'] # 試合のターン数
turnSeconds = matchData['matches'][0]['turnSeconds'] # 試合のターンあたりの秒数
width = matchData['matches'][0]['board']['width'] # フィールドの横の数
height = matchData['matches'][0]['board']['height'] # フィールドの縦の数
mason = matchData['matches'][0]['board']['mason'] # 職人の数
turn = statusData['turn'] # 何ターン目か

# boolean
isFirst = matchData['matches'][0]['first'] # 先手かどうか [True:yes False:no]

# array
walls = statusData['board']['walls'] # “現在”の配置されている城壁の情報 [0:なし 1:自チームの城壁 2:相手チームの城壁]
territories = statusData['board']['territories'] # “現在”の陣地の情報 [0:中立 1:自チームの陣地 2:相手チームの陣地]
structures = statusData['board']['structures'] # “現在”の配置されている構造物 [0:無配置 1:池 2:城]
masons = statusData['board']['masons'] # “現在”の配置されている職人の位置と番号 [自チームの職人のIDが正、相手チームの職人のIDが負]


# ---------以下にコード記入----------

print(responceMatch.status_code)

# ---------------------------------

requests.post(urlPost, data=payload)