import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_recommend_play_data_pb2 as _stru_recommend_play_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRecommendPlayDataReply(_message.Message):
    __slots__ = ("recommend_play_data", "err_code")
    class RecommendPlayDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_recommend_play_data_pb2.RecommendPlayData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_recommend_play_data_pb2.RecommendPlayData, _Mapping]] = ...) -> None: ...
    RECOMMEND_PLAY_DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    recommend_play_data: _containers.MessageMap[int, _stru_recommend_play_data_pb2.RecommendPlayData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, recommend_play_data: _Optional[_Mapping[int, _stru_recommend_play_data_pb2.RecommendPlayData]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
