from rest_framework.routers import SimpleRouter
from blogs.views import BlogViewset

router = SimpleRouter()
router.register('', BlogViewset)

urlpatterns = router.get_urls()
