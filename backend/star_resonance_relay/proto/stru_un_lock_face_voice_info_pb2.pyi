from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnLockFaceVoiceInfo(_message.Message):
    __slots__ = ("voice_id",)
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    voice_id: int
    def __init__(self, voice_id: _Optional[int] = ...) -> None: ...
