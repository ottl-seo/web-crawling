import requests
from bs4 import BeautifulSoup

# csv 형식으로 저장하기
f = open("navertv.csv", "w")
f.write("제목, 채널명, 재생수, 좋아요\n") #수집한 데이터가 어떤 데이터인지 헤더를 넣어주는 작업 중요

raw = requests.get("https://tv.naver.com/r/")
html= BeautifulSoup(raw.text, "html.parser")
container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    # 제목에 콤마가 포함되는 경우 오류를 피하기위해 콤마를 모두 없애준다.
    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit= hit.replace("재생 수", "")
    like=like[5:]
    
    #print(title.text.strip())
    #print(chn.text.strip())
    #print(hit.text.strip())
    #print(like.text.strip())
    #print("="*50)

    f.write(title+','+chn+','+hit+','+like+'\n')

f.close()
