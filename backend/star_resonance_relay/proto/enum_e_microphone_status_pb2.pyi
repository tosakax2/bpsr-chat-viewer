from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMicrophoneStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMicrophoneStatusOpened: _ClassVar[EMicrophoneStatus]
    EMicrophoneStatusClosed: _ClassVar[EMicrophoneStatus]
    EMicrophoneStatusOpenSpeaker: _ClassVar[EMicrophoneStatus]
EMicrophoneStatusOpened: EMicrophoneStatus
EMicrophoneStatusClosed: EMicrophoneStatus
EMicrophoneStatusOpenSpeaker: EMicrophoneStatus
