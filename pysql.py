import datetime as dt

import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

from prettytable import PrettyTable

#db 생성
#CREATE TABLE "vlog" (
#	"number"	TEXT,
#	"disname"	TEXT,
#	"name"	TEXT,
#	"vpe"	TEXT,
#	"location"	TEXT,
#	"time"	INTEGER
#);

db_path = "vlog.db"
db = sqlite3.connect(db_path)
print(db)

c = db.cursor()

#1. 회원가입 후 저장, 이후 로그생성
#2. 마지막꺼만 

#0 등록 value list

#날짜 : db-time에 ymd_str추가 ymd_back_1로 기록 sort, 조회
x = dt.datetime.now()
y1 = x.year
m2 = x.month
d3 = x.day
ymd_str = f"{y1}" + f"{m2}"+ f"{d3}"
ymd_int = int(ymd_str)
ymd_back_1 = ymd_int -1
print(ymd_str)
print(ymd_back_1)

#전체삽입문
#c.execute("INSERT INTO vlog \
#	VALUES('1',"1","1","1","1",'1')")
#   VALUES(number, disname, name, vpe, location, time)")
#c.execute("INSERT INTO vlog(id, name, birthday) \
#    VALUES(?,?,?)", //
#    ('1',"1","1","1","1",'1'))

n_in = 11
number_q = '"' + str(n_in) + '"'
disname_q = '"' + "discordname" + '"'
name_q = '"' + "name" + '"'
vpe_q = '"' + "이거,저거"+ '"'
location_q = '"' + "어디" + '"'
time_auto = ymd_str #34번줄 ymd_int = int(ymd_str)

print("INSERT INTO vlog Values('1', '1', '1', '12', '1', '1');")
sql_in = "INSERT INTO vlog Values(" + number_q +", " + disname_q + ", " + name_q + ", "+ vpe_q +", "+ location_q+", " + time_auto+ ");"
print(sql_in)
#c.execute("INSERT INTO vlog Values('1', '1', '1', '12', '1', '1');")
c.execute(sql_in)

print("pass input after")

#수정 edit value
#c.execute("INSERT INTO vlog Values('Derick', '010-1234-5678');")

#단일보기 print
phonenum2see = 11
#print(type(phonenum2see))
print("11")
for row in c.execute("SELECT * FROM vlog WHERE number='%s'" %phonenum2see):
    print("1")
    print(row)
#    row= row +row
    #new_str = row.replace(')', '!')

xx = PrettyTable(["전번", "디코이름", "이름", "물품", "주소", "시간"])
#xx.set_field_align("전번", "l") 
# Left align city names
#xx.set_padding_width(1) # One space between column edges and contents (default)
xx.add_row(row)
print(xx)

##address string 치환
#new_str = str.replace('-', '!')
#new_str = str.replace('!', '-')

print("1")
print(row)
#전체로그 보기
#c.execute("SELECT * FROM vlog")
#fone = c.fetchone()
#print(fone)
#print(c.fetchall())

#저장
db.commit()
c.close()



from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='your webhook url', content='Webhook Message')
response = webhook.execute()