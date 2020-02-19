from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.BookViewSet)
# router.register(r'authors', views.AuthorViewSet)
# router.register(r'publishers', views.PublisherViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]