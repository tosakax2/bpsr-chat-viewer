import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_get_first_pay_info_pb2 as _stru_get_first_pay_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFirstPayReply(_message.Message):
    __slots__ = ("first_pay_info", "ladder_pay_info", "err_code")
    class LadderPayInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_get_first_pay_info_pb2.GetFirstPayInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_get_first_pay_info_pb2.GetFirstPayInfo, _Mapping]] = ...) -> None: ...
    FIRST_PAY_INFO_FIELD_NUMBER: _ClassVar[int]
    LADDER_PAY_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    first_pay_info: _containers.RepeatedScalarFieldContainer[int]
    ladder_pay_info: _containers.MessageMap[int, _stru_get_first_pay_info_pb2.GetFirstPayInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, first_pay_info: _Optional[_Iterable[int]] = ..., ladder_pay_info: _Optional[_Mapping[int, _stru_get_first_pay_info_pb2.GetFirstPayInfo]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
