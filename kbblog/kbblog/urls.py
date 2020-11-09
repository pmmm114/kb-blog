"""kbblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

from django.contrib import admin
from django.urls import include, path, re_path

from .views import indexView

from django.views.generic import TemplateView

urlpatterns = [
    # social auth url
    path('', include('social_django.urls', namespace='social')),
    # app url
    path('', indexView.as_view(), name='blog_index'),
    path('profiles/', include('profiles.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('service-worker.js', TemplateView.as_view(template_name="common/service-worker.js", content_type="application/javascript"), name='service_worker'),
    # admin url
    path('admin', admin.site.urls),
    re_path(r'^.*$', indexView.as_view(), name='not_url'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
