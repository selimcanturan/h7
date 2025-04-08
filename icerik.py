import requests
from bs4 import BeautifulSoup
from collections import deque
import threading
    #icerik.py h7 , tarih, başlık, içerik icerik.txt ye atsın noktalı virgül ile ayırsın
linkk="https://www.milligazete.com.tr/haber/24163445/mart-ayinda-odeme-basladi-anneler-basvurursa-alabiliyor"

def icerik_al(url):
    yeni_url = requests.get(url)
    soup = BeautifulSoup(yeni_url.content,'html.parser')
    #################başlık
    title = soup.find("h1", {"itemprop": "headline"})
    baslik=title.get_text(strip=True)
    ##################tarih
    tarih=soup.find("span", {"class": "tarih"})
    tarih_yaz=tarih.get_text(strip=True)
    #print(tarih_yaz)
    ###################içerik
    icerik= soup.find("div", {"class": "post-text mb20 word em dark-1 tleft detay", "itemprop": "articleBody"})
    icerik_yaz=icerik.get_text(strip=True)
    #print(icerik_yaz)
    #################dosyala
    str= f"{tarih_yaz}; {baslik}; {icerik_yaz}"
    f = open("icerik.txt","w")
   # print(baslik,";","\n","Tarih; ",tarih_yaz,"\n","İçerik; ",icerik_yaz,"\n", file=f)
    print(str, file=f)
    f.close()
icerik_al(linkk)
