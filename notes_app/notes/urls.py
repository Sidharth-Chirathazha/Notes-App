from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.notes_view, name='notes'),
    path('note/<uuid:note_id>/', views.note_detail_view, name='note_detail'),
    path('note/add/', views.add_note_view, name='add_note'),
    path('note/<uuid:note_id>/edit/', views.edit_note_view, name='edit_note'),
    path('note/<uuid:note_id>/delete/', views.delete_note_view, name='delete_note'),
]