from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BackflowOnlineData(_message.Message):
    __slots__ = ("login_time_stamp", "logout_time_stamp", "add_up_online_time")
    LOGIN_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    ADD_UP_ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    login_time_stamp: int
    logout_time_stamp: int
    add_up_online_time: int
    def __init__(self, login_time_stamp: _Optional[int] = ..., logout_time_stamp: _Optional[int] = ..., add_up_online_time: _Optional[int] = ...) -> None: ...
