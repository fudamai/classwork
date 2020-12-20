from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blogs', views.BlogsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'zones', views.ZonesViewSet)
router.register(r'comments', views.CommentsViewSet)

# The API URLs are determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]