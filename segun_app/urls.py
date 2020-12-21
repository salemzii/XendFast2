from django.urls import path
from . import views
from .views import verification, createKycinfo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.landing_page, name='home'),
    path('send_money/', views.transaction, name='send-money'),
    path('charge/', views.charge, name='charge'),
    path('k_check/', views.check_verified, name='check'),
    path('kyc_success/', views.kyc_succ, name='kyc-success'),
    path('success/<str:args>', views.successmsg, name='success'), #<str:args>
    path('register/', views.register, name='sign-up'),
    path('email_verify/', views.email_success, name='e-success'),
    path('verify_mail/', views.verify_mail, name='verify'),
    path('activate/<uidb64>/<token>', verification.as_view(), name='activate'),
    path('uploadKyc/<int:user_id>', createKycinfo.as_view(), name='uploadKyc'),
    path('kycmsg/', views.kyc_msg, name='kyc-msg'),
    path('ViewKyc/<int:user_id>', views.kyc_detail, name='viewKyc')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)