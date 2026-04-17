from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdIpImage(_message.Message):
    __slots__ = ("image_type", "review_type", "cos_url", "dns_url")
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    COS_URL_FIELD_NUMBER: _ClassVar[int]
    DNS_URL_FIELD_NUMBER: _ClassVar[int]
    image_type: int
    review_type: int
    cos_url: str
    dns_url: str
    def __init__(self, image_type: _Optional[int] = ..., review_type: _Optional[int] = ..., cos_url: _Optional[str] = ..., dns_url: _Optional[str] = ...) -> None: ...
