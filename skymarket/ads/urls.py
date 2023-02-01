from django.urls import  path
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('ads', AdViewSet)

urlpatterns = [
    path("ads/<int:ad_id>/comments/",
         CommentViewSet.as_view({"get": "list", "post": 'create'})),

]

urlpatterns += router.urls
