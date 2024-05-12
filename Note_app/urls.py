from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.registration_page, name='registration'),
    path('', views.login_page, name='login'),
    path('posts/<int:id>/', views.posts_page, name='posts'),
    path('add_note/<int:id>/', views.add_note, name='add_note'),
    path('general/<int:id>/', views.general_page, name='general'),

    
    path('delete/<int:id>/', views.note_delete, name='delete'),
    path('update/<int:pk>', views.note_update, name='update')
]
