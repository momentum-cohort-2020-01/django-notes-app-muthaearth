from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('notes/new/', views.notes_new, name='notes_new'),
    path('notes/<int:pk>', views.notes_detail, name='notes_detail'),
    path('notes/edit/', views.notes_new, name='notes_edit'),
    path('notes/delete/', views.notes_delete, name='notes_delete'),
    path('admin/', admin.site.urls),
]
