import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_home_land_item_instance_pb2 as _stru_home_land_item_instance_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandFurnitureWarehouseInfoReply(_message.Message):
    __slots__ = ("items", "slots", "item_to_slots", "err_code")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_item_instance_pb2.HomeLandItemInstance
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ...) -> None: ...
    class SlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ItemToSlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    ITEM_TO_SLOTS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.MessageMap[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]
    slots: _containers.ScalarMap[int, int]
    item_to_slots: _containers.ScalarMap[int, int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, items: _Optional[_Mapping[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]] = ..., slots: _Optional[_Mapping[int, int]] = ..., item_to_slots: _Optional[_Mapping[int, int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
