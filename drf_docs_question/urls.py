
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from app01.views import WorksMainViewSet

router = DefaultRouter()


router.register('worksmain', WorksMainViewSet, basename = "worksmain")
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title = '金该全景')),
    path('api-auth/', include('rest_framework.urls')),  # drf 认证url
]
