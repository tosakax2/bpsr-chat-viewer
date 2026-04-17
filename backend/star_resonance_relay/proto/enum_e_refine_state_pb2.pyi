from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERefineState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Null: _ClassVar[ERefineState]
    Unlock: _ClassVar[ERefineState]
    CountDown: _ClassVar[ERefineState]
    Wait: _ClassVar[ERefineState]
    Receive: _ClassVar[ERefineState]
    Add: _ClassVar[ERefineState]
Null: ERefineState
Unlock: ERefineState
CountDown: ERefineState
Wait: ERefineState
Receive: ERefineState
Add: ERefineState
