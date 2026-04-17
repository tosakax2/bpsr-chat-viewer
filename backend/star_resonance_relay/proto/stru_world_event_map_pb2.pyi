import stru_world_event_data_pb2 as _stru_world_event_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldEventMap(_message.Message):
    __slots__ = ("event_map", "accept_count", "last_update_time", "refresh_time")
    class EventMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_world_event_data_pb2.worldEventData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_world_event_data_pb2.worldEventData, _Mapping]] = ...) -> None: ...
    EVENT_MAP_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    event_map: _containers.MessageMap[int, _stru_world_event_data_pb2.worldEventData]
    accept_count: int
    last_update_time: int
    refresh_time: int
    def __init__(self, event_map: _Optional[_Mapping[int, _stru_world_event_data_pb2.worldEventData]] = ..., accept_count: _Optional[int] = ..., last_update_time: _Optional[int] = ..., refresh_time: _Optional[int] = ...) -> None: ...
