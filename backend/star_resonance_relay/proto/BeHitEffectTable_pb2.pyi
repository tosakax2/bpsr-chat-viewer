import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BeHitEffectTableBase(_message.Message):
    __slots__ = ("id", "weapon_hit_type", "fleshy_type", "effect_array", "frame_ratio")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_HIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLESHY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATIO_FIELD_NUMBER: _ClassVar[int]
    id: int
    weapon_hit_type: int
    fleshy_type: int
    effect_array: _table_basic_pb2.string_array
    frame_ratio: float
    def __init__(self, id: _Optional[int] = ..., weapon_hit_type: _Optional[int] = ..., fleshy_type: _Optional[int] = ..., effect_array: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., frame_ratio: _Optional[float] = ...) -> None: ...

class BeHitEffectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BeHitEffectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BeHitEffectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BeHitEffectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BeHitEffectTableBase]] = ...) -> None: ...
