from django.urls import path, include
from api import views as api_views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'apex/filenames', api_views.APEX_FILENAMES, 'APEX_FILENAMES')
router.register(r'apex', api_views.APEX, 'APEX')


urlpatterns = [
    path('', include(router.urls)),
]