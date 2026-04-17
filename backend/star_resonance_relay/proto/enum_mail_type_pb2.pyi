from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MailType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MailTypeNull: _ClassVar[MailType]
    MailTypePersonal: _ClassVar[MailType]
    MailTypeWorld: _ClassVar[MailType]
    MailTypeMax: _ClassVar[MailType]
MailTypeNull: MailType
MailTypePersonal: MailType
MailTypeWorld: MailType
MailTypeMax: MailType
