import enum_e_ride_property_type_pb2 as _enum_e_ride_property_type_pb2
import stru_ride_data_pb2 as _stru_ride_data_pb2
import stru_ride_skin_container_pb2 as _stru_ride_skin_container_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RideList(_message.Message):
    __slots__ = ("rides", "type", "skin_data")
    class RidesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_ride_data_pb2.RideData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_ride_data_pb2.RideData, _Mapping]] = ...) -> None: ...
    class SkinDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_ride_skin_container_pb2.RideSkinContainer
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_ride_skin_container_pb2.RideSkinContainer, _Mapping]] = ...) -> None: ...
    RIDES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIN_DATA_FIELD_NUMBER: _ClassVar[int]
    rides: _containers.MessageMap[int, _stru_ride_data_pb2.RideData]
    type: _enum_e_ride_property_type_pb2.ERidePropertyType
    skin_data: _containers.MessageMap[int, _stru_ride_skin_container_pb2.RideSkinContainer]
    def __init__(self, rides: _Optional[_Mapping[int, _stru_ride_data_pb2.RideData]] = ..., type: _Optional[_Union[_enum_e_ride_property_type_pb2.ERidePropertyType, str]] = ..., skin_data: _Optional[_Mapping[int, _stru_ride_skin_container_pb2.RideSkinContainer]] = ...) -> None: ...
