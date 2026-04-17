from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReportPicture(_message.Message):
    __slots__ = ("picture_id", "target_uuid", "union")
    PICTURE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    UNION_FIELD_NUMBER: _ClassVar[int]
    picture_id: str
    target_uuid: int
    union: bool
    def __init__(self, picture_id: _Optional[str] = ..., target_uuid: _Optional[int] = ..., union: bool = ...) -> None: ...
