from django.conf.urls import url, include
from django.contrib import admin

from . import views
from blog import views as blogViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^about/$',views.about),
    url(r'^blog/', include('blog.urls'))

]
