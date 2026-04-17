import stru_affix_data_pb2 as _stru_affix_data_pb2
import enum_e_item_bind_flag_pb2 as _enum_e_item_bind_flag_pb2
import stru_equip_attr_pb2 as _stru_equip_attr_pb2
import stru_item_extend_data_pb2 as _stru_item_extend_data_pb2
import stru_mod_attr_pb2 as _stru_mod_attr_pb2
import stru_mod_new_attr_pb2 as _stru_mod_new_attr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("uuid", "config_id", "count", "invalid", "bind_flag", "create_time", "expire_time", "opt_src", "quality", "equip_attr", "mod_attr", "cool_down_expire_time", "mod_new_attr", "affix_data", "extend_attr", "reward_id", "gene_sequence", "gene_source", "locked")
    class ExtendAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_item_extend_data_pb2.ItemExtendData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_item_extend_data_pb2.ItemExtendData, _Mapping]] = ...) -> None: ...
    class GeneSequenceEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    BIND_FLAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    OPT_SRC_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ATTR_FIELD_NUMBER: _ClassVar[int]
    MOD_ATTR_FIELD_NUMBER: _ClassVar[int]
    COOL_DOWN_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    MOD_NEW_ATTR_FIELD_NUMBER: _ClassVar[int]
    AFFIX_DATA_FIELD_NUMBER: _ClassVar[int]
    EXTEND_ATTR_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    GENE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    GENE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    config_id: int
    count: int
    invalid: int
    bind_flag: _enum_e_item_bind_flag_pb2.EItemBindFlag
    create_time: int
    expire_time: int
    opt_src: int
    quality: int
    equip_attr: _stru_equip_attr_pb2.EquipAttr
    mod_attr: _stru_mod_attr_pb2.ModAttr
    cool_down_expire_time: int
    mod_new_attr: _stru_mod_new_attr_pb2.ModNewAttr
    affix_data: _stru_affix_data_pb2.AffixData
    extend_attr: _containers.MessageMap[int, _stru_item_extend_data_pb2.ItemExtendData]
    reward_id: int
    gene_sequence: _containers.ScalarMap[int, int]
    gene_source: int
    locked: bool
    def __init__(self, uuid: _Optional[int] = ..., config_id: _Optional[int] = ..., count: _Optional[int] = ..., invalid: _Optional[int] = ..., bind_flag: _Optional[_Union[_enum_e_item_bind_flag_pb2.EItemBindFlag, str]] = ..., create_time: _Optional[int] = ..., expire_time: _Optional[int] = ..., opt_src: _Optional[int] = ..., quality: _Optional[int] = ..., equip_attr: _Optional[_Union[_stru_equip_attr_pb2.EquipAttr, _Mapping]] = ..., mod_attr: _Optional[_Union[_stru_mod_attr_pb2.ModAttr, _Mapping]] = ..., cool_down_expire_time: _Optional[int] = ..., mod_new_attr: _Optional[_Union[_stru_mod_new_attr_pb2.ModNewAttr, _Mapping]] = ..., affix_data: _Optional[_Union[_stru_affix_data_pb2.AffixData, _Mapping]] = ..., extend_attr: _Optional[_Mapping[int, _stru_item_extend_data_pb2.ItemExtendData]] = ..., reward_id: _Optional[int] = ..., gene_sequence: _Optional[_Mapping[int, int]] = ..., gene_source: _Optional[int] = ..., locked: bool = ...) -> None: ...
