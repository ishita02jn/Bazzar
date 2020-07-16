from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls'))
    # path('', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
