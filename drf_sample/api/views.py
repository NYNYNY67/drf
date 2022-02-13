from rest_framework import viewsets, generics
from app.models import Post
from .serializers import PostSerializer


# ModelViewSetを継承したビュークラスを定義
# CRUD全部
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 全件読み取り
class PostListAPIView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 作成
class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostSerializer


# 読み取り
class PostRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 更新
class PostUpdateAPIView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 削除
class PostDestroyAPIView(generics.DestroyAPIView):

    queryset = Post.objects.all()
