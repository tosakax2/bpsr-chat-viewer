import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_warehouse_info_pb2 as _stru_warehouse_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReBeInitiateWarehouseReply(_message.Message):
    __slots__ = ("warehouse", "err_code")
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    warehouse: _stru_warehouse_info_pb2.WarehouseInfo
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, warehouse: _Optional[_Union[_stru_warehouse_info_pb2.WarehouseInfo, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
