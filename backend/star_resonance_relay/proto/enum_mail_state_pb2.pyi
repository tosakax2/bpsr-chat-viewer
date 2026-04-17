from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MailState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MailStateNull: _ClassVar[MailState]
    MailStateSend: _ClassVar[MailState]
    MailStateRead: _ClassVar[MailState]
    MailStateGet: _ClassVar[MailState]
    MailStateDelete: _ClassVar[MailState]
    MailStateHide: _ClassVar[MailState]
MailStateNull: MailState
MailStateSend: MailState
MailStateRead: MailState
MailStateGet: MailState
MailStateDelete: MailState
MailStateHide: MailState
