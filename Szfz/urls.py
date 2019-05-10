"""Szfz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from sz_app import views
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    # url('^sz_app/', include('sz_app.urls')),    # 将sz_app/开头的url分配到sz_app.urls
    url(r'^index/$', views.index, name="home"),  # 应用 <form action={% url "home" %}>
    url(r'^dsri/$', views.dsri),
    url(r'^start/$', views.start),
    url(r'^case/(?P<menu>\w*)', views.case),
    url(r'^city/(?P<menu1>\w*)', views.city),
    url(r'^news/(?P<menu2>\w*)', views.news),
    url(r'^download/$', views.download),
    url(r'^logout/$', views.logout),
]
