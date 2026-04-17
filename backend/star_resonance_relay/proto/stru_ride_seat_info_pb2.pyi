import stru_passenger_info_pb2 as _stru_passenger_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RideSeatInfo(_message.Message):
    __slots__ = ("controller_id", "passengers")
    CONTROLLER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSENGERS_FIELD_NUMBER: _ClassVar[int]
    controller_id: int
    passengers: _containers.RepeatedCompositeFieldContainer[_stru_passenger_info_pb2.PassengerInfo]
    def __init__(self, controller_id: _Optional[int] = ..., passengers: _Optional[_Iterable[_Union[_stru_passenger_info_pb2.PassengerInfo, _Mapping]]] = ...) -> None: ...
