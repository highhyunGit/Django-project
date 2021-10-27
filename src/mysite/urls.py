from django.contrib import admin
#from django.urls import path
from django.urls import path, include
from mysite import views
from mysite.views import *
# from mysite.views import CrawlingForm, dispcrawling

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('photo/', include('photo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('schedulebot/', BotView.as_view(), name='schedulebot'),
    path('core/', include('core.urls')),
    # path('crawlingform/', CrawlingForm.as_view(), name='crawlingform'),
    # path('dispCrawling/', views.dispcrawling, name='dispCrawling'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

