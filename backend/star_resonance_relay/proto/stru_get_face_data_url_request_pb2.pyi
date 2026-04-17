import stru_face_upload_data_pb2 as _stru_face_upload_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFaceDataUrlRequest(_message.Message):
    __slots__ = ("face_data",)
    FACE_DATA_FIELD_NUMBER: _ClassVar[int]
    face_data: _stru_face_upload_data_pb2.FaceUploadData
    def __init__(self, face_data: _Optional[_Union[_stru_face_upload_data_pb2.FaceUploadData, _Mapping]] = ...) -> None: ...
