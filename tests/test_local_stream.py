from src.local_stream import LocalStream


def test_put_and_get_event():
    stream = LocalStream()

    event = {"event_id": "test-001", "total_amount": 1500}

    stream.put_event(event)

    assert stream.size() == 1
    assert stream.get_event() == event
    assert stream.size() == 0


def test_multiple_events():
    stream = LocalStream()

    event1 = {"event_id": "test-001"}
    event2 = {"event_id": "test-002"}

    stream.put_event(event1)
    stream.put_event(event2)

    assert stream.size() == 2
    assert stream.get_event() == event1
    assert stream.get_event() == event2