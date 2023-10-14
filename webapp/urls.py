from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('save_data/', views.save_data, name="save_data")
]

# Add this at the end of your urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
