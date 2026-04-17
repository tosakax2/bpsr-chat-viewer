import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_text_check_item_result_pb2 as _stru_text_check_item_result_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextCheckDataResult(_message.Message):
    __slots__ = ("err_code", "err_msg", "item_results")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    ITEM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    err_msg: str
    item_results: _containers.RepeatedCompositeFieldContainer[_stru_text_check_item_result_pb2.TextCheckItemResult]
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., err_msg: _Optional[str] = ..., item_results: _Optional[_Iterable[_Union[_stru_text_check_item_result_pb2.TextCheckItemResult, _Mapping]]] = ...) -> None: ...
