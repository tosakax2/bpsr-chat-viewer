import stru_sign_reward_data_pb2 as _stru_sign_reward_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignRewardNotifyRequest(_message.Message):
    __slots__ = ("sign_days", "reward_days", "sign_reward_data_map")
    class SignRewardDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_sign_reward_data_pb2.SignRewardData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_sign_reward_data_pb2.SignRewardData, _Mapping]] = ...) -> None: ...
    SIGN_DAYS_FIELD_NUMBER: _ClassVar[int]
    REWARD_DAYS_FIELD_NUMBER: _ClassVar[int]
    SIGN_REWARD_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    sign_days: _containers.RepeatedScalarFieldContainer[int]
    reward_days: _containers.RepeatedScalarFieldContainer[int]
    sign_reward_data_map: _containers.MessageMap[int, _stru_sign_reward_data_pb2.SignRewardData]
    def __init__(self, sign_days: _Optional[_Iterable[int]] = ..., reward_days: _Optional[_Iterable[int]] = ..., sign_reward_data_map: _Optional[_Mapping[int, _stru_sign_reward_data_pb2.SignRewardData]] = ...) -> None: ...
