from dj_cqrs.constants import SignalType
from dj_cqrs.controller.producer import produce
from dj_cqrs.dataclasses import TransportPayload


# from cqrs_rql_mongo.cqrs import produce_cqrs; produce_cqrs({'pk': 1})
def produce_cqrs(data):
    return produce(
        TransportPayload(
            SignalType.SAVE,
            'event',
            data,
            data['pk'],
        ),
    )
