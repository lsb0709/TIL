from secrets import choice
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    menus = ['삼겹살', '치킨', '낙곱새', '라면', '짜장면', '족발', '초밥']
    images = {
        '삼겹살': "https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg",
        '치킨': "https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg",
        '낙곱새': "https://image.wingeat.com/item/templates/6a72b4e2a847450fb57628709513456f-w970.jpg",
        '라면': "https://cdnweb01.wikitree.co.kr/webdata/editor/202011/20/img_20201120153506_39ceb616.webp",
        '짜장면': "https://folkency.nfm.go.kr/upload/img/20190305/20190305123024_t_.jpg",
        '족발': "https://static.hubzum.zumst.com/hubzum/2019/07/26/11/8291a05e16b14e9b91eedc7a4375c934_780x585.jpg",
        '초밥': "https://gurunavi.com/ko/japanfoodie/article/sushi/img/sushi_01.jpg"
    }
    
    menu = random.choice(menus)

    context = {
        "menu": menu,
        "img": images[menu]
    }
    return render(request, 'index.html', context)

def lotto(request):
    
    return render(request, "lotto.html")