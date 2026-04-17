from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileInfo(_message.Message):
    __slots__ = ("profile_id", "profile_url", "half_body_url")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
    HALF_BODY_URL_FIELD_NUMBER: _ClassVar[int]
    profile_id: int
    profile_url: str
    half_body_url: str
    def __init__(self, profile_id: _Optional[int] = ..., profile_url: _Optional[str] = ..., half_body_url: _Optional[str] = ...) -> None: ...
