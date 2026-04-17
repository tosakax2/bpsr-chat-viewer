import stru_map_attr_value_pb2 as _stru_map_attr_value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapAttr(_message.Message):
    __slots__ = ("IsClear", "Id", "Attrs")
    ISCLEAR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    IsClear: bool
    Id: int
    Attrs: _containers.RepeatedCompositeFieldContainer[_stru_map_attr_value_pb2.MapAttrValue]
    def __init__(self, IsClear: bool = ..., Id: _Optional[int] = ..., Attrs: _Optional[_Iterable[_Union[_stru_map_attr_value_pb2.MapAttrValue, _Mapping]]] = ...) -> None: ...
