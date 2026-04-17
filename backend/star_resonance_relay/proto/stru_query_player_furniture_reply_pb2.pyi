import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_homeland_player_warehouse_info_pb2 as _stru_homeland_player_warehouse_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryPlayerFurnitureReply(_message.Message):
    __slots__ = ("furniture_warehouse", "err_code")
    FURNITURE_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    furniture_warehouse: _stru_homeland_player_warehouse_info_pb2.HomelandPlayerWarehouseInfo
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, furniture_warehouse: _Optional[_Union[_stru_homeland_player_warehouse_info_pb2.HomelandPlayerWarehouseInfo, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
