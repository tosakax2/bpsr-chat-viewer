from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SystemType_Null: _ClassVar[SystemType]
    SystemType_Android: _ClassVar[SystemType]
    SystemType_Ios: _ClassVar[SystemType]
    SystemType_Web: _ClassVar[SystemType]
    SystemType_Linux: _ClassVar[SystemType]
    SystemType_Windows: _ClassVar[SystemType]
    SystemType_HarmonyOS: _ClassVar[SystemType]
SystemType_Null: SystemType
SystemType_Android: SystemType
SystemType_Ios: SystemType
SystemType_Web: SystemType
SystemType_Linux: SystemType
SystemType_Windows: SystemType
SystemType_HarmonyOS: SystemType
