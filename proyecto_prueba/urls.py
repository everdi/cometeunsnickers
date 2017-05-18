from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'app_prueba.views.home_v', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
