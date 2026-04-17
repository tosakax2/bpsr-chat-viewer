import stru_device_info_pb2 as _stru_device_info_pb2
import stru_face_data_db_pb2 as _stru_face_data_db_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCharRequest(_message.Message):
    __slots__ = ("token", "name", "gender", "v_body_size", "face_data", "device_info", "init_profession_id", "area_id")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    V_BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    FACE_DATA_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    INIT_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    name: str
    gender: int
    v_body_size: int
    face_data: _stru_face_data_db_pb2.FaceDataDb
    device_info: _stru_device_info_pb2.DeviceInfo
    init_profession_id: int
    area_id: int
    def __init__(self, token: _Optional[str] = ..., name: _Optional[str] = ..., gender: _Optional[int] = ..., v_body_size: _Optional[int] = ..., face_data: _Optional[_Union[_stru_face_data_db_pb2.FaceDataDb, _Mapping]] = ..., device_info: _Optional[_Union[_stru_device_info_pb2.DeviceInfo, _Mapping]] = ..., init_profession_id: _Optional[int] = ..., area_id: _Optional[int] = ...) -> None: ...
