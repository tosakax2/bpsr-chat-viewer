import stru_function_time_data_pb2 as _stru_function_time_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameFunctionData(_message.Message):
    __slots__ = ("id", "state", "product_id", "function_times")
    class FunctionTimesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_function_time_data_pb2.FunctionTimeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_function_time_data_pb2.FunctionTimeData, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_TIMES_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: bool
    product_id: int
    function_times: _containers.MessageMap[int, _stru_function_time_data_pb2.FunctionTimeData]
    def __init__(self, id: _Optional[int] = ..., state: bool = ..., product_id: _Optional[int] = ..., function_times: _Optional[_Mapping[int, _stru_function_time_data_pb2.FunctionTimeData]] = ...) -> None: ...
