import stru_equip_attr_pb2 as _stru_equip_attr_pb2
import stru_equip_enchant_info_pb2 as _stru_equip_enchant_info_pb2
import stru_equip_info_pb2 as _stru_equip_info_pb2
import stru_equip_suit_info_pb2 as _stru_equip_suit_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipList(_message.Message):
    __slots__ = ("equip_list", "equip_attr", "equip_recast_info", "equip_enchant", "suit_info_dict")
    class EquipListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_equip_info_pb2.EquipInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_equip_info_pb2.EquipInfo, _Mapping]] = ...) -> None: ...
    class EquipRecastInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_equip_attr_pb2.EquipAttr
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_equip_attr_pb2.EquipAttr, _Mapping]] = ...) -> None: ...
    class EquipEnchantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_equip_enchant_info_pb2.EquipEnchantInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_equip_enchant_info_pb2.EquipEnchantInfo, _Mapping]] = ...) -> None: ...
    class SuitInfoDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_equip_suit_info_pb2.EquipSuitInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_equip_suit_info_pb2.EquipSuitInfo, _Mapping]] = ...) -> None: ...
    EQUIP_LIST_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ATTR_FIELD_NUMBER: _ClassVar[int]
    EQUIP_RECAST_INFO_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ENCHANT_FIELD_NUMBER: _ClassVar[int]
    SUIT_INFO_DICT_FIELD_NUMBER: _ClassVar[int]
    equip_list: _containers.MessageMap[int, _stru_equip_info_pb2.EquipInfo]
    equip_attr: _stru_equip_attr_pb2.EquipAttr
    equip_recast_info: _containers.MessageMap[int, _stru_equip_attr_pb2.EquipAttr]
    equip_enchant: _containers.MessageMap[int, _stru_equip_enchant_info_pb2.EquipEnchantInfo]
    suit_info_dict: _containers.MessageMap[int, _stru_equip_suit_info_pb2.EquipSuitInfo]
    def __init__(self, equip_list: _Optional[_Mapping[int, _stru_equip_info_pb2.EquipInfo]] = ..., equip_attr: _Optional[_Union[_stru_equip_attr_pb2.EquipAttr, _Mapping]] = ..., equip_recast_info: _Optional[_Mapping[int, _stru_equip_attr_pb2.EquipAttr]] = ..., equip_enchant: _Optional[_Mapping[int, _stru_equip_enchant_info_pb2.EquipEnchantInfo]] = ..., suit_info_dict: _Optional[_Mapping[int, _stru_equip_suit_info_pb2.EquipSuitInfo]] = ...) -> None: ...
