import enum_e_use_slot_type_pb2 as _enum_e_use_slot_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UseSlotRequest(_message.Message):
    __slots__ = ("slot_id", "use_type", "extra_data")
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    USE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    slot_id: int
    use_type: _enum_e_use_slot_type_pb2.EUseSlotType
    extra_data: bytes
    def __init__(self, slot_id: _Optional[int] = ..., use_type: _Optional[_Union[_enum_e_use_slot_type_pb2.EUseSlotType, str]] = ..., extra_data: _Optional[bytes] = ...) -> None: ...
