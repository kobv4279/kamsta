#url여결하기
#urls.py

from django.urls import path
from .views import PhotoUpdate, PhotoDelete, PhotoCreate, PhotoDetail, PhotoList

app_name = "photo"
urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PhotoDelete.as_view(), name='detail'),
    #PhotoDetail의 as_view()로 가지고 와서 detail path에 연결

    path("", PhotoList.as_view(), name='index'),  #as_view()를 해줘야 제네릭view가 생성성
]


#photo의 네임은 따로 주소 연결 안하고 바로 주소지로 들어왔을때 보이게
#index연결


#메인화면에서 img가 보이도록 하기 위해서
#static  url을 못불러오기 때문에 이런 urls패턴을 설정해줬다

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)