from django.urls import path, re_path, include
from django.shortcuts import redirect
from contact_manager_app.views import get_contacts

urlpatterns = [
    path('', lambda r: redirect('contacts_list'), name='root'),
    path('contacts/', include('contact_manager_app.urls')),
]