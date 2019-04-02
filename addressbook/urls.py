from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='addressbooklist_list'),
    path('create_contact/', views.ContactCreate.as_view(), name='addressbooklist_create'),
    path('update_contact/<int:pk>/', views.ContactUpdate.as_view(), name='addressbooklist_update'),
    path('delete_contact/<int:pk>/', views.ContactDelete.as_view(), name='addressbooklist_delete'),
    path('upload-csv/', views.contact_upload, name='contact_upload'),
    path('download-csv/', views.contact_download, name='contact_download'),
]