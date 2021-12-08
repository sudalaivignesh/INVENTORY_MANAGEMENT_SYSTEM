# -*- coding: utf-8 -*-
"""inventory management system

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sg_h2_hJ4UOcns3Z8pMOP7swvuYVnHT6
"""

import json
products={
    'p001':{"productname":"Tomato","quantity":40,"netweight in kg/L":"1","type":"veg","MRP":"40","discount":"10","sales price":36,"arrival date":"05/09/2021"},
    'p002':{"productname":"Potato","quantity":70,"netweight in kg/L":"1","type":"veg","MRP":"30","discount":"10","sales price":27,"arrival date":"04/09/2021"},
    'p003':{"productname":"Onion","quantity":70,"netweight in kg/L":"1","type":"veg","MRP":"60","discount":"0","sales price":60,"arrival time":"04/09/2021"},
    'p004':{"productname":"Cauliflower","quantity":50,"netweight in kg/L":"1","type":"veg","MRP":"30","discount":"5","sales price":28.5,"arrival time":"05/09/2021"},
    'p005':{"productname":"Green bean","quantity":40,"netweight in kg/L":"1","type":"veg","MRP":"45","discount":"5","sales price":42.75,"arrival time":"05/09/2021"},
    'p006':{"productname":"Cabbage","quantity":30,"netweight in kg/L":"1","type":"veg","MRP":"20","discount":"0","sales price":20,"arrival time":"05/09/2021"},
    'p007':{"productname":"Beetroot","quantity":30,"netweight in kg/L":"1","type":"veg","MRP":"30","discount":"10","sales price":27,"arrival time":"04/09/2021"},
    'p008':{"productname":"Brinjal","quantity":40,"netweight in kg/L":"","type":"veg","MRP":"35","discount":"5","sales price":33.25,"arrival time":"03/09/2021"},
    'p009':{"productname":"Chillies","quantity":20,"netweight in kg/L":"0.1","type":"veg","MRP":"10","discount":"5","sales price":9.5,"arrival time":"05/09/2021"},
    'p010':{"productname":"Ladies finger","quantity":40,"netweight in kg/L":"1","type":"veg","MRP":"20","discount":"5","sales price":19,"arrival time":"04/09/2021"},
    'p011':{"productname":"Carrot","quantity":50,"netweight in kg/L":"1","type":"veg","MRP":"30","discount":"10","sales price":27,"arrival time":"04/09/2021"},
    'p012':{"productname":"Ginger","quantity":45,"netweight in kg/L":"0.1","type":"veg","MRP":"10","discount":"5","sales price":9.5,"arrival time":"03/09/2021"},
    'p013':{"productname":"coconut oil","quantity":60,"netweight in kg/L":"1","type":"oil","MRP":"60","discount":"0","sales price":60,"arrival time":"13/08/2021"},
    'p014':{"productname":"sunflower oil","quantity":70,"netweight in kg/L":"1","type":"oil","MRP":"45","discount":"10","sales price":40.5,"arrival time":"13/08/2021"},
    'p015':{"productname":"sesame oil","quantity":65,"netweight in kg/L":"1","type":"oil","MRP":"65","discount":"0","sales price":65,"arrival time":"13/08/2021"},
    'p016':{"productname":"ground nut oil","quantity":75,"netweight in kg/L":"1","type":"oil","MRP":"50","discount":"15","sales price":42.5,"arrival time":"20/07/2021"},
    'p017':{"productname":"chickpeas","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"35","discount":"3","sales price":33.95,"arrival time":"10/06/2021"},
    'p018':{"productname":"black-eyed peas","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"40","discount":"0","sales price":"40","arrival time":"10/06/2021"},
    'p019':{"productname":"split pigeon peas","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"50","discount":"4","sales price":48,"arrival time":"10/06/2021"},
    'p020':{"productname":"brown chickpeas","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"50","discount":"4","sales price":48,"arrival time":"10/06/2021"},
    'p021':{"productname":"green mung bean","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"45","discount":"0","sales price":45,"arrival time":"10/06/2021"},
    'p022':{"productname":"split black gram","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"45","discount":"3","sales price":43.65,"arrival time":"10/06/2021"},
    'p023':{"productname":"hulled split green mung bean","quantity":40,"netweight in kg/L":"1","type":"dhal","MRP":"50","discount":"10","sales price":45,"arrival time":"10/06/2021"},
    'p024':{"productname":"cardamon","quantity":30,"netweight in kg/L":"0.1","type":"spice","MRP":"30","discount":"0","sales price":30,"arrival time":"13/08/2021"},
    'p025':{"productname":"cinnamon","quantity":30,"netweight in kg/L":"0.1","type":"spice","MRP":"10","discount":"5","sales price":9.5,"arrival time":"13/08/2021"},
    'p026':{"productname":"bay leaf","quantity":30,"netweight in kg/L":"0.1","type":"spice","MRP":"10","discount":"0","sales price":10,"arrival time":"13/08/2021"},
    'p027':{"productname":"star anise","quantity":30,"netweight in kg/L":"0.1","type":"spice","MRP":"20","discount":"0","sales price":20,"arrival time":"13/08/2021"},
    'p028':{"productname":"basmati rice","quantity":500,"netweight in kg/L":"1","type":"rice","MRP":"60","discount":"5","sales price":57,"arrival time":"01/08/2021"},
    'p029':{"productname":"Idly rice","quantity":450,"netweight in kg/L":"1","type":"rice","MRP":"45","discount":"4","sales price":43.2,"arrival time":"01/08/2021"},
    'p030':{"productname":"salt","quantity":36,"netweight in kg/L":"1","type":"mineral","MRP":"12","discount":"5","sales price":11.4,"arrival time":"03/09/2021"},
    }
ab=json.dumps(products)
js=open("IMS.json",'w')
js.write(ab)
js.close()
 
transaction={}
cd=json.dumps(transaction)
sj=open("TRANSACTION.json",'w')
sj.write(cd)
sj.close()
 
  
 
 
def purchase():
  total_amount=0
  phone=int(input("enter the phone number")) 
  if (len(str(phone))!=10):
    print ("please enter a 10 digit number")
    purchase()
  else:
    while(True):
      g=int(input("enter  1 for purchase and enter other 1 to finish the purchase  : "))
      if (g==1):
        product_id=input("enter the product id = ")
        quantity3=int(input("enter the required quantity = "))
        if (quantity3>=products[product_id]["quantity"]):
          print("it has only",products[product_id]["quantity"], "products")
          continue
        else:
          amount=products[product_id]["sales price"]*quantity3
          print("-------------------------------------------------------------------------------------------------")
          print("product name : ",products[product_id]["productname"])
          print("MRP : ",products[product_id]["MRP"])
          print("discount : ",products[product_id]["discount"])
          print("sales price : ",products[product_id]["sales price"])
          print("quantity : ",quantity3)
          print("amount : ",amount)
          print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
          products[product_id]["quantity"]=products[product_id]["quantity"]-quantity3
          total_amount=total_amount+amount
          continue
      else :      
        print("*******************************")
        print("total amount",total_amount)
        print("***************************")
        print("                              ......thankyou come again......                                     ")
        import time
        Time_of_Purchase=time.ctime()
        transaction[phone]={'total amount = ':total_amount,'time of purchase = ':Time_of_Purchase}
        cd=json.dumps(transaction)
        sj=open("TRANSACTION.json",'w')
        sj.write(cd)
        sj.close()
 
      break
  ab=json.dumps(products)
  js=open("IMS.json",'w')
  js.write(ab)
  js.close()
  
 
def new():
  no_products=int(input("enter the number of new products to be added"))
  print("-------------------------------------------------------------------------------------------------")
  for i in range(no_products):
    product_id=input("enter the product id = ")
    productname=input("enter the product name = ")
    quantity=int(input("enter the product quantity = "))
    netweight=int(input("enter the netweight in kg/L = "))
    product_type=input("enter the product type = ")
    MRP=int(input("enter the product MRP = "))
    discount=int(input("enter the discout % = "))
    sales_price=float(input("enter the sales price of the product = "))
    arrival_date=input("enter the arrival date = ")
    print("-------------------------------------------------")
    print ("new product  is successfully added")
    products[product_id]={'productname': productname,'quantity': quantity,'netweight in kg/L':netweight,'type': product_type,'MRP':MRP,'discount':discount,'sales price':sales_price,'arrival date':arrival_date}
    print("-------------------------------------------------")
  ab=json.dumps(products)
  js=open("IMS.json",'w')
  js.write(ab)
  js.close()
 
 
 
def edit():
  no_products=int(input("enter the number of new products to be added"))
  print("-------------------------------------------------------------------------------------------------")
  for i in range(no_products):
    product_id=input("enter the product id = ")
    quantity3=int(input("enter the product quantity = "))
    products[product_id]["quantity"]=products[product_id]["quantity"]+quantity3
    print("*************************")
    print("total quantity = ",products[product_id]["quantity"]) 
 
  ab=json.dumps(products)
  js=open("IMS.json",'w')
  js.write(ab)
  js.close()
 
 
 
print('\33[1m'"welcome to inventory")
print("-------------------------------------------------------------------------------------------------")
print("for purchase enter q ")
print("for adding new product enter w ") 
print("for increasing quantity of existing product  enter e ")
print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
user_input=input("enter your choise = ")
if (user_input=='q'):
  print("-------------------------------------------------------------------------------------------------")
  purchase()
elif (user_input=='w'):
  print("-------------------------------------------------------------------------------------------------")
  new()
elif (user_input=='e'):
  print("-------------------------------------------------------------------------------------------------")
  edit()
else:
  print("please enter valid input")
