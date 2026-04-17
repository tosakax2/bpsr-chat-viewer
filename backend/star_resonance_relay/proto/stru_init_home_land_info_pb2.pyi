import stru_homeland_decoration_info_pb2 as _stru_homeland_decoration_info_pb2
import stru_structure_pb2 as _stru_structure_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitHomeLandInfo(_message.Message):
    __slots__ = ("is_outer", "structures", "decoration_info")
    class StructuresEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_structure_pb2.Structure
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_structure_pb2.Structure, _Mapping]] = ...) -> None: ...
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    STRUCTURES_FIELD_NUMBER: _ClassVar[int]
    DECORATION_INFO_FIELD_NUMBER: _ClassVar[int]
    is_outer: bool
    structures: _containers.MessageMap[int, _stru_structure_pb2.Structure]
    decoration_info: _stru_homeland_decoration_info_pb2.HomelandDecorationInfo
    def __init__(self, is_outer: bool = ..., structures: _Optional[_Mapping[int, _stru_structure_pb2.Structure]] = ..., decoration_info: _Optional[_Union[_stru_homeland_decoration_info_pb2.HomelandDecorationInfo, _Mapping]] = ...) -> None: ...
