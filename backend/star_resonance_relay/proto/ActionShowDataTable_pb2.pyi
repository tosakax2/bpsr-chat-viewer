from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionShowDataTableBase(_message.Message):
    __slots__ = ("id", "start", "duration", "end", "is_attacker", "state_id", "group_id", "action_name", "res_path", "action_type", "is_loop", "is_upend", "enhance_damping")
    ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    RES_PATH_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    IS_UPEND_FIELD_NUMBER: _ClassVar[int]
    ENHANCE_DAMPING_FIELD_NUMBER: _ClassVar[int]
    id: int
    start: float
    duration: float
    end: float
    is_attacker: bool
    state_id: int
    group_id: int
    action_name: str
    res_path: str
    action_type: int
    is_loop: bool
    is_upend: bool
    enhance_damping: bool
    def __init__(self, id: _Optional[int] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., end: _Optional[float] = ..., is_attacker: bool = ..., state_id: _Optional[int] = ..., group_id: _Optional[int] = ..., action_name: _Optional[str] = ..., res_path: _Optional[str] = ..., action_type: _Optional[int] = ..., is_loop: bool = ..., is_upend: bool = ..., enhance_damping: bool = ...) -> None: ...

class ActionShowDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ActionShowDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ActionShowDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ActionShowDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ActionShowDataTableBase]] = ...) -> None: ...
