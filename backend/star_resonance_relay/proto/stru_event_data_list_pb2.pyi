import stru_event_data_pb2 as _stru_event_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventDataList(_message.Message):
    __slots__ = ("Uuid", "Events")
    UUID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    Events: _containers.RepeatedCompositeFieldContainer[_stru_event_data_pb2.EventData]
    def __init__(self, Uuid: _Optional[int] = ..., Events: _Optional[_Iterable[_Union[_stru_event_data_pb2.EventData, _Mapping]]] = ...) -> None: ...
