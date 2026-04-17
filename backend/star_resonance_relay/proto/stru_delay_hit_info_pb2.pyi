import stru_delay_hit_target_info_pb2 as _stru_delay_hit_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DelayHitInfo(_message.Message):
    __slots__ = ("effect_id", "buff_uuid", "event_id", "play_time", "target_infos")
    EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_UUID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAY_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    effect_id: int
    buff_uuid: int
    event_id: int
    play_time: float
    target_infos: _containers.RepeatedCompositeFieldContainer[_stru_delay_hit_target_info_pb2.DelayHitTargetInfo]
    def __init__(self, effect_id: _Optional[int] = ..., buff_uuid: _Optional[int] = ..., event_id: _Optional[int] = ..., play_time: _Optional[float] = ..., target_infos: _Optional[_Iterable[_Union[_stru_delay_hit_target_info_pb2.DelayHitTargetInfo, _Mapping]]] = ...) -> None: ...
