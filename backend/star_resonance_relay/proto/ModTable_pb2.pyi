import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModTableBase(_message.Message):
    __slots__ = ("id", "mod_pic", "mod_lvl", "effect_type", "effect_config", "effect_parameter", "tag_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOD_PIC_FIELD_NUMBER: _ClassVar[int]
    MOD_LVL_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    mod_pic: str
    mod_lvl: int
    effect_type: int
    effect_config: int
    effect_parameter: _table_basic_pb2.int_array
    tag_id: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., mod_pic: _Optional[str] = ..., mod_lvl: _Optional[int] = ..., effect_type: _Optional[int] = ..., effect_config: _Optional[int] = ..., effect_parameter: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., tag_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class ModTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModTableBase]] = ...) -> None: ...
