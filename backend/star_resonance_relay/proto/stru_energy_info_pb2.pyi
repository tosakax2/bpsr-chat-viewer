import stru_energy_item_info_pb2 as _stru_energy_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnergyInfo(_message.Message):
    __slots__ = ("energy_value", "unlock_num", "energy_item_info")
    class EnergyItemInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_energy_item_info_pb2.EnergyItemInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_energy_item_info_pb2.EnergyItemInfo, _Mapping]] = ...) -> None: ...
    ENERGY_VALUE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_NUM_FIELD_NUMBER: _ClassVar[int]
    ENERGY_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    energy_value: int
    unlock_num: int
    energy_item_info: _containers.MessageMap[int, _stru_energy_item_info_pb2.EnergyItemInfo]
    def __init__(self, energy_value: _Optional[int] = ..., unlock_num: _Optional[int] = ..., energy_item_info: _Optional[_Mapping[int, _stru_energy_item_info_pb2.EnergyItemInfo]] = ...) -> None: ...
