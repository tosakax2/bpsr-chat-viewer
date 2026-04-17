from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReportHome(_message.Message):
    __slots__ = ("home_id",)
    HOME_ID_FIELD_NUMBER: _ClassVar[int]
    home_id: int
    def __init__(self, home_id: _Optional[int] = ...) -> None: ...
