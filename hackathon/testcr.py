from bs4 import BeautifulSoup
import requests
import sqlite3


def insert_db(data):
    conn = sqlite3.connect("Hackathon.db")
    cur = conn.cursor()
    cur.execute("insert into cse (aTitle, aDate, aUpdate, aWriter, aView, aContent) values (?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close() 


html=requests.get('http://www.eec.pusan.ac.kr/bbs/eehome/2650/artclList.do').text
soup=BeautifulSoup(html, 'html.parser')
ports=soup.select('td._artclTdTitle a')
num=soup.select('td._artclTdNum')
Titles=[]
Dates=[]
Updates=[]
Writers=[]
Views=[]
Contents_css=[]
Contents_text=[]
for port in ports:
    url="http://www.eec.pusan.ac.kr/"+port.get('href')
    subhtml=requests.get(url).text
    subsoup=BeautifulSoup(subhtml, 'html.parser')
    aTitle=subsoup.select('.artclViewTitle')[0].text.strip()
    head=subsoup.select('.artclViewHead .right dd')
    length=len(head)
        
    aDate=subsoup.select('.artclViewHead .right dd')[length-4].text
    aUpdate=subsoup.select('.artclViewHead .right dd')[length-3].text
    aWriter=subsoup.select('.artclViewHead .right dd')[length-2].text.replace("\n", "").replace("\t", "")
    aView=subsoup.select('.artclViewHead .right dd')[length-1].text
    css=subsoup.select('.artclView')
    Contents_css.append(css)
    content=""
    for p in css:
        content=content+p.text+"\n"
    Contents_text.append(content)
    data=(aTitle, aDate, aUpdate, aWriter, aView, content)
    insert_db(data)

   


