from django.urls import path, include
from api import views as api_views
from api import endpoints
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'apex/filenames', api_views.APEX_FILENAMES, 'APEX_FILENAMES_BACKEND')
router.register(r'apex/deployments', api_views.APEX_DEPLOYMENTS, 'APEX_FILENAMES_BACKEND')
router.register(r'apex/crud', api_views.APEX_RAW_DATA_CRUD, 'APEX_RAW_DATA_CRUD_BACKEND')
router.register(r'apex/frontend/decode', endpoints.DECODE_STATUS, 'APEX_DECODE_STATUS_FRONTEND')
router.register(r'apex/frontend/deployments', endpoints.APEX_DEPLOYMENTS, 'APEX_DEPLOYMENTS_FRONTEND')
router.register(r'apex/frontend/users', endpoints.APEX_USERs, 'APEX_USERS_FRONTEND')
router.register(r'apex/frontend/list_users', endpoints.LIST_APEX_USERs, 'LIST_APEX_USERS_FRONTEND')
router.register(r'apex/frontend/rawdata', endpoints.APEX_RAW_DATA_GIVEN_DEPLOYMENT, 'APEX_RAW_DATA_GIVEN_DEPLOYMENT_FRONTEND')
router.register(r'apex/frontend/stats', endpoints.APEX_DEPLOYMENT_STATISTICS, 'APEX_STATS_GIVEN_DEPLOYMENT_FRONTEND')
router.register(r'apex/frontend/deployment_sites', endpoints.APEX_DEPLOYMENT_SITES, 'APEX_DEPLOYMENT_SITES_AND_ASSOCIATED_APEX_MACHINES_FRONTEND')
router.register(r'apex', api_views.APEX, 'APEX_BACKEND')

urlpatterns = [
    path('', include(router.urls)),
]