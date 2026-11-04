
from src.local_stream import LocalStream
from src.stream_producer import produce_events
from src.stream_consumer import consume_events


def test_producer_consumer_integration():
    stream = LocalStream()

    produce_events(stream, number_of_events=3)

    assert stream.size() == 3

    consume_events(stream, max_events=3)

    assert stream.size() == 0

def test_producer_generates_unique_event_ids():
    stream = LocalStream()

    produce_events(stream, number_of_events=5)

    event_ids = []

    while stream.size() > 0:
        event = stream.get_event()
        event_ids.append(event["event_id"])

    assert len(event_ids) == 5
    assert len(set(event_ids)) == 5
