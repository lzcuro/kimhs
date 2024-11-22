# from django.shortcuts import render, get_object_or_404
# from main.models import ScienceIssue

# def admin(request):
#     return render(request, 'first/base.html')

from django.shortcuts import render

def main(request):
    return render(request, 'first/base.html')
