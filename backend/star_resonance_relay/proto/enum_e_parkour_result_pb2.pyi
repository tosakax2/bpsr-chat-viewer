from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EParkourResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EParkourResult_None: _ClassVar[EParkourResult]
    EParkourResult_Success: _ClassVar[EParkourResult]
    EParkourResult_Fail: _ClassVar[EParkourResult]
EParkourResult_None: EParkourResult
EParkourResult_Success: EParkourResult
EParkourResult_Fail: EParkourResult
