from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ticaMgj/9p1YZDQJsA1qzW3yu5fDm2Wh0o1L6c8Avl77a74KQFDOnoUvjZgSddweUGqVBBDr3Uud1kndOKpIlrxgBli24+H2LYsP3hfjIDiPU9eCwvjyOeNSxNh1yYYOFwCVtCaGup2OdIU0yUJmjwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c9781042046451acbfe8932171e82fc1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()