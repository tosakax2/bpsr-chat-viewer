import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AffixTableBase(_message.Message):
    __slots__ = ("id", "name", "description", "remark", "icon", "effect_type", "target_type", "level", "mutex", "effect", "effect_time", "gs_change")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MUTEX_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TIME_FIELD_NUMBER: _ClassVar[int]
    GS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    description: _table_basic_pb2.mlstring
    remark: str
    icon: str
    effect_type: int
    target_type: int
    level: int
    mutex: _table_basic_pb2.int_array
    effect: _table_basic_pb2.int_table
    effect_time: _table_basic_pb2.number_table
    gs_change: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., remark: _Optional[str] = ..., icon: _Optional[str] = ..., effect_type: _Optional[int] = ..., target_type: _Optional[int] = ..., level: _Optional[int] = ..., mutex: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., effect: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., effect_time: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., gs_change: _Optional[int] = ...) -> None: ...

class AffixTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AffixTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AffixTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AffixTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AffixTableBase]] = ...) -> None: ...
