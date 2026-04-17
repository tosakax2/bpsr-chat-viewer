import stru_activity_reward_progress_pb2 as _stru_activity_reward_progress_pb2
import stru_buy_gift_info_pb2 as _stru_buy_gift_info_pb2
import enum_e_activity_obtain_status_pb2 as _enum_e_activity_obtain_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityAward(_message.Message):
    __slots__ = ("award_id", "reward_show_begintime", "reward_show_endtime", "reward_begintime", "reward_endtime", "condition", "item_list", "award_list", "obtain_status", "progress_list", "reward_info")
    class ConditionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class ItemListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_SHOW_BEGINTIME_FIELD_NUMBER: _ClassVar[int]
    REWARD_SHOW_ENDTIME_FIELD_NUMBER: _ClassVar[int]
    REWARD_BEGINTIME_FIELD_NUMBER: _ClassVar[int]
    REWARD_ENDTIME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    AWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    REWARD_INFO_FIELD_NUMBER: _ClassVar[int]
    award_id: int
    reward_show_begintime: int
    reward_show_endtime: int
    reward_begintime: int
    reward_endtime: int
    condition: _containers.ScalarMap[int, str]
    item_list: _containers.ScalarMap[int, int]
    award_list: _containers.RepeatedScalarFieldContainer[int]
    obtain_status: _enum_e_activity_obtain_status_pb2.EActivityObtainStatus
    progress_list: _stru_activity_reward_progress_pb2.ActivityRewardProgress
    reward_info: _stru_buy_gift_info_pb2.BuyGiftInfo
    def __init__(self, award_id: _Optional[int] = ..., reward_show_begintime: _Optional[int] = ..., reward_show_endtime: _Optional[int] = ..., reward_begintime: _Optional[int] = ..., reward_endtime: _Optional[int] = ..., condition: _Optional[_Mapping[int, str]] = ..., item_list: _Optional[_Mapping[int, int]] = ..., award_list: _Optional[_Iterable[int]] = ..., obtain_status: _Optional[_Union[_enum_e_activity_obtain_status_pb2.EActivityObtainStatus, str]] = ..., progress_list: _Optional[_Union[_stru_activity_reward_progress_pb2.ActivityRewardProgress, _Mapping]] = ..., reward_info: _Optional[_Union[_stru_buy_gift_info_pb2.BuyGiftInfo, _Mapping]] = ...) -> None: ...
