import stru_home_land_item_instance_pb2 as _stru_home_land_item_instance_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandPlayerWarehouseInfo(_message.Message):
    __slots__ = ("furniture_items",)
    class FurnitureItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_item_instance_pb2.HomeLandItemInstance
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ...) -> None: ...
    FURNITURE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    furniture_items: _containers.MessageMap[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]
    def __init__(self, furniture_items: _Optional[_Mapping[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]] = ...) -> None: ...
