import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemFunctionTableBase(_message.Message):
    __slots__ = ("id", "name", "type", "parameter", "button", "use_limit", "reconfirm", "target", "auto_apply", "use_cd", "public_cd", "effect", "sound_effect", "can_quick", "item_batch")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    USE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RECONFIRM_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPLY_FIELD_NUMBER: _ClassVar[int]
    USE_CD_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_CD_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    SOUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
    CAN_QUICK_FIELD_NUMBER: _ClassVar[int]
    ITEM_BATCH_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: int
    parameter: _table_basic_pb2.string_array
    button: _table_basic_pb2.mlstring
    use_limit: _table_basic_pb2.string_array
    reconfirm: int
    target: int
    auto_apply: int
    use_cd: int
    public_cd: _table_basic_pb2.int_array
    effect: str
    sound_effect: str
    can_quick: int
    item_batch: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[int] = ..., parameter: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., button: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., use_limit: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., reconfirm: _Optional[int] = ..., target: _Optional[int] = ..., auto_apply: _Optional[int] = ..., use_cd: _Optional[int] = ..., public_cd: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., effect: _Optional[str] = ..., sound_effect: _Optional[str] = ..., can_quick: _Optional[int] = ..., item_batch: _Optional[int] = ...) -> None: ...

class ItemFunctionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ItemFunctionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ItemFunctionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ItemFunctionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ItemFunctionTableBase]] = ...) -> None: ...
