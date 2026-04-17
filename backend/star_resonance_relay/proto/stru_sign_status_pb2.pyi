from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SignStatus(_message.Message):
    __slots__ = ("is_signed", "is_rewarded", "is_supplement", "sign_time", "reward_time")
    IS_SIGNED_FIELD_NUMBER: _ClassVar[int]
    IS_REWARDED_FIELD_NUMBER: _ClassVar[int]
    IS_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    SIGN_TIME_FIELD_NUMBER: _ClassVar[int]
    REWARD_TIME_FIELD_NUMBER: _ClassVar[int]
    is_signed: bool
    is_rewarded: bool
    is_supplement: bool
    sign_time: int
    reward_time: int
    def __init__(self, is_signed: bool = ..., is_rewarded: bool = ..., is_supplement: bool = ..., sign_time: _Optional[int] = ..., reward_time: _Optional[int] = ...) -> None: ...
