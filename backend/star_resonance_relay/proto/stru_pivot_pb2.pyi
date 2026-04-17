import stru_pivot_info_pb2 as _stru_pivot_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pivot(_message.Message):
    __slots__ = ("pivots", "map_pivots")
    class PivotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_pivot_info_pb2.PivotInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_pivot_info_pb2.PivotInfo, _Mapping]] = ...) -> None: ...
    class MapPivotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_pivot_info_pb2.PivotInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_pivot_info_pb2.PivotInfo, _Mapping]] = ...) -> None: ...
    PIVOTS_FIELD_NUMBER: _ClassVar[int]
    MAP_PIVOTS_FIELD_NUMBER: _ClassVar[int]
    pivots: _containers.MessageMap[int, _stru_pivot_info_pb2.PivotInfo]
    map_pivots: _containers.MessageMap[int, _stru_pivot_info_pb2.PivotInfo]
    def __init__(self, pivots: _Optional[_Mapping[int, _stru_pivot_info_pb2.PivotInfo]] = ..., map_pivots: _Optional[_Mapping[int, _stru_pivot_info_pb2.PivotInfo]] = ...) -> None: ...
