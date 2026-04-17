import stru_picture_verify_pb2 as _stru_picture_verify_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PictureInfo(_message.Message):
    __slots__ = ("url", "verify")
    URL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_FIELD_NUMBER: _ClassVar[int]
    url: str
    verify: _stru_picture_verify_pb2.PictureVerify
    def __init__(self, url: _Optional[str] = ..., verify: _Optional[_Union[_stru_picture_verify_pb2.PictureVerify, _Mapping]] = ...) -> None: ...
