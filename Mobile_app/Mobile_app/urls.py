"""
URL configuration for Mobile_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from visits.views import WorkerViewSet, StoreViewSet, VisitViewSet

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'visits', VisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('workers/', WorkerViewSet.as_view({'get': 'list'})),
    path('workers/<int:pk>/', WorkerViewSet.as_view({'get': 'etrieve'})),
    path('workers/create/', WorkerViewSet.as_view({'post': 'create'})),
    path('workers/<int:pk>/update/', WorkerViewSet.as_view({'put': 'update'})),
    path('workers/<int:pk>/delete/', WorkerViewSet.as_view({'delete': 'destroy'})),
]
