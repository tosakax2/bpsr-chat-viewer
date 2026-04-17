import stru_friend_data_pb2 as _stru_friend_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUpdateDataRequest(_message.Message):
    __slots__ = ("operation_map", "sync_data")
    class OperationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OPERATION_MAP_FIELD_NUMBER: _ClassVar[int]
    SYNC_DATA_FIELD_NUMBER: _ClassVar[int]
    operation_map: _containers.ScalarMap[int, int]
    sync_data: _stru_friend_data_pb2.FriendData
    def __init__(self, operation_map: _Optional[_Mapping[int, int]] = ..., sync_data: _Optional[_Union[_stru_friend_data_pb2.FriendData, _Mapping]] = ...) -> None: ...
