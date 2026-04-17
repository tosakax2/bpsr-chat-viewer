import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeLowestPriceReply(_message.Message):
    __slots__ = ("config_id", "lowest_price", "err_code")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    LOWEST_PRICE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    lowest_price: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, config_id: _Optional[int] = ..., lowest_price: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
