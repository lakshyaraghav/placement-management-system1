

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from tstudentapp import views
from tsmyblog import views
# from tstudentapp.views import GeneratePdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tstudentapp.urls')),
    path('blog/',include('tsmyblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    
    
    # path('pdf/', GeneratePdf.as_view()), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
