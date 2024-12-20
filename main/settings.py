# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # 전역 templates 폴더를 사용하려면 추가
        'APP_DIRS': True,  # 앱 내부의 templates 폴더 사용
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CSRF 관련 설정
CSRF_COOKIE_NAME = "csrftoken"  # CSRF 쿠키 이름
CSRF_COOKIE_HTTPONLY = False    # JavaScript에서 CSRF 쿠키를 접근할 수 있도록 허용
CSRF_USE_SESSIONS = False       # 세션을 사용하지 않고 쿠키에서 CSRF 토큰을 가져옴

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 이 줄이 필요합니다
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_COOKIE_SECURE = True  # 개발 환경에서는 False, 배포 시에는 True로 설정