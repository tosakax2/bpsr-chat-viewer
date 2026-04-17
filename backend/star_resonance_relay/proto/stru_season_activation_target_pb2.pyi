from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonActivationTarget(_message.Message):
    __slots__ = ("id", "target_type", "target_uuid", "reward_rate", "progress", "completed_times")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    REWARD_RATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TIMES_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_type: int
    target_uuid: int
    reward_rate: int
    progress: int
    completed_times: int
    def __init__(self, id: _Optional[int] = ..., target_type: _Optional[int] = ..., target_uuid: _Optional[int] = ..., reward_rate: _Optional[int] = ..., progress: _Optional[int] = ..., completed_times: _Optional[int] = ...) -> None: ...
