from dj_rql.drf.paginations import RQLContentRangeLimitOffsetPagination

from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet

from cqrs_rql_mongo.models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255, required=True, allow_null=False, allow_blank=False,
    )
    slug = serializers.CharField(
        max_length=255, required=True, allow_null=False, allow_blank=False,
    )


class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = PostSerializer
    pagination_class = RQLContentRangeLimitOffsetPagination
    queryset = Post.objects.all()
