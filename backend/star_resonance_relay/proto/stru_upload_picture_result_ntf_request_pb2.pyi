import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
import stru_picture_info_pb2 as _stru_picture_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadPictureResultNtfRequest(_message.Message):
    __slots__ = ("err_code", "picture_type", "picture_info")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_INFO_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    picture_type: _enum_e_picture_type_pb2.EPictureType
    picture_info: _stru_picture_info_pb2.PictureInfo
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., picture_type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., picture_info: _Optional[_Union[_stru_picture_info_pb2.PictureInfo, _Mapping]] = ...) -> None: ...
