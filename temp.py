#from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup as bs
url='http://excise.gos.pk/vehicle/vehicle_result'
data={
      'reg_no':'CK-4744',
      'wheelers_type':'1'
}   
doc= requests.post(url,data=data)
#print(doc.text)
var = bs(doc.text, "html.parser")
print("Url Parsered")
list=var.findAll("div",{"class":"col-md-8"})
list=var.findAll("h6")
    for info in list:
        print(info.text)
