import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_mail_base_pb2 as _stru_mail_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailListReply(_message.Message):
    __slots__ = ("mail_list", "size", "err_code")
    class MailListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mail_base_pb2.MailBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mail_base_pb2.MailBase, _Mapping]] = ...) -> None: ...
    MAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mail_list: _containers.MessageMap[int, _stru_mail_base_pb2.MailBase]
    size: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mail_list: _Optional[_Mapping[int, _stru_mail_base_pb2.MailBase]] = ..., size: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
