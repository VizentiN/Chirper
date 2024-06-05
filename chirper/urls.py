import debug_toolbar
from chirper import views
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from post.views import home

urlpatterns = [
    path('', home, name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('post/', include('post.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]