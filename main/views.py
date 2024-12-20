from django.shortcuts import render, get_object_or_404
from .models import Section
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

# 메인 페이지 (섹션 리스트)
def main_page(request):
    sections = Section.objects.all()  # 모든 섹션 데이터 불러오기
    return render(request, 'main_page.html', {'sections': sections})

# 섹션 상세 페이지
def detail_page(request, id):
    section = get_object_or_404(Section, id=id)
    section.views += 1  # 조회수 증가
    section.save()  # 변경사항 저장
    return render(request, 'detail.html', {'section': section})

# 데이터 저장용 (실제로는 DB를 사용해야 함)
@csrf_protect
def save_section(request):
    if request.method == 'POST':
        try:
            # JSON 데이터로 섹션 정보 가져오기
            import json
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            categories = data.get('categories')

            # 섹션 저장
            section = Section(title=title, author=author, categories=categories)
            section.save()

            # 성공 메시지 반환
            return JsonResponse({'message': 'Section saved successfully!'}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

# 섹션 목록 가져오기
def get_sections(request):
    sections = Section.objects.all()  # 실제 데이터베이스에서 섹션 가져오기
    sections_data = [{'id': section.id, 'title': section.title} for section in sections]
    return JsonResponse({'sections': sections_data})

# 홈 페이지 뷰
def home(request):
    return render(request, 'cosmicflow.html')  # 템플릿을 템플릿 폴더에서 자동으로 찾음

def section_list(request):
    sections = Section.objects.all()  # 데이터베이스에서 모든 섹션을 가져옴
    return render(request, 'sections.html', {'sections': sections})

# 섹션 저장하는 뷰
def save_section(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        Section.objects.create(title=title, author=author)  # 새로운 섹션 생성
        return redirect('section_list')  # 섹션 리스트 페이지로 리디렉션
    return HttpResponse("Invalid Request", status=400)

def category_detail_view(request, category_name):
    sections = Section.objects.filter(categories__contains=[category_name])  # 해당 카테고리에 맞는 섹션들 필터링
    return render(request, 'category.html', {'sections': sections, 'category_name': category_name})

def category_view(request):
    categories = [
        'Physics', 'Chemistry', 'Biology', 'Astronomy', 'Earth Science', 
        'Environmental Science', 'Engineering', 'Medicine', 'Computer Science', 'Psychology'
    ]
    return render(request, 'category_list.html', {'categories': categories})


def example(request):
    return render(request, 'example.html')

def qa(request):
    return render(request, 'qa.html')