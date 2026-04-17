from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EInstructionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    InstructionType_Undefined: _ClassVar[EInstructionType]
    InstructionType_Tips: _ClassVar[EInstructionType]
    InstructionType_Logout: _ClassVar[EInstructionType]
    InstructionType_OpenUrl: _ClassVar[EInstructionType]
    InstructionType_UserDefined: _ClassVar[EInstructionType]
    InstructionType_Stop: _ClassVar[EInstructionType]
    InstructionType_PreLogout: _ClassVar[EInstructionType]
InstructionType_Undefined: EInstructionType
InstructionType_Tips: EInstructionType
InstructionType_Logout: EInstructionType
InstructionType_OpenUrl: EInstructionType
InstructionType_UserDefined: EInstructionType
InstructionType_Stop: EInstructionType
InstructionType_PreLogout: EInstructionType
