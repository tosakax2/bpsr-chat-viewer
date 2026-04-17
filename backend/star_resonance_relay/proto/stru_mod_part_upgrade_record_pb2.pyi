from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModPartUpgradeRecord(_message.Message):
    __slots__ = ("part_id", "is_success")
    PART_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    part_id: int
    is_success: bool
    def __init__(self, part_id: _Optional[int] = ..., is_success: bool = ...) -> None: ...
