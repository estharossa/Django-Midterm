from rest_framework import routers
from store.views import *

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='book')
router.register('journals', JournalViewSet, basename='journal')

urlpatterns = router.urls
