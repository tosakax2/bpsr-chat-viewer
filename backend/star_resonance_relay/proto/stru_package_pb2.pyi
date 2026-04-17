import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Package(_message.Message):
    __slots__ = ("type", "max_capacity", "item_cd", "items", "public_cd", "change_version")
    class ItemCdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_item_pb2.Item
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_CD_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_CD_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    type: int
    max_capacity: int
    item_cd: _containers.ScalarMap[int, int]
    items: _containers.MessageMap[int, _stru_item_pb2.Item]
    public_cd: int
    change_version: int
    def __init__(self, type: _Optional[int] = ..., max_capacity: _Optional[int] = ..., item_cd: _Optional[_Mapping[int, int]] = ..., items: _Optional[_Mapping[int, _stru_item_pb2.Item]] = ..., public_cd: _Optional[int] = ..., change_version: _Optional[int] = ...) -> None: ...
