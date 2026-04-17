import stru_mark_info_pb2 as _stru_mark_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkData(_message.Message):
    __slots__ = ("id", "mark_info_map", "mark_uuid")
    class MarkInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mark_info_pb2.MarkInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mark_info_pb2.MarkInfo, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MARK_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    MARK_UUID_FIELD_NUMBER: _ClassVar[int]
    id: int
    mark_info_map: _containers.MessageMap[int, _stru_mark_info_pb2.MarkInfo]
    mark_uuid: int
    def __init__(self, id: _Optional[int] = ..., mark_info_map: _Optional[_Mapping[int, _stru_mark_info_pb2.MarkInfo]] = ..., mark_uuid: _Optional[int] = ...) -> None: ...
