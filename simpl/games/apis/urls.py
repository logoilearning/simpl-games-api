from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'decisions', views.DecisionViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'periods', views.PeriodViewSet)
router.register(r'phases', views.PhaseViewSet)
router.register(r'results', views.ResultViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'runs', views.RunViewSet)
router.register(r'runusers', views.RunUserViewSet)
router.register(r'scenarios', views.ScenarioViewSet)
router.register(r'worlds', views.WorldViewSet)

urlpatterns = router.urls
