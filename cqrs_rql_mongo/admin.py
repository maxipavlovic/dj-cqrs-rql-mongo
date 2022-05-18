from django_mongoengine import mongo_admin as admin

from cqrs_rql_mongo.models import Post


@admin.register(Post)
class BlogPostAdmin(admin.DocumentAdmin):
    pass
