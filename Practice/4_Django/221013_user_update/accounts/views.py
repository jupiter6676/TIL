from django.shortcuts import render

# Create your views here.
# 회원 목록 조회 페이지
def index(request):
    return render(request, 'accounts/index.html')