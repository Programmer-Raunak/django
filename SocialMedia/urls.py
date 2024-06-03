from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.start     ,name='start'),
   path('f/',views.found,name='found')
]