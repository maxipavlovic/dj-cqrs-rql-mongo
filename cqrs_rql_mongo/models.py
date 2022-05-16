from dj_cqrs.registries import ReplicaRegistry

from django.utils.timezone import now

from django_mongoengine import Document, EmbeddedDocument, fields


class Comment(EmbeddedDocument):
    created_at = fields.DateTimeField(default=now, editable=False)
    author = fields.StringField(verbose_name="Name", max_length=255)
    email = fields.EmailField(verbose_name="Email")
    body = fields.StringField(verbose_name="Comment")


# from cqrs_rql_mongo.models import Post
class Post(Document):
    CQRS_ID = 'event'
    CQRS_NO_DB_OPERATIONS = True

    created_at = fields.DateTimeField(default=now, editable=False)
    title = fields.StringField(max_length=255)
    slug = fields.StringField(max_length=255, primary_key=True)
    comments = fields.ListField(
        fields.EmbeddedDocumentField('Comment'), blank=True,
    )

    @classmethod
    def cqrs_save(cls, master_data, previous_data=None, sync=False):
        return master_data, previous_data, sync


ReplicaRegistry.register_model(Post)
