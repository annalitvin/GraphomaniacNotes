from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_notes/', views.NoteFormView.as_view(), name='note_input'),
    path('notes/', views.NotesListView.as_view(), name='notes_list'),
    path('success/', views.success, name='success')
]
