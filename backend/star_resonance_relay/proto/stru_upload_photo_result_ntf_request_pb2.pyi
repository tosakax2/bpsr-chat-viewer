import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_platform_func_type_pb2 as _enum_e_platform_func_type_pb2
import stru_photo_graph_show_pb2 as _stru_photo_graph_show_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadPhotoResultNtfRequest(_message.Message):
    __slots__ = ("err_code", "photo_info", "func_type")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_INFO_FIELD_NUMBER: _ClassVar[int]
    FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    photo_info: _stru_photo_graph_show_pb2.PhotoGraphShow
    func_type: _enum_e_platform_func_type_pb2.EPlatformFuncType
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., photo_info: _Optional[_Union[_stru_photo_graph_show_pb2.PhotoGraphShow, _Mapping]] = ..., func_type: _Optional[_Union[_enum_e_platform_func_type_pb2.EPlatformFuncType, str]] = ...) -> None: ...
