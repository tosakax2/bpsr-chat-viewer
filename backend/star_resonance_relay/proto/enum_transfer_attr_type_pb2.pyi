from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TransferAttrType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TransferAttrTypeNull: _ClassVar[TransferAttrType]
    TransferAttrTypeCommonLeave: _ClassVar[TransferAttrType]
    TransferAttrTypeCommonEnter: _ClassVar[TransferAttrType]
    TransferAttrTypePassLineLeave: _ClassVar[TransferAttrType]
    TransferAttrTypePassLineEnter: _ClassVar[TransferAttrType]
TransferAttrTypeNull: TransferAttrType
TransferAttrTypeCommonLeave: TransferAttrType
TransferAttrTypeCommonEnter: TransferAttrType
TransferAttrTypePassLineLeave: TransferAttrType
TransferAttrTypePassLineEnter: TransferAttrType
