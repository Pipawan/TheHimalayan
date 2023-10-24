"""
URL configuration for TheHimalayan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from portals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('home/', views.home_view),
    path('about/', views.About),
    path('breaking_news/', views.Breaking_news),
    path('contact/', views.contact_view),
    path('politics/', views.political_news_view),
    path('science/', views.science_news_view),
    path('sports/', views.sports_news_view),
    path('international/',views.international_list_view),
    path('logout/', views.logout_view),
    path('signup/', views.Signup_view),
     path('thanks/',views.thanks_view),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail_view,name='post_detail'),
    path('accounts/',include('django.contrib.auth.urls')),
]