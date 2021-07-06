from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser
from Spider import Spider
import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

# 從 config.ini 檔 讀入token 與 secret 參數
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 測試有沒有架站成功  
# @app.route("/")
# def helloWorld():
#     return 'hello world'

# 接收 LINE 的資訊
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    # line有一些預設訊息
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        # Phoebe 愛唱歌
        pretty_note = '~♫~♪~♬'
        pretty_text = ''
        pretty_text='我是嘟比，我喜歡唱歌~ \n'
        sp = Spider();

        for i in event.message.text:
            pretty_text += i
            pretty_text += random.choice(pretty_note)
        spmethod =sp.spiderForPttBeauty();
        pretty_text = pretty_text + '\n'+ spmethod;

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text)
        )

if __name__ == "__main__":
    app.run()