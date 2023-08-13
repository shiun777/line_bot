from line_bot_api import *
import requests
import flask
def google_map(event):
    
    buttons_map = TemplateSendMessage(
            alt_text= '附近資訊',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                actions=[
                    MessageTemplateAction(
                        label='附近停車場',
                        text='附近停車場'
                    ),
                    MessageTemplateAction(
                        label='附近加油站',
                        text='附近加油站'
                    ),
                    MessageTemplateAction(
                        label='附近機車行',
                        text='附近機車行'
                    ),
                    MessageTemplateAction(
                        label='附近美食',
                        text='附近美食'
                    )
                ]
            )
        )
    line_bot_api.reply_message(
        event.reply_token, 
        [buttons_map]
    )


def get_user_location(user_id, api_key):
    base_url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.post(base_url, json={})
    data = response.json()

    if "location" in data:
        location_lat = data['location']['lat']
        location_lng = data['location']['lng']
        print(f"使用者 {user_id} 的地點：緯度 {location_lat}, 經度 {location_lng}")
        return f"{location_lat},{location_lng}"

    else:
        print("無法獲取使用者地點。")
        return None

def search_nearby_parking(location, radius, api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": "parking",
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        return data['results']
    else:
        print("搜尋附近停車場失敗。狀態:", data['status'])
        return []

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'


