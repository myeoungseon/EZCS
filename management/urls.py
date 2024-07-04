from django.urls import path 
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.manager_dashboard, name='dashboard'), #대쉬보드 화면
    path('management_detail/<int:id>/', views.manager_detail, name='management_detail'), # 직원상세정보화면
    path('detail/<int:id>/', views.detail, name='detail'), # 직원상세정보화면
    path('management_detail/<int:id>/edit', views.manager_edit, name='edit'), # 직원상세정보수정
    path('allow/', views.allow, name='allow'), #가입승인화면
    path('approve/<int:id>/', views.approve_user, name='approve_user'), #승인해주는 로직
    path('inactive/', views.inactive, name='inactive'), #퇴사 및 휴직 관리 화면
    # path('search/', views.search, name='search'), #검색 로직
]

