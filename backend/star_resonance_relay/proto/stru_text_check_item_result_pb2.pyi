import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextCheckItemResult(_message.Message):
    __slots__ = ("err_code", "err_msg", "item_err_code", "item_err_msg", "context", "request_id", "text_check_result", "filtered_text", "lable", "check_desc")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    ITEM_ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_CHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    FILTERED_TEXT_FIELD_NUMBER: _ClassVar[int]
    LABLE_FIELD_NUMBER: _ClassVar[int]
    CHECK_DESC_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    err_msg: str
    item_err_code: int
    item_err_msg: str
    context: str
    request_id: str
    text_check_result: int
    filtered_text: str
    lable: int
    check_desc: str
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., err_msg: _Optional[str] = ..., item_err_code: _Optional[int] = ..., item_err_msg: _Optional[str] = ..., context: _Optional[str] = ..., request_id: _Optional[str] = ..., text_check_result: _Optional[int] = ..., filtered_text: _Optional[str] = ..., lable: _Optional[int] = ..., check_desc: _Optional[str] = ...) -> None: ...
