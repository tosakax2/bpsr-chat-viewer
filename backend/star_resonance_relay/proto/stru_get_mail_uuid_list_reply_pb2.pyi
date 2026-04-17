import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailUuidListReply(_message.Message):
    __slots__ = ("mail_uuid_list", "err_code")
    MAIL_UUID_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mail_uuid_list: _containers.RepeatedScalarFieldContainer[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mail_uuid_list: _Optional[_Iterable[int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
