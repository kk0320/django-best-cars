"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include  # include を追加
from pages import views  # 追加: pagesアプリのviewsをインポート

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理者ページ
    path('pages/', include('pages.urls')),  # pagesアプリ
    path('', views.about, name='home'),  # ルートパスをAboutページに設定
]
