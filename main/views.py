from django.shortcuts import render

def home(request):
    return render(request, 'cosmicflow.html')  # cosmicflow.html 파일로 연결

import os
from django.conf import settings

def home(request):
    template_path = os.path.join(settings.BASE_DIR, "main/templates/cosmicflow.html")
    print(f"템플릿 경로 확인: {template_path}")
    return render(request, 'cosmicflow.html')
