from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FightPointSubData(_message.Message):
    __slots__ = ("function_type", "root_function_type", "point")
    FUNCTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_FUNCTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    function_type: int
    root_function_type: int
    point: int
    def __init__(self, function_type: _Optional[int] = ..., root_function_type: _Optional[int] = ..., point: _Optional[int] = ...) -> None: ...
