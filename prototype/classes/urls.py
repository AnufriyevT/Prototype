from rest_framework import routers

from .views import ProjectViewSet

router = routers.SimpleRouter()

router.register(r'project', ProjectViewSet)

urlpatterns = []
urlpatterns += router.urls
