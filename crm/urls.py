from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'crm'


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('common.urls', namespace='common')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^leads/', include('leads.urls', namespace='leads')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^cases/', include('cases.urls', namespace='cases')),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
