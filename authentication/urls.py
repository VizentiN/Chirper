from django.urls import path
from .views import signup, login_request, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
]