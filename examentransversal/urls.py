"""
URL configuration for examentransversal project.

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
from django.urls import path, include
from CRUD import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls')),
    path('', views.home, name='home'),
    path('gestionobras/', views.gestionobras, name='gestionobras'),
    path('mision/', views.mision, name='mision'),
    path('galeria<int:obra_id>', views.galeria, name='galeria'),
    path('galeriap/', views.galeriap, name='galeriap'),
    path('galeria1/', views.galeria1, name='galeria1'),
    path('galeria2/', views.galeria2, name='galeria2'),
    path('galeria3/', views.galeria3, name='galeria3'),
    path('galeria4/', views.galeria4, name='galeria4'),
    path('galeria5/', views.galeria5, name='galeria5'),
    path('galeria6/', views.galeria6, name='galeria6'),
    path('galeria7/', views.galeria7, name='galeria7'),
    path('galeria8/', views.galeria8, name='galeria8'),
    path('galeria9/', views.galeria9, name='galeria9'),
    path('formulario/', views.formulario, name='formulario'),
    path('mapa/', views.mapa, name='mapa'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)