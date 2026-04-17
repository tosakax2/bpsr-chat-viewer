import stru_picture_info_pb2 as _stru_picture_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvatarInfo(_message.Message):
    __slots__ = ("avatar_id", "profile", "half_body", "business_card_style_id", "avatar_frame_id")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    HALF_BODY_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_CARD_STYLE_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    profile: _stru_picture_info_pb2.PictureInfo
    half_body: _stru_picture_info_pb2.PictureInfo
    business_card_style_id: int
    avatar_frame_id: int
    def __init__(self, avatar_id: _Optional[int] = ..., profile: _Optional[_Union[_stru_picture_info_pb2.PictureInfo, _Mapping]] = ..., half_body: _Optional[_Union[_stru_picture_info_pb2.PictureInfo, _Mapping]] = ..., business_card_style_id: _Optional[int] = ..., avatar_frame_id: _Optional[int] = ...) -> None: ...
