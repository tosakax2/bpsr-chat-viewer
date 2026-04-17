import stru_activity_reward_limit_times_pb2 as _stru_activity_reward_limit_times_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyGiftInfo(_message.Message):
    __slots__ = ("pay_product_id", "limit_times")
    PAY_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TIMES_FIELD_NUMBER: _ClassVar[int]
    pay_product_id: int
    limit_times: _containers.RepeatedCompositeFieldContainer[_stru_activity_reward_limit_times_pb2.ActivityRewardLimitTimes]
    def __init__(self, pay_product_id: _Optional[int] = ..., limit_times: _Optional[_Iterable[_Union[_stru_activity_reward_limit_times_pb2.ActivityRewardLimitTimes, _Mapping]]] = ...) -> None: ...
