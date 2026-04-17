from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERecordState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERecordState_None: _ClassVar[ERecordState]
    ERecordState_Perfect: _ClassVar[ERecordState]
    ERecordState_Broken: _ClassVar[ERecordState]
ERecordState_None: ERecordState
ERecordState_Perfect: ERecordState
ERecordState_Broken: ERecordState
