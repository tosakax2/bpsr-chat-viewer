from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MailImportance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MailImportanceNormal: _ClassVar[MailImportance]
    MailImportanceImportant: _ClassVar[MailImportance]
MailImportanceNormal: MailImportance
MailImportanceImportant: MailImportance
