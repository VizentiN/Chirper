import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    re_path("chirper/(?P<version>(v1|v2))/", include("post.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]