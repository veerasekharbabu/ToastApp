from flask import Flask, render_template
import pandas as pd
from pymongo import MongoClient
from flask_jsonpify import jsonpify
import time
import re
from livereload import Server
from flask import render_template
from IPython.display import HTML,display
from sshtunnel import SSHTunnelForwarder
app = Flask(__name__)
 
i=1
@app.route("/")
def index():
 val = input("Enter Menu or order")
#va11=input("Enter order to give the order")

 host = "127.0.0.1"
 #MONGO_DB = "DATABASE_NAME"
 user = "admin"
 password = "password"
 port = int(27017)
 global i
 if val in "Menu" and i==1:
  client = MongoClient()
  i=i+1
  #client.admin.authenticate('username', 'pass', mechanism = 'SCRAM-SHA-1')
  mydatabase = client["Toastapp111"]
  Menu111 = mydatabase["Menu111"]
  #client1 = client.Menu111.authenticate(username="admin",password="password")
  #Menu111.remove({})
  rec1=[{
  
  'item': 'veg Biriyani', 
  'cost': '200' , 
  },
  {
 
  'item': 'fish Biriyani', 
  'cost': '300' ,
  },
  {
  
  'item': 'chicken Biriyani', 
  'cost': '250' ,
  },
  {
 
  'item': 'Mutton Biriyani', 
  'cost': '400' ,
  }]
  
# inserting the data in the database
  rec = mydatabase.Menu111.insert(rec1)
  
  global df
  df = pd.DataFrame(list(mydatabase.Menu111.find()))
  df = df.filter(['item','cost'], axis=1)
  df=df.drop_duplicates()
  #df=df.drop_duplicates(keep='first',inplace=True)
  #df1=pd.DataFrame()
  html1 = df.to_html(escape=False)
  #render_template("Menu1.html", html_data = html1)
  #print(html1)
  client.close()
  #server = SSHTunnelForwarder(MONGO_HOST,ssh_username=MONGO_USER,ssh_password=MONGO_PASS,remote_bind_address=('127.0.0.1', 27017))
  #server.start()
  #MongoClient("mongodb://{user}:{password}@{host}:{port}")
  ad1= input("If Admin type yes else No")
  
  if 'yes' in ad1:
   ad2 = input("Enter add ,edit or delete")
   if 'add' in ad2:
    try:
     client1 = MongoClient()
    except:
     print("An exception occurred") 
    if client1 != None:
     Menu1 = input("Enter New menu item name")
     cost1=  input("Enter cost of the menu entered")
     rec11 = [{
     'item': Menu1, 
     'cost': cost1, 
     }]
     rec0= mydatabase.Menu111.insert(rec11)
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     
   #df1=pd.DataFrame()
     html1 = df.to_html(escape=False)
   #render_template("Menu1.html", html_data = html1)
     #print(html1)
     return render_template("Menu1.html", html_data1 = html1)
   if 'delete' in ad2:
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     ad3 = int(input("enter index number to remove food item"))
     df=df.drop(ad3)
     #df = pd.DataFrame(df.values.tolist())
     df=df.reset_index(drop=True)
     html1 = df.to_html(escape=False)
   #render_template("Menu1.html", html_data = html1)
     #print(html1)
     return render_template("Menu1.html", html_data1 = html1)
   if 'edit' in ad2:
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     ed1food=str(input("food that needs updated cost"))
     #print(len(df.index))
     #j=0
     
     ed1old=input("cost that needs to be changed")
     ed1new=input("enter updated cost")
     #if ed1food in df['item'].to_list():
      #df_list = df['item'].index.tolist()
      #print(df_list)
      #idx = df['item'].to_list().index(ed1food)
     idx1 =df['item'].to_list().index(ed1food)
     print(idx1)
     listcost1=df['cost'].to_list()
     print(listcost1)
	 
     listitem1=df['item'].to_list()
     print(listitem1)
     listcost11=[]
     for k in range(0,len(listcost1)):
      if listcost1[k] ==ed1old and listitem1[k] == ed1food:
       listcost1[k]=ed1new
      
	  
      #listcost1[idx1]=ed1new
      df =pd.DataFrame(list(zip(listitem1, listcost1)),columns =['item', 'cost'])
	  #print(idx)
      #df[idx][idx].replace({ 'item':{ed1food: ed1food},'cost':{ed1old: ed1new}}) 
     #df = df.filter(['item','cost'], axis=1)
     #df=df.drop_duplicates()
     #df=df.reset_index(drop=True)
      html1 = df.to_html(escape=False)
     else:
      html1 = df.to_html(escape=False) 
     return render_template("Menu1.html", html_data1 = html1) 	
  if 'No' in ad1:
   #df = pd.DataFrame(list(mydatabase.Menu111.find()))
   #df = pd.DataFrame(df.values.tolist())
   df = df.filter(['item','cost'], axis=1)
   df=df.drop_duplicates()
   df=df.reset_index(drop=True)
   html1 = df.to_html(escape=False)
   #print(html1)
   return render_template("Menu1.html", html_data1 = html1)
  
  df = pd.DataFrame(list(mydatabase.Menu111.find()))
  df = df.filter(['item','cost'], axis=1)
  df=df.drop_duplicates()
  df=df.reset_index(drop=True)
  html1 = df.to_html(escape=False)
  #return render_template("Menu1.html", html_data1 = html1)
 if val in "Menu" and i >=1:
  client = MongoClient()
  i=i+1
  #client.admin.authenticate('username', 'pass', mechanism = 'SCRAM-SHA-1')
  mydatabase = client["Toastapp111"]
  Menu111 = mydatabase["Menu111"]
  #client1 = client.Menu111.authenticate(username="admin",password="password")
  #Menu111.remove({})
  df = df.filter(['item','cost'], axis=1)
  df=df.drop_duplicates()
  #df=df.drop_duplicates(keep='first',inplace=True)
  #df1=pd.DataFrame()
  html1 = df.to_html(escape=False)
  #render_template("Menu1.html", html_data = html1)
  print(html1)
  client.close()
  #server = SSHTunnelForwarder(MONGO_HOST,ssh_username=MONGO_USER,ssh_password=MONGO_PASS,remote_bind_address=('127.0.0.1', 27017))
  #server.start()
  #MongoClient("mongodb://{user}:{password}@{host}:{port}")
  ad1= input("If Admin type yes else No")
  
  if 'yes' in ad1:
   ad2 = input("Enter add ,edit or delete")
   if 'add' in ad2:
    try:
     client1 = MongoClient()
    except:
     print("An exception occurred") 
    if client1 != None:
     Menu1 = input("Enter New menu item name")
     cost1=  input("Enter cost of the menu entered")
     rec11 = [{
     'item': Menu1, 
     'cost': cost1, 
     }]
     rec0= mydatabase.Menu111.insert(rec11)
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     
   #df1=pd.DataFrame()
     html1 = df.to_html(escape=False)
   #render_template("Menu1.html", html_data = html1)
     #print(html1)
     return render_template("Menu1.html", html_data1 = html1)
   if 'delete' in ad2:
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     ad3 = int(input("enter index number to remove food item"))
     df=df.drop(ad3)
     #df = pd.DataFrame(df.values.tolist())
     df=df.reset_index(drop=True)
     html1 = df.to_html(escape=False)
   #render_template("Menu1.html", html_data = html1)
     print(html1)
     return render_template("Menu1.html", html_data1 = html1)
   if 'edit' in ad2:
     df = pd.DataFrame(list(mydatabase.Menu111.find()))
     df = df.filter(['item','cost'], axis=1)
     df=df.drop_duplicates()
     df=df.reset_index(drop=True)
     print(df)
     ed1food=str(input("food that needs updated cost"))
     #print(len(df.index))
     #j=0
     
     ed1old=input("cost that needs to be changed")
     ed1new=input("enter updated cost")
     #if ed1food in df['item'].to_list():
      #df_list = df['item'].index.tolist()
      #print(df_list)
      #idx = df['item'].to_list().index(ed1food)
     idx1 =df['item'].to_list().index(ed1food)
     print(idx1)
     listcost1=df['cost'].to_list()
     print(listcost1)
	 
     listitem1=df['item'].to_list()
     print(listitem1)
     listcost11=[]
     for k in range(0,len(listcost1)):
      if listcost1[k] ==ed1old and listitem1[k] == ed1food:
       listcost1[k]=ed1new
      
	  
      #listcost1[idx1]=ed1new
      df =pd.DataFrame(list(zip(listitem1, listcost1)),columns =['item', 'cost'])
	  #print(idx)
      #df[idx][idx].replace({ 'item':{ed1food: ed1food},'cost':{ed1old: ed1new}}) 
     #df = df.filter(['item','cost'], axis=1)
     #df=df.drop_duplicates()
     #df=df.reset_index(drop=True)
      html1 = df.to_html(escape=False)
     else:
      html1 = df.to_html(escape=False) 
     return render_template("Menu1.html", html_data1 = html1) 	
     	
  if 'No' in ad1:
   #df = pd.DataFrame(list(mydatabase.Menu111.find()))
   #df = pd.DataFrame(df.values.tolist())
   df = df.filter(['item','cost'], axis=1)
   df=df.drop_duplicates()
   df=df.reset_index(drop=True)
   html1 = df.to_html(escape=False)
   print(html1)
   return render_template("Menu1.html", html_data1 = html1) 
  
 if val in "order":
   client = MongoClient()
   mydatabase = client["Toastapp111"]
   Menu111 = mydatabase["Menu111"]
   order1 = mydatabase['order1']
   order1.remove({})
   if i ==1:
    df = pd.DataFrame(list(mydatabase.Menu111.find()))
   df = df.filter(['item','cost'], axis=1)
   df=df.drop_duplicates()
   df=df.reset_index(drop=True)
   print(df)
   print("order from menu items untill No")
   df = pd.DataFrame(list(mydatabase.Menu111.find()))
   #df1=pd.DataFrame(list(mydatabase.order1.find()))
   #print(df)
   #for doc1 in mydatabase.Menu111.find():
      #print(doc1)
   Val1=''	  
   while Val1 != 'No':	  
    Val1 = input("Enter order item")
   #mydatabase.Menu111.createIndex( { "$**": "text" } )
    pattern=re.compile(Val1)
    for doc in mydatabase.Menu111.find():
    #print(doc)
    
     if Val1 in pattern.findall(str(doc)):
      mydatabase.order1.insert(doc)
    #else:
     # print("item not there")
	  
    #df1=pd.DataFrame(list(mydatabase.order1.find()))
   print("ordered items are")
   #for doc11 in mydatabase.order1.find():
      #print(doc11)
   df1=pd.DataFrame(list(mydatabase.order1.find()))
   df1 = df1.filter(['item','cost'], axis=1)
   df1=df1.drop_duplicates()
   df1=df1.reset_index(drop=True)
   print(df1)
   
   html = df1.to_html(escape=False)
   #print(html)
 
 #if val is "Menu":
  #return render_template("Menu1.html", html_data1 = html1)
  
 #if val is "order":
   return render_template("first1.html", html_data = html)
 if __name__ == "__main__":
    app.run(debug=True) 
