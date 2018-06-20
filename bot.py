# -*- coding: utf-8 -*-
import discord
import asyncio
import response

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

@client.event
async def on_member_join(member):
    ch_name = "welcome_channel_name" # 反応させたいチャンネル名
    defchannel = discord.utils.get(member.server.channels, name=ch_name)
    m = "ようこそ、{0.mention}さん"
    await client.send_message(defchannel, m.format(member)) # メッセージ送信

    name_role = "your_add_role_name" # 付与させたい役職
    addrole = discord.utils.get(member.server.roles, name=name_role)
    await client.add_roles(member, addrole) # 役職付与

@client.event
async def on_message(message): # メッセージ受信時
    if client.user != message.author: # 自身のメッセージには反応しない
        if "じゃんけん" in message.content or "ジャンケン" in message.content: # メッセージ内容からじゃんけんするかを判別
            m = response.janken(message.content)
            # 戻り値が2個以上の場合
            if type(m) is tuple:
                await client.send_message(message.channel, 'じゃんけん、' + m[0] ) # メッセージ送信
                await client.send_message(message.channel, m[1])
            else:
                await client.send_message(message.channel, m)
        else: # じゃんけん機能以外の応答
            m = response.res_message(message.content)
            if not m: # 返答するメッセージなしの場合
                pass
            else:
                await client.send_message(message.channel, m.format(message))

client.run("BOT_TOKEN") # クライアント秘密鍵
