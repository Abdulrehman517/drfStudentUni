from django.template.defaulttags import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import StudentViewSet, UniversityViewSet

app_name = 'app'
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
# schema_view = get_swagger_view(title='Swagger API')
# urlpatterns = [
#     url(r'^docs/', include('rest_framework_swagger.urls')),
# ]


# urlpatterns = [
#     path(r'docs/', include('rest_framework_swagger.urls')),
# ]

urlpatterns = router.urls
