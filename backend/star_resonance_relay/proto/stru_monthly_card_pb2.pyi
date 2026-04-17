import stru_item_pb2 as _stru_item_pb2
import stru_monthly_card_buy_list_pb2 as _stru_monthly_card_buy_list_pb2
import stru_monthly_card_info_pb2 as _stru_monthly_card_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonthlyCard(_message.Message):
    __slots__ = ("expire_time", "monthly_card_info", "last_award_monthly_card_time", "tips_clicked", "tips_day", "items", "monthly_card_buy_list")
    class MonthlyCardInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_monthly_card_info_pb2.MonthlyCardInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_monthly_card_info_pb2.MonthlyCardInfo, _Mapping]] = ...) -> None: ...
    class MonthlyCardBuyListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_monthly_card_buy_list_pb2.MonthlyCardBuyList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_monthly_card_buy_list_pb2.MonthlyCardBuyList, _Mapping]] = ...) -> None: ...
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CARD_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_AWARD_MONTHLY_CARD_TIME_FIELD_NUMBER: _ClassVar[int]
    TIPS_CLICKED_FIELD_NUMBER: _ClassVar[int]
    TIPS_DAY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CARD_BUY_LIST_FIELD_NUMBER: _ClassVar[int]
    expire_time: int
    monthly_card_info: _containers.MessageMap[int, _stru_monthly_card_info_pb2.MonthlyCardInfo]
    last_award_monthly_card_time: int
    tips_clicked: int
    tips_day: int
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    monthly_card_buy_list: _containers.MessageMap[int, _stru_monthly_card_buy_list_pb2.MonthlyCardBuyList]
    def __init__(self, expire_time: _Optional[int] = ..., monthly_card_info: _Optional[_Mapping[int, _stru_monthly_card_info_pb2.MonthlyCardInfo]] = ..., last_award_monthly_card_time: _Optional[int] = ..., tips_clicked: _Optional[int] = ..., tips_day: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., monthly_card_buy_list: _Optional[_Mapping[int, _stru_monthly_card_buy_list_pb2.MonthlyCardBuyList]] = ...) -> None: ...
