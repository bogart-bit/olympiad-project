from django.contrib import admin
from django.urls import path
from tasks import views as tasks_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks_views.index, name='home'),
    path('tasks/', tasks_views.tasks_list, name='tasks_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)