from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetShowHallRequest(_message.Message):
    __slots__ = ("is_show", "is_server_set")
    IS_SHOW_FIELD_NUMBER: _ClassVar[int]
    IS_SERVER_SET_FIELD_NUMBER: _ClassVar[int]
    is_show: bool
    is_server_set: bool
    def __init__(self, is_show: bool = ..., is_server_set: bool = ...) -> None: ...
