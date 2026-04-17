import stru_lucky_value_info_pb2 as _stru_lucky_value_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LuckyValueMgr(_message.Message):
    __slots__ = ("luck_value_info", "init_value")
    class LuckValueInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_lucky_value_info_pb2.LuckyValueInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_lucky_value_info_pb2.LuckyValueInfo, _Mapping]] = ...) -> None: ...
    LUCK_VALUE_INFO_FIELD_NUMBER: _ClassVar[int]
    INIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    luck_value_info: _containers.MessageMap[int, _stru_lucky_value_info_pb2.LuckyValueInfo]
    init_value: bool
    def __init__(self, luck_value_info: _Optional[_Mapping[int, _stru_lucky_value_info_pb2.LuckyValueInfo]] = ..., init_value: bool = ...) -> None: ...
