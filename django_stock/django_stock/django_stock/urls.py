from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('stocks/index.html', include('stocks.urls')), #메인화면
    path('admin/', admin.site.urls),
]