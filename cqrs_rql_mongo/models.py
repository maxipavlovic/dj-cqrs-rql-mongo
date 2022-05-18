from dj_cqrs.registries import ReplicaRegistry

from django.utils.timezone import now

from django_mongoengine import Document, fields


# from cqrs_rql_mongo.models import Post
class Post(Document):
    CQRS_ID = 'event'
    CQRS_NO_DB_OPERATIONS = True

    created_at = fields.DateTimeField(default=now, editable=False)
    title = fields.StringField(max_length=255)
    slug = fields.StringField(max_length=255, primary_key=True)

    @classmethod
    def cqrs_save(cls, master_data, previous_data=None, sync=False):
        return master_data, previous_data, sync


ReplicaRegistry.register_model(Post)
