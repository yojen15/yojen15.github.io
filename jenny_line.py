from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import * #linebot下的工具全部都要import的意思

carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://images2.gamme.com.tw/news2/2017/52/41/qZqZo6SVk6ecq6Q.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message1',
                        text='message text1'
                    ),
                    URIAction(
                        label='你累了嗎',
                        uri='https://pets.ettoday.net/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://img.ltn.com.tw/Upload/playing/page/2019/09/14/190914-21024-01-WvNZA.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageAction(
                        label='message2',
                        text='message text2'
                    ),
                    URIAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)

app = Flask(__name__)

line_bot_api = LineBotApi('b3y0S4Je04cfMocNFxrrfa/NZSl2HJzeX9pkin8BApXROSmCBn38RP1Bls7AsrqiZ9bMi4I5/i1sg93geq98Psa4wWnqaLdXHRN86FZpD2oQCyN9oncXVEHa0FzNR8Onqdtqy7LABSutvpuoGetVXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('84a3bba094b5de8e397b2d7631d6a1da')

#@app.route("/", methods=['GET'])
#def index():
    # name = request.args.get('name')
    # return "Hello"+name
 #   return "hello"

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

#@handler.add(MessageEvent, message=TextMessage)
#def message_text(event): 
    #profile = line_bot_api.get_profile("U3aca428c86db94ab1d6982d4d1ed469e")
    #if event.message.text == "WiFi密碼":
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="PELOTON-FITNESS/Password - xHFittyNe$$//PELOTON-GUEST/Password - !PelotonTP3"))
    #else: 
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Onepeloton"))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0') #開發模式，儲存後它會自動更新flask，我就不用一直下python，ngrok也不用動