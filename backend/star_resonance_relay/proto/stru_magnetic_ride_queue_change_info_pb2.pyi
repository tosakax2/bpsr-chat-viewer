import stru_magnetic_ride_path_point_change_info_pb2 as _stru_magnetic_ride_path_point_change_info_pb2
import stru_magmetic_ride_passenger_change_info_pb2 as _stru_magmetic_ride_passenger_change_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagneticRideQueueChangeInfo(_message.Message):
    __slots__ = ("QueueUuid", "PassengerChangeInfo", "PathPointChangeInfo", "IsCircle", "IsRemove", "PathLength")
    QUEUEUUID_FIELD_NUMBER: _ClassVar[int]
    PASSENGERCHANGEINFO_FIELD_NUMBER: _ClassVar[int]
    PATHPOINTCHANGEINFO_FIELD_NUMBER: _ClassVar[int]
    ISCIRCLE_FIELD_NUMBER: _ClassVar[int]
    ISREMOVE_FIELD_NUMBER: _ClassVar[int]
    PATHLENGTH_FIELD_NUMBER: _ClassVar[int]
    QueueUuid: int
    PassengerChangeInfo: _stru_magmetic_ride_passenger_change_info_pb2.MagneticRidePassengerChangeInfo
    PathPointChangeInfo: _stru_magnetic_ride_path_point_change_info_pb2.MagneticRidePathPointChangeInfo
    IsCircle: bool
    IsRemove: bool
    PathLength: float
    def __init__(self, QueueUuid: _Optional[int] = ..., PassengerChangeInfo: _Optional[_Union[_stru_magmetic_ride_passenger_change_info_pb2.MagneticRidePassengerChangeInfo, _Mapping]] = ..., PathPointChangeInfo: _Optional[_Union[_stru_magnetic_ride_path_point_change_info_pb2.MagneticRidePathPointChangeInfo, _Mapping]] = ..., IsCircle: bool = ..., IsRemove: bool = ..., PathLength: _Optional[float] = ...) -> None: ...
