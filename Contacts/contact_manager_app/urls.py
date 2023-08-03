from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_contacts, name='contacts_list'),  # Use 'contacts_list' here
    path('add/', views.add_contact, name='add_contact'),
    path('<int:pk>/', views.get_contact, name='get_contact'),  # Correct URL pattern
    path('<int:pk>/update/', views.update_contact, name='update_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
    path('delete_all/', views.delete_all_contacts, name='delete_all_contacts'),
]