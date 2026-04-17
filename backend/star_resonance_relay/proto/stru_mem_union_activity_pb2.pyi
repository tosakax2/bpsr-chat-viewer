import stru_not_claimed_reward_pb2 as _stru_not_claimed_reward_pb2
import stru_union_activity_target_pb2 as _stru_union_activity_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemUnionActivity(_message.Message):
    __slots__ = ("last_refresh_time", "personal_targets", "received_point_award_ids", "no_claimed_active_awards", "next_refresh_time")
    class PersonalTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_activity_target_pb2.UnionActivityTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_activity_target_pb2.UnionActivityTarget, _Mapping]] = ...) -> None: ...
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_TARGETS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_POINT_AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    NO_CLAIMED_ACTIVE_AWARDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    last_refresh_time: int
    personal_targets: _containers.MessageMap[int, _stru_union_activity_target_pb2.UnionActivityTarget]
    received_point_award_ids: _containers.RepeatedScalarFieldContainer[int]
    no_claimed_active_awards: _containers.RepeatedCompositeFieldContainer[_stru_not_claimed_reward_pb2.NotClaimedReward]
    next_refresh_time: int
    def __init__(self, last_refresh_time: _Optional[int] = ..., personal_targets: _Optional[_Mapping[int, _stru_union_activity_target_pb2.UnionActivityTarget]] = ..., received_point_award_ids: _Optional[_Iterable[int]] = ..., no_claimed_active_awards: _Optional[_Iterable[_Union[_stru_not_claimed_reward_pb2.NotClaimedReward, _Mapping]]] = ..., next_refresh_time: _Optional[int] = ...) -> None: ...
