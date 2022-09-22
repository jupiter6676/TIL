from django.shortcuts import render
import random

# Create your views here.
def getDinner(request):
    randNum = random.randrange(0, 5)    # 0 ~ 4 사이 랜덤 정수

    print(f'###########################################{randNum}###########')

    menus = ['삼겹살', '된장찌개', '부대찌개', '회', '치킨',]
    images = [
        'https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg',
        'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201812/26/d6b14e96-2da0-4fb5-86d7-622a1ac79a88.jpg',
        'https://simg.ssgcdn.com/trans.ssg?src=/cmpt/edit/202005/28/102020052810014534459085730018_841.jpg&w=830&t=5088adf635ca30ff21a0ab880d05e8198da5c93e',
        'https://t1.daumcdn.net/cfile/tistory/9979CA3359EEB37627',
        'https://pelicana.co.kr/resources/images/menu/best_menu02_200824.jpg',
    ]

    context = {
        'menu': menus[randNum],
        'image': images[randNum], 
    }

    return render(request, 'today_dinner.html', context)