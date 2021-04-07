
from django.contrib import admin
from django.urls import path, include
from apps.Tuluayork.views import Home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Tuluayork/', include(('apps.Tuluayork.urls','Tuluayork'))),
    path('home/', Home, name = 'index')
    
   

]
