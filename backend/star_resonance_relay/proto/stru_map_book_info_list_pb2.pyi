import stru_map_book_info_pb2 as _stru_map_book_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapBookInfoList(_message.Message):
    __slots__ = ("map_book_map",)
    class MapBookMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_map_book_info_pb2.MapBookInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_map_book_info_pb2.MapBookInfo, _Mapping]] = ...) -> None: ...
    MAP_BOOK_MAP_FIELD_NUMBER: _ClassVar[int]
    map_book_map: _containers.MessageMap[int, _stru_map_book_info_pb2.MapBookInfo]
    def __init__(self, map_book_map: _Optional[_Mapping[int, _stru_map_book_info_pb2.MapBookInfo]] = ...) -> None: ...
