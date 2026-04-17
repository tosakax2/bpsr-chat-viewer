import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionEffectLibTableBase(_message.Message):
    __slots__ = ("id", "effect_lib_id", "effect_type", "effect_config", "value_range", "random_range")
    ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_FIELD_NUMBER: _ClassVar[int]
    RANDOM_RANGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    effect_lib_id: int
    effect_type: int
    effect_config: int
    value_range: _table_basic_pb2.int_table
    random_range: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., effect_lib_id: _Optional[int] = ..., effect_type: _Optional[int] = ..., effect_config: _Optional[int] = ..., value_range: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., random_range: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ProfessionEffectLibTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfessionEffectLibTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfessionEffectLibTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfessionEffectLibTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfessionEffectLibTableBase]] = ...) -> None: ...
