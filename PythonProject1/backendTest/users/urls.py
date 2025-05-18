# urls.py
from django.urls import path, include
from .views import register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('testapp/', include(('testapp.urls', 'testapp'), namespace='testapp')),
]
