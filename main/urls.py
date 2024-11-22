# from django.urls import path
# from . import views
# from django.contrib import admin


# urlpatterns = [
#     path('admin/', admin.site.urls)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]
