from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('icecream/', include('icecream.urls')),
    path('', include('homepage.urls')),
]
