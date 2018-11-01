import requests
from bs4 import BeautifulSoup as bs

class Get_Data:
    def Identify(self,checker,regno,Vtype):#Both Type of car and province
        #this function is just a prototype
        if(checker == 1):
            self.login_sindh(regno,Vtype)
            self.debug(self.lists) 
            #could not do KPK yet as website is not working
    def login_sindh(self,regno,Vtype):
        self.url='http://excise.gos.pk/vehicle/vehicle_result'
        self.data={'reg_no':regno,'wheelers_type':Vtype} 
        self.doc= requests.post(self.url,data=self.data)
        self.var = bs(self.doc.text, "html.parser");
        self.lists=self.var.findAll("div",{"class":"col-md-8"})
        self.lists=self.var.findAll("h6")    
    def debug(self,lists):
        for elements in lists:
            print(elements.text);
           
                
obj=Get_Data();
obj.Identify('CK-4744',1)
