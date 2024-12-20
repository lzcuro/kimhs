from django.urls import path
from . import views  # views.py 파일 import

urlpatterns = [
    path('', views.home, name='home'),  # 메인 페이지
    path('section/<int:section_id>/', views.detail_page, name='detail'),  # 상세 페이지 URL
    path('save-section/', views.save_section, name='save_section'),
    path('get-sections/', views.get_sections, name='get_sections'),
    path('category/', views.category_view, name='category'),  # 카테고리 페이지 기본 URL
    path('category/<str:category_name>/', views.category_detail_view, name='category_detail'),  # 카테고리별 상세 페이지 URL
    path('example/', views.example, name='example'),
    path('qa/', views.qa, name='qa')
]
