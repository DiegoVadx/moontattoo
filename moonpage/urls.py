from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .settings import base
# el as es un alias , eso es todo ;)
from apps.home import views as home
from apps.gallery import views as gallery


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home.Home.as_view(),
        name='home'),
    # voila
    url(r'^galeria/', gallery.Gallery.as_view(),
        name='vertical')

] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

