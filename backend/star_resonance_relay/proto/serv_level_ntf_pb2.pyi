from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LevelNtf(_message.Message):
    __slots__ = ()
    class DisplayBossUI(_message.Message):
        __slots__ = ("is_enter", "boss_uuid")
        IS_ENTER_FIELD_NUMBER: _ClassVar[int]
        BOSS_UUID_FIELD_NUMBER: _ClassVar[int]
        is_enter: bool
        boss_uuid: int
        def __init__(self, is_enter: bool = ..., boss_uuid: _Optional[int] = ...) -> None: ...
    class DisplayBossOutOverdriveUI(_message.Message):
        __slots__ = ("is_break", "is_weak")
        IS_BREAK_FIELD_NUMBER: _ClassVar[int]
        IS_WEAK_FIELD_NUMBER: _ClassVar[int]
        is_break: bool
        is_weak: bool
        def __init__(self, is_break: bool = ..., is_weak: bool = ...) -> None: ...
    def __init__(self) -> None: ...
