from line_bot_api import *

def stock_reply_other(stockNumber):
    content_text = "即時股價和K線圖"
    text_message = TextSendMessage(
                                text= content_text,
                                quick_reply= QuickReply(
                                    items=[
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="#+股票代號查詢",
                                                    text="#"+stockNumber,
                                                )
                                        ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="K線圖",
                                                    text="@K"+stockNumber
                                                    )
                                        ),
                                    ]
                                ))
    return text_message


# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "匯率查詢(台幣對換)",
                        "weight": "bold",
                        "size": "xl",
                        "style": "normal",
                        "color": "#DDDDDD"
                    }
                    ],
                    "backgroundColor": "#444444"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美金",
                            "text": "USD"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日圓",
                            "text": "JPY"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港幣",
                            "text": "HKD"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        }
                        ],
                        "backgroundColor": "#888888"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "英鎊",
                            "text": "GBP"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#AAAAAA"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "澳幣",
                            "text": "AUD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#AAAAAA"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "加拿大幣",
                            "text": "CAD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#AAAAAA",
                            "margin": "sm"
                        }
                        ],
                        "backgroundColor": "#888888"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞士法郎",
                            "text": "CHF"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#444444"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "新加坡",
                            "text": "SGD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#444444"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非幣",
                            "text": "ZAR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#444444"
                        }
                        ],
                        "backgroundColor": "#888888",
                        "borderColor": "#888888"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞典幣",
                            "text": "SEK"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰幣",
                            "text": "THB"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "菲比索",
                            "text": "PHP"
                            },
                            "gravity": "center",
                            "style": "secondary",
                            "margin": "sm"
                        }
                        ],
                        "borderColor": "#888888",
                        "backgroundColor": "#888888"
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "印尼幣",
                            "text": "IDR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#AAAAAA"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓元",
                            "text": "KRW"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#AAAAAA"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "馬來幣",
                            "text": "MYR"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#AAAAAA"
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "越南盾",
                            "text": "VND"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#444444",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "人民幣",
                            "text": "CNY"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#444444",
                            "margin": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "紐元",
                            "text": "NZD"
                            },
                            "gravity": "center",
                            "style": "primary",
                            "color": "#444444",
                            "margin": "sm"
                        }
                        ]
                    }
                    ],
                    "backgroundColor": "#888888"
                }
        }
                    
    )
    return flex_message