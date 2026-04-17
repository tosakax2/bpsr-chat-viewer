import enum_e_show_item_type_pb2 as _enum_e_show_item_type_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowItemsInfo(_message.Message):
    __slots__ = ("type", "items")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_show_item_type_pb2.EShowItemType
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    def __init__(self, type: _Optional[_Union[_enum_e_show_item_type_pb2.EShowItemType, str]] = ..., items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ...) -> None: ...
