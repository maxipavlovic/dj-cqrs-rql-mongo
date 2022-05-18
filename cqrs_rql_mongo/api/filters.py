from dj_rql.filter_cls import RQLFilterClass

from cqrs_rql_mongo.models import Post


class PostFilters(RQLFilterClass):
    MODEL = Post


# from cqrs_rql_mongo.filters import init_filters; init_filters()
def init_filters():
    return PostFilters(Post.objects)
