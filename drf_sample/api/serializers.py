from rest_framework import serializers
from app.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        # 新規フィールドをメソッドの戻り値で作るフィールド追加
        is_staff = serializers.SerializerMethodField()

        model = Post
        fields = ('id', 'title', 'content', 'user', 'like', 'created_at')

    def is_staff(self):
        return True if self.user=="administrator" else False


class PostListSerializer(serializers.ListSerializer):

    child = PostSerializer()
