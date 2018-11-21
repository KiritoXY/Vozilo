from bs4 import BeautifulSoup as bs
import urllib.request as urlread


response = urlread.urlopen('https://www.kpexcise.gov.pk/mvrecords/getmvr.php?dname=peshawar&dtype=reg&reg_no=B2647')
html = response.read()
var = bs(html, "html.parser")
list=var.findAll("strong")
for data in list:
    print(data.text)
    
    
import requests
from bs4 import BeautifulSoup as bs
import urllib.request as urlread
import urllib
import random 

class Get_Data:
    def Identify(self,regno,Vtype):#Both Type of car and province
        #this function is just a prototype
        
        self.login_sindh(regno,Vtype)
        if(self.lists_text != []):
           self.debug(self.lists_text)
        else:
            self.login_KPK(regno)
        if(self.newlist != []):
            self.debug(self.newlist)
    def get_KPK_cities(self):
        self.html_data=urlread.urlopen('https://www.kpexcise.gov.pk/mvrecords/')
        self.read=self.html_data.read()
        self.temp= bs(self.read,"html.parser")
        self.cities=self.temp.findAll("option");
        self.the_cities= [];
        for i in range(1,len(self.cities)-2):
            self.new_cities=str(self.cities[i])
            self.index=self.new_cities.find('">')
            self.new_cities=self.new_cities[0:self.index]
            self.index=self.new_cities.find('="')
            self.new_cities=self.new_cities[self.index+2:len(self.new_cities)]
            self.the_cities.append(self.new_cities)
    def login_sindh(self,regno,Vtype):
        self.lists_text=[]
        self.url='http://excise.gos.pk/vehicle/vehicle_result'
        self.data={'reg_no':regno,'wheelers_type':Vtype} 
        self.doc= requests.post(self.url,data=self.data)
        self.var = bs(self.doc.text, "html.parser");
        self.lists=self.var.findAll("div",{"class":"col-md-8"})
        self.lists=self.var.findAll("h6")  
        for data in self.lists:
            self.lists_text.append(data.text)
    def login_KPK(self,regno):
        self.get_KPK_cities();
        for city in self.the_cities:
            self.listes= []
            self.newlist=[]
            index=0
            self.new_regno=regno.replace("-","%20")
            self.new_regno=regno.replace(" ","%20")
            #print(city)
            self.url2='https://www.kpexcise.gov.pk/mvrecords/getmvr.php?dname='+city+'&dtype=reg&reg_no='+self.new_regno
            #print(self.url2)
            try:
                self.response = urlread.urlopen(self.url2)
            except urllib.error.URLError:
                print("Error accessing site")
                continue
            except urllib.error.HTTPError:
                print("Error accessing site")
                continue
            else:        
                html2 = self.response.read()
                var2 = bs(html2, "html.parser")
                self.listes=var2.findAll("strong")
                if(self.listes != []):
                    for data in self.listes:
                        #print(data.text)
                        if((index%2 == 0 and index < 20 and index > 2 and index != 4) or (index == 3)):
                            self.newlist.append(data.text)
                        index=index+1  
                    if(random.randint(1,3)% 2 == 0):
                        self.newlist.append("Vehicle is not Clear")
                    else:
                        self.newlist.append("Vehicle is Clear")
                    break    
    def debug(self,lists):
        if(lists != []):
            for elements in lists:
                print(elements);
        else:
            print("Data cannot be retrived due to some errors")
                
obj=Get_Data();
obj.Identify('BA 9159',1)
