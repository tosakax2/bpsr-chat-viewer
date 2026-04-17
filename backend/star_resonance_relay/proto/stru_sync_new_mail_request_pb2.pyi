import enum_mail_importance_pb2 as _enum_mail_importance_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncNewMailRequest(_message.Message):
    __slots__ = ("mail_uuid", "importance")
    MAIL_UUID_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    mail_uuid: int
    importance: _enum_mail_importance_pb2.MailImportance
    def __init__(self, mail_uuid: _Optional[int] = ..., importance: _Optional[_Union[_enum_mail_importance_pb2.MailImportance, str]] = ...) -> None: ...
