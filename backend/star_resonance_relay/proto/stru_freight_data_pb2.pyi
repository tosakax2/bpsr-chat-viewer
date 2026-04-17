from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FreightData(_message.Message):
    __slots__ = ("refresh_time", "goods_value", "set_off", "can_receive", "up_goods_list", "keep_goods_list", "down_goods_list", "can_reward_time")
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    GOODS_VALUE_FIELD_NUMBER: _ClassVar[int]
    SET_OFF_FIELD_NUMBER: _ClassVar[int]
    CAN_RECEIVE_FIELD_NUMBER: _ClassVar[int]
    UP_GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    KEEP_GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    DOWN_GOODS_LIST_FIELD_NUMBER: _ClassVar[int]
    CAN_REWARD_TIME_FIELD_NUMBER: _ClassVar[int]
    refresh_time: int
    goods_value: int
    set_off: bool
    can_receive: bool
    up_goods_list: _containers.RepeatedScalarFieldContainer[int]
    keep_goods_list: _containers.RepeatedScalarFieldContainer[int]
    down_goods_list: _containers.RepeatedScalarFieldContainer[int]
    can_reward_time: int
    def __init__(self, refresh_time: _Optional[int] = ..., goods_value: _Optional[int] = ..., set_off: bool = ..., can_receive: bool = ..., up_goods_list: _Optional[_Iterable[int]] = ..., keep_goods_list: _Optional[_Iterable[int]] = ..., down_goods_list: _Optional[_Iterable[int]] = ..., can_reward_time: _Optional[int] = ...) -> None: ...
