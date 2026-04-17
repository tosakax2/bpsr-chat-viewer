import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_mail_base_pb2 as _stru_mail_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailInfoReply(_message.Message):
    __slots__ = ("mail", "mails", "err_code")
    MAIL_FIELD_NUMBER: _ClassVar[int]
    MAILS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mail: _stru_mail_base_pb2.MailBase
    mails: _containers.RepeatedCompositeFieldContainer[_stru_mail_base_pb2.MailBase]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mail: _Optional[_Union[_stru_mail_base_pb2.MailBase, _Mapping]] = ..., mails: _Optional[_Iterable[_Union[_stru_mail_base_pb2.MailBase, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
