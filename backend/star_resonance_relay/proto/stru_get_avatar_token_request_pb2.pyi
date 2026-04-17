import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
import stru_picture_verify_pb2 as _stru_picture_verify_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvatarTokenRequest(_message.Message):
    __slots__ = ("verify_info", "picture_type", "picture_id", "picture_name")
    VERIFY_INFO_FIELD_NUMBER: _ClassVar[int]
    PICTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_ID_FIELD_NUMBER: _ClassVar[int]
    PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    verify_info: _stru_picture_verify_pb2.PictureVerify
    picture_type: _enum_e_picture_type_pb2.EPictureType
    picture_id: int
    picture_name: str
    def __init__(self, verify_info: _Optional[_Union[_stru_picture_verify_pb2.PictureVerify, _Mapping]] = ..., picture_type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., picture_id: _Optional[int] = ..., picture_name: _Optional[str] = ...) -> None: ...
