from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, TeamViewSet, PlayerViewSet, CompetitionViewSet, ParticipationViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)  # 注册 Profile API 路由
router.register(r'teams', TeamViewSet)         # 注册 Team API 路由
router.register(r'players', PlayerViewSet)     # 注册 Player API 路由
router.register(r'Competition', CompetitionViewSet)     # 注册 Competition API 路由
router.register(r'Participation', ParticipationViewSet)     # 注册 Participation API 路由

urlpatterns = [
    path('', include(router.urls)),  # 将路由器的 URL 包含进项目 URL 中
]
