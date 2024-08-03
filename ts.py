import requests
from wxpusher import WxPusher # https://github.com/wxpusher/wxpusher-sdk-python

app_token = 'AT_vK5oR3rY68dsfTkWansUjbERriYZcILs'   # 本处改成自己的应用 APP_TOKEN
uid_myself = 'UID_GRn5qjZj2AZuBzhdbUYcUUdRfHyf'  # 本处改成自己的 UID
def wxpusher_send(msg):
    """利用 wxpusher 的 python SDK ，实现微信信息的发送"""
    result = WxPusher.send_message(msg,
                 uids=[uid_myself,],
                 token=app_token,
                 summary=msg[:99])  # 限定99个字符以内长度
    return result

def main(msg):
    result = wxpusher_send(msg)
    print(result)

if __name__ == '__main__':
    main('hello, world!')
