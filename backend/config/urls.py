from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(title='AutoParkApi', default_version='v1', description='About AutoParks',
                                           contact=openapi.Contact(email='admin@gmail.com')), public=True,
                              permission_classes=[AllowAny])
urlpatterns = [
    path('api/auth', include('apps.auth.urls')),
    path('api/users', include('apps.users.urls')),
    path('api/meters', include('apps.meter.urls')),
    path('api/readings', include('apps.readings.urls')),
    path('api/advertisement', include('apps.advertisement.urls')),
    path('api/poll', include('apps.poll.urls')),
    path('api/news', include('apps.news.urls')),
    path('api/fault_msg', include('apps.fault_message.urls')),
    path('api/payment', include('apps.payment_for_user.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
