import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TmpTokenResult(_message.Message):
    __slots__ = ("tmp_secret_id", "tmp_secret_key", "tmp_token", "expired_time", "region", "bucket", "object_key", "picture_id", "version", "err_code")
    TMP_SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    TMP_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    TMP_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_TIME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    PICTURE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    tmp_secret_id: str
    tmp_secret_key: str
    tmp_token: str
    expired_time: int
    region: str
    bucket: str
    object_key: str
    picture_id: int
    version: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, tmp_secret_id: _Optional[str] = ..., tmp_secret_key: _Optional[str] = ..., tmp_token: _Optional[str] = ..., expired_time: _Optional[int] = ..., region: _Optional[str] = ..., bucket: _Optional[str] = ..., object_key: _Optional[str] = ..., picture_id: _Optional[int] = ..., version: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
