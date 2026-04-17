import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanetMemoryTableBase(_message.Message):
    __slots__ = ("room_id", "dungeon_id", "room_pos", "unlock_room_id", "room_type", "link_model", "affix", "room_name", "gs_limit", "target_monster", "unlock_time", "extra_target")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_POS_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINK_MODEL_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    GS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TARGET_MONSTER_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TARGET_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    dungeon_id: int
    room_pos: _table_basic_pb2.number_array
    unlock_room_id: _table_basic_pb2.int_array
    room_type: int
    link_model: _table_basic_pb2.int_array
    affix: _table_basic_pb2.int_array
    room_name: _table_basic_pb2.mlstring
    gs_limit: int
    target_monster: _table_basic_pb2.int_array
    unlock_time: _table_basic_pb2.int_array
    extra_target: _table_basic_pb2.int_array
    def __init__(self, room_id: _Optional[int] = ..., dungeon_id: _Optional[int] = ..., room_pos: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., unlock_room_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., room_type: _Optional[int] = ..., link_model: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., affix: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., room_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., gs_limit: _Optional[int] = ..., target_monster: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., unlock_time: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., extra_target: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class PlanetMemoryTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PlanetMemoryTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlanetMemoryTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PlanetMemoryTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PlanetMemoryTableBase]] = ...) -> None: ...
