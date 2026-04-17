import stru_fashion_benefit_collection_history_pb2 as _stru_fashion_benefit_collection_history_pb2
import stru_fashion_benefit_task_info_pb2 as _stru_fashion_benefit_task_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FashionBenefit(_message.Message):
    __slots__ = ("last_reward_id", "level", "points_task", "points_cycle", "points_collection", "task_list", "collection_history", "next_refresh_time", "max_points", "last_add_time", "cur_day_max_points", "expire_cycle", "last_level", "firt_expire_time", "last_reward_ids")
    class TaskListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fashion_benefit_task_info_pb2.FashionBenefitTaskInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fashion_benefit_task_info_pb2.FashionBenefitTaskInfo, _Mapping]] = ...) -> None: ...
    LAST_REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POINTS_TASK_FIELD_NUMBER: _ClassVar[int]
    POINTS_CYCLE_FIELD_NUMBER: _ClassVar[int]
    POINTS_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    LAST_ADD_TIME_FIELD_NUMBER: _ClassVar[int]
    CUR_DAY_MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_CYCLE_FIELD_NUMBER: _ClassVar[int]
    LAST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FIRT_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_REWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    last_reward_id: int
    level: int
    points_task: int
    points_cycle: int
    points_collection: int
    task_list: _containers.MessageMap[int, _stru_fashion_benefit_task_info_pb2.FashionBenefitTaskInfo]
    collection_history: _containers.RepeatedCompositeFieldContainer[_stru_fashion_benefit_collection_history_pb2.FashionBenefitCollectionHistory]
    next_refresh_time: int
    max_points: int
    last_add_time: int
    cur_day_max_points: int
    expire_cycle: int
    last_level: int
    firt_expire_time: int
    last_reward_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, last_reward_id: _Optional[int] = ..., level: _Optional[int] = ..., points_task: _Optional[int] = ..., points_cycle: _Optional[int] = ..., points_collection: _Optional[int] = ..., task_list: _Optional[_Mapping[int, _stru_fashion_benefit_task_info_pb2.FashionBenefitTaskInfo]] = ..., collection_history: _Optional[_Iterable[_Union[_stru_fashion_benefit_collection_history_pb2.FashionBenefitCollectionHistory, _Mapping]]] = ..., next_refresh_time: _Optional[int] = ..., max_points: _Optional[int] = ..., last_add_time: _Optional[int] = ..., cur_day_max_points: _Optional[int] = ..., expire_cycle: _Optional[int] = ..., last_level: _Optional[int] = ..., firt_expire_time: _Optional[int] = ..., last_reward_ids: _Optional[_Iterable[int]] = ...) -> None: ...
