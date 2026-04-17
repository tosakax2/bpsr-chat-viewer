from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotGetProceedAwardInfo(_message.Message):
    __slots__ = ("award_id_times",)
    class AwardIdTimesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AWARD_ID_TIMES_FIELD_NUMBER: _ClassVar[int]
    award_id_times: _containers.ScalarMap[int, int]
    def __init__(self, award_id_times: _Optional[_Mapping[int, int]] = ...) -> None: ...
