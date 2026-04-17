import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_pay_reply_pb2 as _stru_pay_reply_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityActionReply(_message.Message):
    __slots__ = ("pay_reply", "err_code")
    PAY_REPLY_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    pay_reply: _stru_pay_reply_pb2.PayReply
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, pay_reply: _Optional[_Union[_stru_pay_reply_pb2.PayReply, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
