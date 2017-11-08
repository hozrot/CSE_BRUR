from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
	url(r'^$',views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^carrier/', include('carrier.urls')),
    url(r'^co_curricular/', include('co_curricular.urls')),
    url(r'^seminer/', include('seminer.urls')),
    url(r'^social_work/', include('social_work.urls')),
    url(r'^study/', include('study.urls')),
]
