import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_face_upload_data_pb2 as _stru_face_upload_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFaceUploadDataReply(_message.Message):
    __slots__ = ("face_cos_data_list", "err_code")
    FACE_COS_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    face_cos_data_list: _containers.RepeatedCompositeFieldContainer[_stru_face_upload_data_pb2.FaceUploadData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, face_cos_data_list: _Optional[_Iterable[_Union[_stru_face_upload_data_pb2.FaceUploadData, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
