import enum_e_ride_property_type_pb2 as _enum_e_ride_property_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeOnRideParam(_message.Message):
    __slots__ = ("ride_type", "ride_id")
    RIDE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RIDE_ID_FIELD_NUMBER: _ClassVar[int]
    ride_type: _enum_e_ride_property_type_pb2.ERidePropertyType
    ride_id: int
    def __init__(self, ride_type: _Optional[_Union[_enum_e_ride_property_type_pb2.ERidePropertyType, str]] = ..., ride_id: _Optional[int] = ...) -> None: ...
