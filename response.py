import random

# "反応させたいキーワード" : "送信するメッセージ"
message_dict = {
"おはよう" : "おはようございます、{0.author.name}さん",
"こんにちは" : "こんにちは、{0.author.name}さん",
"こんばんわ" : "こんばんわ、{0.author.name}さん",
}

def res_message(message):
    for keyward in list(message_dict.keys()):
        if keyward in message:
            return message_dict[keyward]
            break
        else:
            continue

janken_dict = {
"win" : "あなたの勝ちです",
"lose" : "私の勝ちです",
"draw" : "あいこです",
}
janken_list = ["グー","チョキ","パー"]

def janken(message):
    for keyward in janken_list:
        if keyward in message:
            your_hand = keyward
            bot_janken = random.choice(janken_list) # bot側の手をランダム選出
            result = win_or_lose(your_hand , bot_janken) # 勝敗判定
            for keyward in list(janken_dict.keys()):
                if keyward in result:
                    return bot_janken , janken_dict[keyward]
                    break
                else:
                    continue
        else:
            continue

def win_or_lose(A,B):
    if ((A == "グー" and B == "チョキ") or (A == "チョキ" and B == "パー") or (A == "パー" and B == "グー")):
        return "win"
    elif ((A == "グー" and B == "パー") or (A == "チョキ" and B == "グー") or (A == "パー" and B == "チョキ")):
        return "lose"
    else:
        return "draw"
