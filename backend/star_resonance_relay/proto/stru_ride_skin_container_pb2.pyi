import stru_ride_skin_data_pb2 as _stru_ride_skin_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RideSkinContainer(_message.Message):
    __slots__ = ("ride_skin_id", "sinks")
    class SinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_ride_skin_data_pb2.RideSkinData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_ride_skin_data_pb2.RideSkinData, _Mapping]] = ...) -> None: ...
    RIDE_SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    SINKS_FIELD_NUMBER: _ClassVar[int]
    ride_skin_id: int
    sinks: _containers.MessageMap[int, _stru_ride_skin_data_pb2.RideSkinData]
    def __init__(self, ride_skin_id: _Optional[int] = ..., sinks: _Optional[_Mapping[int, _stru_ride_skin_data_pb2.RideSkinData]] = ...) -> None: ...
