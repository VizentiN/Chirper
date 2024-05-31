import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    re_path("chirper/(?P<version>(v1|v2))/", include("post.urls")),
]