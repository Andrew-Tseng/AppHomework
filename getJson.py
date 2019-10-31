import requests
import json
data = requests.get(url="http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx")
with open("AgriculturalProductsTradingMarket.json","w",encoding="utf-8") as myFile:
    json.dump(data.json(), myFile,ensure_ascii=False)
myFile.close()