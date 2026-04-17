from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionTableBase(_message.Message):
    __slots__ = ("id", "action_effect", "is_blend", "is_upper", "look_at_body_weight", "unlock_item", "is_follow")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_EFFECT_FIELD_NUMBER: _ClassVar[int]
    IS_BLEND_FIELD_NUMBER: _ClassVar[int]
    IS_UPPER_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_BODY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_ITEM_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    id: int
    action_effect: str
    is_blend: bool
    is_upper: bool
    look_at_body_weight: float
    unlock_item: int
    is_follow: bool
    def __init__(self, id: _Optional[int] = ..., action_effect: _Optional[str] = ..., is_blend: bool = ..., is_upper: bool = ..., look_at_body_weight: _Optional[float] = ..., unlock_item: _Optional[int] = ..., is_follow: bool = ...) -> None: ...

class ActionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ActionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ActionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ActionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ActionTableBase]] = ...) -> None: ...
