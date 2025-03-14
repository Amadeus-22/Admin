from django.contrib import admin
from django.urls import path, include # The idea behind include() is to make it easy to plug-and-play URLs. See more at documentation

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
