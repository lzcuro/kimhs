from django.urls import path
from . import views  # views.py 파일 import

urlpatterns = [
    path('', views.home, name='home'),  # 메인 페이지
]
