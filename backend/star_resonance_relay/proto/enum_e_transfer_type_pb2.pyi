from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TransferTypeNotSetCamera: _ClassVar[ETransferType]
    TransferTypeNotSetPosition: _ClassVar[ETransferType]
    TransferTypeLoadingBlack: _ClassVar[ETransferType]
    TransferTypeLoadingRipple: _ClassVar[ETransferType]
    TransferTypeEffect: _ClassVar[ETransferType]
    TransferTypePassLine: _ClassVar[ETransferType]
    TransferTypeLoadingWhite: _ClassVar[ETransferType]
    TransferTypeLoadingNoEffect: _ClassVar[ETransferType]
TransferTypeNotSetCamera: ETransferType
TransferTypeNotSetPosition: ETransferType
TransferTypeLoadingBlack: ETransferType
TransferTypeLoadingRipple: ETransferType
TransferTypeEffect: ETransferType
TransferTypePassLine: ETransferType
TransferTypeLoadingWhite: ETransferType
TransferTypeLoadingNoEffect: ETransferType
