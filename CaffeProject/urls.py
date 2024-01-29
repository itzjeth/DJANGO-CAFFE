
from django.contrib import admin
from django.urls import path
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
        # ---- HOME ---- 
        path('',views.foodapp), 
        path('home',views.foodapp), 
		 path('contact',views.contact), 
            
        # ---- FOOD ---- 
        path('addcaffes',views.addcaffe),
        path('deletefood/<int:FoodId>',views.deletefood),
        path('getfood/<int:FoodId>',views.getfood),
        path('editfood/<int:FoodId>',views.updatefood),
        path('allcaffe',views.showfood),
            
        # ---- CUSTOMER ---- 
        path('addcustomer',views.addcust),
        path('deletecustomer/<int:CustId>',views.deletecust),
        path('getcustomer',views.getcust),
        path('editcustomer/<int:CustId>',views.updatecust),
        path('allcustomer',views.showcust),
    
        # ---- CUSTOMER ---- 
        path('updatepasswd',views.updatepasswd),
        path('updatepassword',views.changepass),
    
        # ---- LOGIN ---- 
        path('login',views.login),
	path('dologin',views.doLogin),
	path('logout',views.doLogout),
	
	# ---- CART ---- 
	path('addtocart/<int:FoodId>',views.addcart),
	path('allcart',views.showcart),
	path('deletecart/<int:CartId>',views.delcart),
	path('updateqnty/<str:s>',views.updateQNT),
	
	# ---- ORDER ---- 
	path('placeorder',views.placeorder),
	path('orders',views.getorder),

    # ---- MOUSEGRABBER ----
   path ('grabber', views.grabber, name="MOUSEGRABBER")
]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
