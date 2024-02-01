
from django.contrib import admin
from django.urls import path
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
       
        path('',views.foodapp), 
        path('home',views.foodapp), 
		 path('contact',views.contact), 
            
     
        path('addcaffes',views.addcaffe),
        path('deletefood/<int:FoodId>',views.deletefood),
        path('getfood/<int:FoodId>',views.getfood),
        path('editfood/<int:FoodId>',views.updatefood),
        path('allcaffe',views.showfood),
            
      
        path('addcustomer',views.addcust),
    
      
        path('login',views.login),
	    path('dologin',views.doLogin),
	    path('logout',views.doLogout),
	
	
	    path('addtocart/<int:FoodId>',views.addcart),
	    path('allcart',views.showcart),
	    path('deletecart/<int:CartId>',views.delcart),
	    path('updateqnty/<str:s>',views.updateQNT),
	
	
	    path('placeorder',views.placeorder),
	    path('orders',views.getorder),

   
   
]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
