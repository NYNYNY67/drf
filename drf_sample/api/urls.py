from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet

# Router(URLの自動登録機能を備えたインスタンス)を作成し、/posts系のAPIを一気に作成
router = routers.DefaultRouter()
router.register('posts', PostViewSet)

# RouterのルートURLのみいつものurlpatternで宣言
urlpatterns = [
    path('', include(router.urls))
]
