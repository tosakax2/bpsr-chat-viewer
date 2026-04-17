import stru_mod_attr_info_pb2 as _stru_mod_attr_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModAttr(_message.Message):
    __slots__ = ("load_flag", "type", "level", "mod_attr_info")
    LOAD_FLAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MOD_ATTR_INFO_FIELD_NUMBER: _ClassVar[int]
    load_flag: int
    type: int
    level: int
    mod_attr_info: _containers.RepeatedCompositeFieldContainer[_stru_mod_attr_info_pb2.ModAttrInfo]
    def __init__(self, load_flag: _Optional[int] = ..., type: _Optional[int] = ..., level: _Optional[int] = ..., mod_attr_info: _Optional[_Iterable[_Union[_stru_mod_attr_info_pb2.ModAttrInfo, _Mapping]]] = ...) -> None: ...
