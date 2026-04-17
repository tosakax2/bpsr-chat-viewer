from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EObjStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EObjStateInteractive: _ClassVar[EObjStateEnum]
    EObjStateInvalid: _ClassVar[EObjStateEnum]
    EObjStateDead: _ClassVar[EObjStateEnum]
    EObjStateNotInteractive: _ClassVar[EObjStateEnum]
    EObjStateBattle: _ClassVar[EObjStateEnum]
    EObjStateNotVisible: _ClassVar[EObjStateEnum]
EObjStateInteractive: EObjStateEnum
EObjStateInvalid: EObjStateEnum
EObjStateDead: EObjStateEnum
EObjStateNotInteractive: EObjStateEnum
EObjStateBattle: EObjStateEnum
EObjStateNotVisible: EObjStateEnum
