from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CharStatisticsData(_message.Message):
    __slots__ = ("login_days", "last_login_time")
    LOGIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    login_days: int
    last_login_time: int
    def __init__(self, login_days: _Optional[int] = ..., last_login_time: _Optional[int] = ...) -> None: ...
