from dj_cqrs.controller import consumer
from dj_cqrs.transport import BaseTransport


class TransportStub(BaseTransport):
    @staticmethod
    def produce(payload):
        return TransportStub.consume(payload)

    @staticmethod
    def consume(payload=None):
        if payload:
            return consumer.consume(payload)
