from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns += router.urls