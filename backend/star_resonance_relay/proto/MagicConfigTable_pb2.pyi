from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagicConfigTableBase(_message.Message):
    __slots__ = ("id", "name", "type", "role_id", "weapon_id", "model_type", "be_hit_act")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BE_HIT_ACT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: int
    role_id: int
    weapon_id: int
    model_type: int
    be_hit_act: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[int] = ..., role_id: _Optional[int] = ..., weapon_id: _Optional[int] = ..., model_type: _Optional[int] = ..., be_hit_act: _Optional[str] = ...) -> None: ...

class MagicConfigTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MagicConfigTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MagicConfigTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MagicConfigTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MagicConfigTableBase]] = ...) -> None: ...
