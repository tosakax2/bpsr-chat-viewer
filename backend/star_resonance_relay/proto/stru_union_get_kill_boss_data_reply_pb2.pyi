import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_raid_kill_boss_record_pb2 as _stru_union_raid_kill_boss_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionGetKillBossDataReply(_message.Message):
    __slots__ = ("kill_cnt", "kill_boss_records", "err_code")
    KILL_CNT_FIELD_NUMBER: _ClassVar[int]
    KILL_BOSS_RECORDS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    kill_cnt: int
    kill_boss_records: _containers.RepeatedCompositeFieldContainer[_stru_union_raid_kill_boss_record_pb2.UnionRaidKillBossRecord]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, kill_cnt: _Optional[int] = ..., kill_boss_records: _Optional[_Iterable[_Union[_stru_union_raid_kill_boss_record_pb2.UnionRaidKillBossRecord, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
