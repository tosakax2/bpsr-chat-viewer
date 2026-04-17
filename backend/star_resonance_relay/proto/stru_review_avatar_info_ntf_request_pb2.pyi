import stru_avatar_info_pb2 as _stru_avatar_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReviewAvatarInfoNtfRequest(_message.Message):
    __slots__ = ("avatar_info",)
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    def __init__(self, avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ...) -> None: ...
