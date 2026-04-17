import stru_equip_attr_set_pb2 as _stru_equip_attr_set_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipAttr(_message.Message):
    __slots__ = ("base_attrs", "perfection_value", "recast_count", "total_recast_count", "basic_attr", "advance_attr", "recast_attr", "perfection_level", "rare_quality_attr", "max_perfection_value", "equip_attr_set", "break_through_time")
    class BaseAttrsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class BasicAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AdvanceAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RecastAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RareQualityAttrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_ATTRS_FIELD_NUMBER: _ClassVar[int]
    PERFECTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    RECAST_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECAST_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASIC_ATTR_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_ATTR_FIELD_NUMBER: _ClassVar[int]
    RECAST_ATTR_FIELD_NUMBER: _ClassVar[int]
    PERFECTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RARE_QUALITY_ATTR_FIELD_NUMBER: _ClassVar[int]
    MAX_PERFECTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ATTR_SET_FIELD_NUMBER: _ClassVar[int]
    BREAK_THROUGH_TIME_FIELD_NUMBER: _ClassVar[int]
    base_attrs: _containers.ScalarMap[int, int]
    perfection_value: int
    recast_count: int
    total_recast_count: int
    basic_attr: _containers.ScalarMap[int, int]
    advance_attr: _containers.ScalarMap[int, int]
    recast_attr: _containers.ScalarMap[int, int]
    perfection_level: int
    rare_quality_attr: _containers.ScalarMap[int, int]
    max_perfection_value: int
    equip_attr_set: _stru_equip_attr_set_pb2.EquipAttrSet
    break_through_time: int
    def __init__(self, base_attrs: _Optional[_Mapping[int, int]] = ..., perfection_value: _Optional[int] = ..., recast_count: _Optional[int] = ..., total_recast_count: _Optional[int] = ..., basic_attr: _Optional[_Mapping[int, int]] = ..., advance_attr: _Optional[_Mapping[int, int]] = ..., recast_attr: _Optional[_Mapping[int, int]] = ..., perfection_level: _Optional[int] = ..., rare_quality_attr: _Optional[_Mapping[int, int]] = ..., max_perfection_value: _Optional[int] = ..., equip_attr_set: _Optional[_Union[_stru_equip_attr_set_pb2.EquipAttrSet, _Mapping]] = ..., break_through_time: _Optional[int] = ...) -> None: ...
