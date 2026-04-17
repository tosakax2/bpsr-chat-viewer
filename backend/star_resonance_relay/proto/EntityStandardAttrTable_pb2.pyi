import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityStandardAttrTableBase(_message.Message):
    __slots__ = ("id", "season", "equip_level", "max_hp", "attack", "body_part_max_hp")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_HP_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    BODY_PART_MAX_HP_FIELD_NUMBER: _ClassVar[int]
    id: int
    season: int
    equip_level: int
    max_hp: _table_basic_pb2.int_table
    attack: _table_basic_pb2.int_table
    body_part_max_hp: int
    def __init__(self, id: _Optional[int] = ..., season: _Optional[int] = ..., equip_level: _Optional[int] = ..., max_hp: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., attack: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., body_part_max_hp: _Optional[int] = ...) -> None: ...

class EntityStandardAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EntityStandardAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EntityStandardAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EntityStandardAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EntityStandardAttrTableBase]] = ...) -> None: ...
