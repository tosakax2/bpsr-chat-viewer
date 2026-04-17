import stru_first_pay_info_pb2 as _stru_first_pay_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayData(_message.Message):
    __slots__ = ("pay_data",)
    class PayDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_first_pay_info_pb2.FirstPayInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_first_pay_info_pb2.FirstPayInfo, _Mapping]] = ...) -> None: ...
    PAY_DATA_FIELD_NUMBER: _ClassVar[int]
    pay_data: _containers.MessageMap[int, _stru_first_pay_info_pb2.FirstPayInfo]
    def __init__(self, pay_data: _Optional[_Mapping[int, _stru_first_pay_info_pb2.FirstPayInfo]] = ...) -> None: ...
