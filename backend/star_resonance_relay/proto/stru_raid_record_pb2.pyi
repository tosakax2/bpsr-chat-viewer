import stru_boss_progress_pb2 as _stru_boss_progress_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RaidRecord(_message.Message):
    __slots__ = ("boss_progress",)
    class BossProgressEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_boss_progress_pb2.BossProgress
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_boss_progress_pb2.BossProgress, _Mapping]] = ...) -> None: ...
    BOSS_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    boss_progress: _containers.MessageMap[int, _stru_boss_progress_pb2.BossProgress]
    def __init__(self, boss_progress: _Optional[_Mapping[int, _stru_boss_progress_pb2.BossProgress]] = ...) -> None: ...
