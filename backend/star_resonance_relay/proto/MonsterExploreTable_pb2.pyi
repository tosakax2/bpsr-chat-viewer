import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterExploreTableBase(_message.Message):
    __slots__ = ("monster_id", "scene", "sort", "target", "unlock_award", "model_retio", "condition")
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_AWARD_FIELD_NUMBER: _ClassVar[int]
    MODEL_RETIO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    scene: int
    sort: int
    target: _table_basic_pb2.int_table
    unlock_award: int
    model_retio: float
    condition: _table_basic_pb2.mlstring
    def __init__(self, monster_id: _Optional[int] = ..., scene: _Optional[int] = ..., sort: _Optional[int] = ..., target: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock_award: _Optional[int] = ..., model_retio: _Optional[float] = ..., condition: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class MonsterExploreTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MonsterExploreTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MonsterExploreTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MonsterExploreTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MonsterExploreTableBase]] = ...) -> None: ...
