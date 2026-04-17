import stru_mail_state_info_pb2 as _stru_mail_state_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncMailInfoRequest(_message.Message):
    __slots__ = ("mails",)
    class MailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mail_state_info_pb2.MailStateInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mail_state_info_pb2.MailStateInfo, _Mapping]] = ...) -> None: ...
    MAILS_FIELD_NUMBER: _ClassVar[int]
    mails: _containers.MessageMap[int, _stru_mail_state_info_pb2.MailStateInfo]
    def __init__(self, mails: _Optional[_Mapping[int, _stru_mail_state_info_pb2.MailStateInfo]] = ...) -> None: ...
