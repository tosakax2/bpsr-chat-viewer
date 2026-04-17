from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UploadFaceSuccessRequest(_message.Message):
    __slots__ = ("face_cos_url",)
    FACE_COS_URL_FIELD_NUMBER: _ClassVar[int]
    face_cos_url: str
    def __init__(self, face_cos_url: _Optional[str] = ...) -> None: ...
