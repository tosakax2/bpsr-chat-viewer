import stru_game_function_data_pb2 as _stru_game_function_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserActivityRewardInfo(_message.Message):
    __slots__ = ("id", "status", "functions")
    class FunctionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_game_function_data_pb2.GameFunctionData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_game_function_data_pb2.GameFunctionData, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: int
    functions: _containers.MessageMap[int, _stru_game_function_data_pb2.GameFunctionData]
    def __init__(self, id: _Optional[int] = ..., status: _Optional[int] = ..., functions: _Optional[_Mapping[int, _stru_game_function_data_pb2.GameFunctionData]] = ...) -> None: ...
