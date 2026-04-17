from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPictureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENormalPicture: _ClassVar[EPictureType]
    ECameraOriginal: _ClassVar[EPictureType]
    ECameraRender: _ClassVar[EPictureType]
    ECameraThumbnail: _ClassVar[EPictureType]
    EProfileSnapShot: _ClassVar[EPictureType]
    EProfileHalfBody: _ClassVar[EPictureType]
ENormalPicture: EPictureType
ECameraOriginal: EPictureType
ECameraRender: EPictureType
ECameraThumbnail: EPictureType
EProfileSnapShot: EPictureType
EProfileHalfBody: EPictureType
