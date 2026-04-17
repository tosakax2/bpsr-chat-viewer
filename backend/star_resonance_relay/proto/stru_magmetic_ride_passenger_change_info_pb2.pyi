import stru_passenger_change_param_pb2 as _stru_passenger_change_param_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagneticRidePassengerChangeInfo(_message.Message):
    __slots__ = ("PassengerChangeList",)
    PASSENGERCHANGELIST_FIELD_NUMBER: _ClassVar[int]
    PassengerChangeList: _containers.RepeatedCompositeFieldContainer[_stru_passenger_change_param_pb2.PassengerChangeParam]
    def __init__(self, PassengerChangeList: _Optional[_Iterable[_Union[_stru_passenger_change_param_pb2.PassengerChangeParam, _Mapping]]] = ...) -> None: ...
