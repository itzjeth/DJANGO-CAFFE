from django.shortcuts import render, redirect
from django.db import connection, transaction
from foodapp.forms import FoodForm,CustForm,AdminForm,CartForm,OrderForm
from foodapp.models import Food,Cust,Admin,Cart,Order
import datetime

cursor = connection.cursor()

# Create your views here.

def foodapp(request):
	return render(request,'index.html')

def contact(request):
	return render(request,'contact.html')

def addcaffe(request):
	
	if request.method=="POST":
		form = FoodForm(request.POST,request.FILES)
		if form.is_valid():
			try:
				form.save()
				return redirect("/allcaffe")
			except:
				return render(request,"error.html")
	else :
		form = FoodForm()
	return render(request,'addcaffe.html',{'form':form})
	
def showfood(request):
	foods = Food.objects.all()
	return render(request,'foodlist.html',{'foodlist':foods})
	
def deletefood(request,FoodId):
	foods = Food.objects.get(FoodId=FoodId)
	foods.delete()
	return redirect("/allcaffe")
	
def getfood(request,FoodId):
	foods = Food.objects.get(FoodId=FoodId)
	return render(request,'updatefood.html',{'f':foods})
	
def updatefood(request,FoodId):
	foods = Food.objects.get(FoodId=FoodId)
	form = FoodForm(request.POST,request.FILES,instance=foods)
	if form.is_valid():
		form.save()
		return redirect("/allcaffe")
	return render(request,'updatefood.html',{'f':foods})
	
def addcust(request):
	if request.method=="POST":
		form = CustForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("/login")
			except:
				return render(request,"error.html")
	else :
		form = CustForm()
	return render(request,'addcust.html',{'form':form})
	
	
def login(request):
	return render(request,'login.html')
	
def doLogin(request):
	if request.method=="POST":
		uid = request.POST.get('userId','')
		upass = request.POST.get('userpass','')
		utype = request.POST.get('type','')
		
		if utype == "Admin":
			for a in Admin.objects.raw('Select * from FP_Admin where AdminId="%s" and AdminPass="%s"'%(uid,upass)):
				if a.AdminId==uid:
					request.session['AdminId']=uid
					return render(request,"index.html",{'success':'Welcome '+a.AdminId})
			else:
				return render(request,"login.html",{'failure':'Incorrect login details'})
					
		if utype == "User":
			for a in Cust.objects.raw('Select * from FP_Cust where CustEmail="%s" and CustPass="%s"'%(uid,upass)):
				if a.CustEmail==uid:
					request.session['CustId']=uid
					return render(request,"index.html",{'success':'Welcome '+a.CustEmail})
			else:
				return render(request,"login.html",{'failure':'Incorrect login details'})
				
def doLogout(request):
	key_session = list(request.session.keys())
	for key in key_session:
		del request.session[key]
	return render(request,'index.html',{'success':'Logged out successfully'})


def addcart(request,FoodId):
	sql = ' Insert into FP_Cart(CustEmail,FoodId,FoodQuant) values("%s","%d","%d")'%(request.session['CustId'],FoodId,1)
	i=cursor.execute(sql)
	transaction.commit()
	return redirect('/allcaffe')
	
def delcart(request,CartId):
	cart = Cart.objects.get(CartId=CartId)
	cart.delete()
	return redirect("/allcart")
	
def showcart(request):
	cart=Cart.objects.raw('Select CartId,FoodName,FoodPrice,FoodQuant,FoodImage from FP_Food as f inner join FP_Cart as c on f.FoodId=c.FoodId where c.CustEmail="%s"'%request.session['CustId'])
	transaction.commit()
	return render(request,"cartlist.html",{'cartlist':cart})
	

def placeorder(request):
        if request.method=="POST":
                price=request.POST.getlist('FoodPrice','')
                q=request.POST.getlist('FoodQuant','')
                total=0.0
                for i in range(len(price)):
                    total=total+float(price[i])*float(q[i])
                today = datetime.datetime.now()
                sql = 'insert into FP_Order(CustEmail,OrderDate,TotalBill) values ("%s","%s","%f")' %(request.session['CustId'],today,total)
                i=cursor.execute(sql)
                transaction.commit()
                sql1= 'select * from FP_Order where CustEmail="%s" and OrderDate="%s"'%(request.session['CustId'],today)
                sql = 'delete from FP_Cart where CustEmail="%s"' %(request.session['CustId'])
                i=cursor.execute(sql)
                transaction.commit()
                
                od=Order()
                
                for o in Order.objects.raw(sql1):
                        if o.CustEmail==request.session['CustId']:
                                od=str(o.OrderId)
                                return render(request,'index.html',{'success':'Order placed sucessfully!!!'+str(o.OrderId)})
        else:
        	pass

def getorder(request):
	orders = Order.objects.all()
	return render(request,'orderlist.html',{'orderlist':orders})

def updateQNT(request,s):
	print(s)
	ind=s.index('@')
	cartId=int(s[:ind])
	qt=int(s[ind+1:])
	sql="update FP_Cart set FoodQuant='%d' where CartId='%d'"%(qt,cartId)
	i=cursor.execute(sql)
	transaction.commit()

