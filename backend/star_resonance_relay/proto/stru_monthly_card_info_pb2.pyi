import enum_e_receive_reward_status_pb2 as _enum_e_receive_reward_status_pb2
import stru_month_card_item_pb2 as _stru_month_card_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonthlyCardInfo(_message.Message):
    __slots__ = ("limit_award_status", "award_status", "month_card_item", "begin_time", "end_time")
    LIMIT_AWARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    AWARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    MONTH_CARD_ITEM_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    limit_award_status: _enum_e_receive_reward_status_pb2.EReceiveRewardStatus
    award_status: _enum_e_receive_reward_status_pb2.EReceiveRewardStatus
    month_card_item: _stru_month_card_item_pb2.MonthCardItem
    begin_time: int
    end_time: int
    def __init__(self, limit_award_status: _Optional[_Union[_enum_e_receive_reward_status_pb2.EReceiveRewardStatus, str]] = ..., award_status: _Optional[_Union[_enum_e_receive_reward_status_pb2.EReceiveRewardStatus, str]] = ..., month_card_item: _Optional[_Union[_stru_month_card_item_pb2.MonthCardItem, _Mapping]] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
