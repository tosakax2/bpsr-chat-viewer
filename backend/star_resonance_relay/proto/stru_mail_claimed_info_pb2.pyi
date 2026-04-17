from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailClaimedInfo(_message.Message):
    __slots__ = ("attachment_mail_list", "claimed_mails")
    class ClaimedMailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ATTACHMENT_MAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_MAILS_FIELD_NUMBER: _ClassVar[int]
    attachment_mail_list: _containers.RepeatedScalarFieldContainer[int]
    claimed_mails: _containers.ScalarMap[int, int]
    def __init__(self, attachment_mail_list: _Optional[_Iterable[int]] = ..., claimed_mails: _Optional[_Mapping[int, int]] = ...) -> None: ...
