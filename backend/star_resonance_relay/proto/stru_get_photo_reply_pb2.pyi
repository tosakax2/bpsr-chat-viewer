import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_photo_graph_show_pb2 as _stru_photo_graph_show_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPhotoReply(_message.Message):
    __slots__ = ("char_id", "photo_id", "photo_graph", "err_code")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_GRAPH_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    photo_id: int
    photo_graph: _stru_photo_graph_show_pb2.PhotoGraphShow
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, char_id: _Optional[int] = ..., photo_id: _Optional[int] = ..., photo_graph: _Optional[_Union[_stru_photo_graph_show_pb2.PhotoGraphShow, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
