import stru_temp_attr_pb2 as _stru_temp_attr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TempAttrCollection(_message.Message):
    __slots__ = ("Attrs",)
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    Attrs: _containers.RepeatedCompositeFieldContainer[_stru_temp_attr_pb2.TempAttr]
    def __init__(self, Attrs: _Optional[_Iterable[_Union[_stru_temp_attr_pb2.TempAttr, _Mapping]]] = ...) -> None: ...
