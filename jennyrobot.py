from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#*是全都要的意思

carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://img.ltn.com.tw/Upload/playing/page/2019/09/14/190914-21024-01-WvNZA.jpg',
                title='每日一療癒',
                text='description1',
                actions=[
                    PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='兩億的fun facts',
                        text='1.傲嬌\n2.愛兇狗又想跟狗玩\n3.最愛跟玩具鴨子玩\n\n但我還是超愛她🥺'

                    ),
                    URIAction(
                        label='你累了嗎？',
                        uri='https://pets.ettoday.net/'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://images2.gamme.com.tw/news2/2017/52/41/qZqZo6SVk6ecq6Q.jpg',
                title='女力健身',
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
                        label='健身正能量',
                        uri='https://www.mayyoufit.com/pages/womenfitness-article-list'
                    )
                ]
            )
        ]
    )
)


#回貼圖
sticker_message = StickerSendMessage(
    package_id='2',
    sticker_id='141'
)

sticker_please = StickerSendMessage(
    package_id='2000000',
    sticker_id='47978'
)



app = Flask(__name__)

line_bot_api = LineBotApi('b3y0S4Je04cfMocNFxrrfa/NZSl2HJzeX9pkin8BApXROSmCBn38RP1Bls7AsrqiZ9bMi4I5/i1sg93geq98Psa4wWnqaLdXHRN86FZpD2oQCyN9oncXVEHa0FzNR8Onqdtqy7LABSutvpuoGetVXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('84a3bba094b5de8e397b2d7631d6a1da')

#可以寫一個網頁https://d2e3ad207631.ngrok.io/
# @app.route("/", methods=['GET'])
# def HomePage():
#     return('''
# <table>
#     <thead>
#         <tr>
#             <th colspan="2">The table header</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>The table body</td>
#             <td>with two columns</td>
#         </tr>
#     </tbody>
# </table>
# ''')

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
        carousel_template_message)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')  
