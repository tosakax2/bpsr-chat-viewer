import stru_mark_data_pb2 as _stru_mark_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapData(_message.Message):
    __slots__ = ("mark_data_map", "ares_map", "mark_uuid")
    class MarkDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mark_data_pb2.MarkData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mark_data_pb2.MarkData, _Mapping]] = ...) -> None: ...
    class AresMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    MARK_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    ARES_MAP_FIELD_NUMBER: _ClassVar[int]
    MARK_UUID_FIELD_NUMBER: _ClassVar[int]
    mark_data_map: _containers.MessageMap[int, _stru_mark_data_pb2.MarkData]
    ares_map: _containers.ScalarMap[int, bool]
    mark_uuid: int
    def __init__(self, mark_data_map: _Optional[_Mapping[int, _stru_mark_data_pb2.MarkData]] = ..., ares_map: _Optional[_Mapping[int, bool]] = ..., mark_uuid: _Optional[int] = ...) -> None: ...
