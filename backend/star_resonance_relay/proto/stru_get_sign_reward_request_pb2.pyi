from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSignRewardRequest(_message.Message):
    __slots__ = ("sign_type", "sign_days")
    SIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIGN_DAYS_FIELD_NUMBER: _ClassVar[int]
    sign_type: int
    sign_days: int
    def __init__(self, sign_type: _Optional[int] = ..., sign_days: _Optional[int] = ...) -> None: ...
