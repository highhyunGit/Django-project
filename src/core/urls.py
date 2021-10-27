from django.urls import path
from core import views


app_name = 'core' # 네임 스페이스
urlpatterns = [
    path('', views.home, name='home'),
]
