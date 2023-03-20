"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from BlogEconomico.views import (index, BlogList, BlogDetail, BlogUpdate, BlogDelete, BlogCreate,
                                 BlogSearch, Login, SignUp, Logout, BlogMineList
                                 )

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('blog/list', BlogList.as_view(), name="blog-list"),
    path('blog/detail/<pk>', BlogDetail.as_view(), name="blog-detail"),
    path('blog/update/<pk>', BlogUpdate.as_view(), name="blog-update"),
    path('blog/delete/<pk>', BlogDelete.as_view(), name="blog-delete"),
    path('blog/create', BlogCreate.as_view(), name="blog-create"),
    path('blog/search', BlogSearch.as_view(), name="blog-search"),
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('blog/list/mine', BlogMineList.as_view(), name="blog-mine"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
