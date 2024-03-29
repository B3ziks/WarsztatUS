"""warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.contrib.auth import views as auth_views
from warsztat.views import home, signup, Register, account, pchange, contact, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path("employee/", include("employee.urls")),
    path("pricing/",include("pricing.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", Register, name="signup"),
    path("account/", account, name="account"),
    path("pchange/", pchange, name="pchange"),
    path("contact/", contact, name="contact"), 
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)