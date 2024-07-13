from prettytable import PrettyTable

from discord_webhook import DiscordWebhook

import datetime as dt

import os
import json
import csv

import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

#txt2img
import aspose.words as aw

import requests

db_path = "vlog.db"
db = sqlite3.connect(db_path)
print(db)

c = db.cursor()

#date
x = dt.datetime.now()
y1 = x.year
m2 = x.month
d3 = x.day
ymd_str = f"{y1}" + f"{m2}"+ f"{d3}"
ymd_int = int(ymd_str)
ymd_back_1 = ymd_int -1
print(ymd_str)
print(ymd_back_1)



import discord
from discord import app_commands
from discord.ext import commands
#from config import token 


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())



@client.event
async def on_ready():
    print(f'{client.user.name} 봇온라인이기')
    synced = await client.tree.sync()

@client.event
async def on_member_join(member):
    print(f'{member.namee} + "ㅎㅇ"')


@client.event
async def on_message(message):
    if not message.author.id == client.user.id:
      if "출근" in message.content:
          print("출근")
          #if message.author.id == 1212||1212 :

          #출근문자
          channel = client.get_channel('1077500489962373201')
          await message.channel.send(f"출근했습니다")
          channel = client.get_channel(1077500489962373201)
          await channel.send('출근했습니다')

      if "노무현" in message.content:
          print("1")
          await message.channel.send('응애무현')
      if "퇴근" in message.content:
          print("퇴근")
          channel = client.get_channel('1077500489962373201')
          await message.channel.send(f"퇴근했습니다")
          
          channel = client.get_channel(1077500489962373201)
          await channel.send('퇴근했습니다')

# 리퀘스트
# 디코이름 4개 날짜

# 와치
# 디코이름 찾아서 메시지

@client.tree.command(name="rrrr")
@app_commands.describe(전화번호 = "전번 , 이름 , 물품 , 주소")
#@client.tree.command(name="rrrr")
#@app_commands.describe(양식 = "a n b n c") #전번 , 이름 , 물품 , 주소
async def rrrr(interaction: discord.Interaction, 전화번호: str, 이름: str, 물품: str, 주소: str):
    n_in = (f"{전화번호}")
    number_q = '"' + str(n_in) + '"'
    print(number_q)
    print(interaction.user.id)

    d_name = interaction.user.id
    disname_q = '"' + str(d_name) + '"'
    name_in = (f"{이름}")
    name_q = '"' + name_in + '"'
    print(name_q)
    vpe_in = (f"{물품}")
    vpe_q = '"' + vpe_in + '"'
    print(vpe_q)
    location_in = (f"{주소}")

    #new_str = row.replace(')', '!')

    location_q = '"' + location_in + '"'
    print(location_q)
    time_auto = ymd_str

    sql_in = "INSERT INTO vlog Values(" + number_q +", " + disname_q + ", " + name_q + ", "+ vpe_q +", "+ location_q+", " + time_auto+ ");"
    c.execute(sql_in)
    await interaction.response.send_message("접수완료")

#    await interaction.response.send_message(f"'{양식}'")


#    a = (f"'{양식}'")
#    print(a)




@client.event
async def on_message(message):
    if not message.author.id == client.user.id:
      if "단일조회" in message.content:

        mai = message.author.id
        row = ""
        xx = PrettyTable(["전번", "디코이름", "이름", "물품", "주소", "시간"])
        for row in c.execute("SELECT * FROM vlog WHERE disname='%s'" %mai):
            fone = c.fetchone()
            #print(row)
            xx.add_row(row)
            #row = row + row
#        xx = PrettyTable(["전번", "디코이름", "이름", "물품", "주소", "시간"])
        #xx.add_row(row)
        print(xx)
        print("rowrowroworworoworworowroworoworworoworworow")
        print(row)
        channel = client.get_channel(1077814525086142474)
        #await channel.send(fone)
        #await channel.send(row)
        await channel.send(xx)       
      
      if "전체조회" in message.content:
        #if관리자 
        xx = PrettyTable(["     전번       ", "     디코이름       ", "      이름     ", "     물품   ", "    주소    ", "    시간     "])
        
        for row in c.execute("SELECT * FROM vlog"):
            print(row)
            xx.add_row(row) 
        print("21516135147197841879479817984127848791297481978249781")            
        print(row)
 
        fone = c.fetchone()
        #print(row)
#        xx.add_row(row)   
        
        fone = c.fetchall()
        print(xx)
#        with open('test.csv', 'w', encoding='utf-8') as f: 
#            writer = csv.writer(f)
#            writer.writerows(xx)
        #adad = xx
        #result = type(adad)
        adad = str(xx)
        #print(result)
        #print(fone)
        #print(fone)
        f = open("demofile3.txt", "w", encoding='utf-8')
        f.write(adad)
        f.close()

        #open and read the file after the overwriting:
        f = open("demofile3.txt", "r")
       
        #xx.add_row(row)       
        channel = client.get_channel(1077814525086142474)
        #await channel.send(xx)
#        await channel.send(row)

        #파일전송
        doc = aw.Document("demofile3.txt")
          
        for page in range(0, doc.page_count):
            extractedPage = doc.extract_pages(page, 1)
            extractedPage.save(f"Output_{page + 1}.jpg")
        
        #await channel.send(file=discord.File(r'C:\Users\noway\OneDrive\바탕 화면\Output_1.jpg'))
        url = "https://discord.com/api/webhooks/1078302613398888518/e0r224Dsyp_AGmu44tWkNDb4blWvV6KCY8dE5pn8SPpZ8Ge1Dk_3NMqRFrXr1yLWKCpo" #webhook url, from here: https://i.imgur.com/f9XnAew.png

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {    "content" : adad,
            "username" : "test"}

        #텍스트
        #봇이름


#https://discordapp.com/developers/docs/resources/channel#embed-object
#data["embeds"] = [
#    {
#        "description" : "test1111",
#        "title" : "제목"
#    }
#]
#제목
#임배드내용




        result = requests.post(url, json = data)


client.run('MTA3NzYwMTQ1ODYyODg3MDE1NA.GuWkcl.Q33Cyml__2WaZpKejk4j3gZCPwaDocd1NXTPFg')

c.execute("SELECT * FROM vlog")
fone = c.fetchone()
print(fone)
print(c.fetchall())

#저장
db.commit()
c.close()
