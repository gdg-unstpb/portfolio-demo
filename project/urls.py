from django.urls import include, path

from portfolio import settings
from project import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home_page,name='home'),
    path('project/<int:id>/',views.project_detail,name='project_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)