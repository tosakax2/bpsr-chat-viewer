from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FashionBenefitCollectionHistory(_message.Message):
    __slots__ = ("fashion_id", "time", "type", "parameter")
    FASHION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    fashion_id: int
    time: int
    type: int
    parameter: int
    def __init__(self, fashion_id: _Optional[int] = ..., time: _Optional[int] = ..., type: _Optional[int] = ..., parameter: _Optional[int] = ...) -> None: ...
