from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailInfoRequest(_message.Message):
    __slots__ = ("mail_uuid", "mail_uuid_list")
    MAIL_UUID_FIELD_NUMBER: _ClassVar[int]
    MAIL_UUID_LIST_FIELD_NUMBER: _ClassVar[int]
    mail_uuid: int
    mail_uuid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mail_uuid: _Optional[int] = ..., mail_uuid_list: _Optional[_Iterable[int]] = ...) -> None: ...
