from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'}) #HTML 요소 <태그 속성 = 속성값>

data2 = data1.findAll('dd') #dd태그 내에서 추출

fine_dust = data2[0].find('span',{'class':'num'}).text #dd태그 내의 span 태그의 텍스트(미세먼지의 농도) 추출
ultra_fine_dust = data2[1].find('span',{'class':'num'}).text #dd태그 내의 span 태그의 텍스트(초미세먼지의 농도) 추력
fine_ozone = data2[2].find('span',{'class':'num'}).text #dd태그 내의 span 태그의 텍스트(오존의 농도) 추출

print("1.미세먼지 농도 : " + fine_dust) #미세먼지 농도 출력
print("2.초미세먼지 농도 : " + ultra_fine_dust) #초미세먼지 농도 출력
print("3.오존 농도 : " + fine_ozone) #오존의 농도 출력