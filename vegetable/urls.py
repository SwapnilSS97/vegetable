from django.contrib import admin
from django.urls import path
from .views import veg,About,contact,signin,signup,signout,profile,fruits

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veg, name='veg'),
    path('About/', About,name='About'),
    path('contact/', contact,name='contact'),
    path('signup/', signup, name='signup'),
    path('signin/', signin,name='signin'),
    path('profile/', profile,name='profile'),
    path('signout/', signout,name='signout'),
    path('fruits/',fruits,name='fruits'),

]