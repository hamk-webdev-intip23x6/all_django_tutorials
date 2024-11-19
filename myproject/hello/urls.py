from django.urls import path
from . import views

app_name = 'hello' # for namespacing of urls "hello:index"
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('second/', views.second, name='second'),
]
