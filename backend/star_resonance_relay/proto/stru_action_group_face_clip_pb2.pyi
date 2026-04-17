from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupFaceClip(_message.Message):
    __slots__ = ("begin_time", "end_time", "fade_time", "face_id")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FADE_TIME_FIELD_NUMBER: _ClassVar[int]
    FACE_ID_FIELD_NUMBER: _ClassVar[int]
    begin_time: float
    end_time: float
    fade_time: float
    face_id: int
    def __init__(self, begin_time: _Optional[float] = ..., end_time: _Optional[float] = ..., fade_time: _Optional[float] = ..., face_id: _Optional[int] = ...) -> None: ...
