### urls.py (в testapp)
from django.urls import path
from .views import test_view, results_view, admin_answers_view
urlpatterns = [
    path('test/', test_view, name='test'),
    path('results/', results_view, name='results'),
    path('admin-answers/', admin_answers_view, name='admin_answers'),
]
