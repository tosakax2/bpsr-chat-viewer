import stru_pay_data_pb2 as _stru_pay_data_pb2
import stru_refund_item_info_pb2 as _stru_refund_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayOrderList(_message.Message):
    __slots__ = ("pay_order_list", "pay_refund_list", "first_pay", "order_index_list", "order_index_refund_list")
    class OrderIndexListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class OrderIndexRefundListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_refund_item_info_pb2.RefundItemInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_refund_item_info_pb2.RefundItemInfo, _Mapping]] = ...) -> None: ...
    PAY_ORDER_LIST_FIELD_NUMBER: _ClassVar[int]
    PAY_REFUND_LIST_FIELD_NUMBER: _ClassVar[int]
    FIRST_PAY_FIELD_NUMBER: _ClassVar[int]
    ORDER_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    ORDER_INDEX_REFUND_LIST_FIELD_NUMBER: _ClassVar[int]
    pay_order_list: _containers.RepeatedScalarFieldContainer[str]
    pay_refund_list: _containers.RepeatedScalarFieldContainer[str]
    first_pay: _stru_pay_data_pb2.PayData
    order_index_list: _containers.ScalarMap[int, int]
    order_index_refund_list: _containers.MessageMap[int, _stru_refund_item_info_pb2.RefundItemInfo]
    def __init__(self, pay_order_list: _Optional[_Iterable[str]] = ..., pay_refund_list: _Optional[_Iterable[str]] = ..., first_pay: _Optional[_Union[_stru_pay_data_pb2.PayData, _Mapping]] = ..., order_index_list: _Optional[_Mapping[int, int]] = ..., order_index_refund_list: _Optional[_Mapping[int, _stru_refund_item_info_pb2.RefundItemInfo]] = ...) -> None: ...
