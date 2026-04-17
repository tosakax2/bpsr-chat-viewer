import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayReply(_message.Message):
    __slots__ = ("server_id", "product_id", "extra_data", "err_code")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    product_id: int
    extra_data: str
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, server_id: _Optional[str] = ..., product_id: _Optional[int] = ..., extra_data: _Optional[str] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
