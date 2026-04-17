import stru_attr_pb2 as _stru_attr_pb2
import stru_map_attr_pb2 as _stru_map_attr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttrCollection(_message.Message):
    __slots__ = ("Uuid", "Attrs", "MapAttrs")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    MAPATTRS_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    Attrs: _containers.RepeatedCompositeFieldContainer[_stru_attr_pb2.Attr]
    MapAttrs: _containers.RepeatedCompositeFieldContainer[_stru_map_attr_pb2.MapAttr]
    def __init__(self, Uuid: _Optional[int] = ..., Attrs: _Optional[_Iterable[_Union[_stru_attr_pb2.Attr, _Mapping]]] = ..., MapAttrs: _Optional[_Iterable[_Union[_stru_map_attr_pb2.MapAttr, _Mapping]]] = ...) -> None: ...
