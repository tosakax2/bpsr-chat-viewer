from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SignRewardData(_message.Message):
    __slots__ = ("sign_days", "reward_days")
    SIGN_DAYS_FIELD_NUMBER: _ClassVar[int]
    REWARD_DAYS_FIELD_NUMBER: _ClassVar[int]
    sign_days: _containers.RepeatedScalarFieldContainer[int]
    reward_days: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sign_days: _Optional[_Iterable[int]] = ..., reward_days: _Optional[_Iterable[int]] = ...) -> None: ...
