import requests as req
from bs4 import BeautifulSoup

url="https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx"
header={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding":"",
"accept-language":"en-US,en;q=0.9",
"cache-control":"max-age=0",
"sec-ch-ua":'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":'"Windows"',
"sec-fetch-dest":"document",
"sec-fetch-mode":"navigate",
"sec-fetch-site":"none",
"sec-fetch-user":"?1",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
def scrapers():
  res1=req.get(url,headers=header)
  soup = BeautifulSoup(res1.content, 'html5lib')
  ti=soup.find_all("tbody")[-1]
  datalist=[]
  for i in ti.find_all("tr",class_="tdcolumn"):
      all_data=i.find_all("td")
      datalist.append(tuple([a.text for a in all_data]))
  return datalist