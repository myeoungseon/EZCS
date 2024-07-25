from django.urls import path 
from . import views

app_name = 'education'

urlpatterns = [
    # 롤플레잉=교육 페이지
    path('', views.chat_view, name='chat_view'),

    # 교육 이력 페이지
    path('edu_history/', views.edu_history, name='edu_history'),

    # 교육이력 상세 페이지
    path('edu_details/<int:id>/', views.edu_details, name='edu_details'),

    # 퀴즈 페이지 
    path('quiz/', views.quiz, name='quiz'),

    # 퀴즈 이력 페이지
    path('quiz_history/', views.quiz_history, name='quiz_history'),

    # 퀴즈 이력 상세페이지
    path('quiz_details/<int:log_id>/', views.quiz_details, name='quiz_details'),

    path('del_train_data', views.delete_training_init_data, name='delTrainData'),
]