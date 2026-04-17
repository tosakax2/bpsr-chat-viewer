import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_boss_data_pb2 as _stru_union_boss_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionGetAllBossDataReply(_message.Message):
    __slots__ = ("boss_datas", "err_code")
    class BossDatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_boss_data_pb2.UnionBossData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_boss_data_pb2.UnionBossData, _Mapping]] = ...) -> None: ...
    BOSS_DATAS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    boss_datas: _containers.MessageMap[int, _stru_union_boss_data_pb2.UnionBossData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, boss_datas: _Optional[_Mapping[int, _stru_union_boss_data_pb2.UnionBossData]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
