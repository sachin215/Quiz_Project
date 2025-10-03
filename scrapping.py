import requests as re
from bs4 import BeautifulSoup
import pandas as pd
#url='https://www.indiabix.com/java-programming/language-fundamentals/'
url='https://www.indiabix.com/database/sql-for-database-construction-and-application-processing/'
list_dat=[]
while('#'!=url):
    response=re.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data= soup.find_all('div',class_='bix-div-container')
    
    for i in data:
        data_c={}
        data_c['Questions']=i.find_all('div',class_='bix-td-qtxt')[0].getText()
        choi=i.find_all('div',class_='bix-td-option-val')
        data_c['choice']=list(map(lambda x:x.getText(),choi))
        data_c['Answer']=i.find_all('input',attrs={'type': 'hidden'})[0].attrs['value']
        list_dat.append(data_c)
    url=soup.find('span', string='Next').find_parent('a').attrs['href']
df=pd.DataFrame(list_dat)
df.to_json('quiz2.json')