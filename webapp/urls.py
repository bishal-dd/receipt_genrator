from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('generate_pdf/', views.generate_pdf, name="generate_pdf"),
    path('view_receipts/', views.receipts_view, name="view_receipts"),
    path('trial_period/', views.trial_period, name="trial_period"),
    path('save_receipt/', views.save_receipt, name="save_receipt"),
    path('generate_individual_receipt/<int:id>/',
         views.generate_individual_receipt, name='generate_individual_receipt'),
    path("admin/webapp/user/<int:pk>/version/", views.toggle_user_status, name="version"),
    path('admin/change_mode/<int:user_id>/', views.change_mode, name='change_mode'),

]

# Add this at the end of your urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
