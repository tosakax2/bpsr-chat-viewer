import stru_backflow_online_data_pb2 as _stru_backflow_online_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewbieBackflowPublicData(_message.Message):
    __slots__ = ("level_award_received", "elective_preference", "online_data", "border_logout_time_stamp")
    LEVEL_AWARD_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    ELECTIVE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    BORDER_LOGOUT_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    level_award_received: bool
    elective_preference: _containers.RepeatedScalarFieldContainer[int]
    online_data: _containers.RepeatedCompositeFieldContainer[_stru_backflow_online_data_pb2.BackflowOnlineData]
    border_logout_time_stamp: int
    def __init__(self, level_award_received: bool = ..., elective_preference: _Optional[_Iterable[int]] = ..., online_data: _Optional[_Iterable[_Union[_stru_backflow_online_data_pb2.BackflowOnlineData, _Mapping]]] = ..., border_logout_time_stamp: _Optional[int] = ...) -> None: ...
