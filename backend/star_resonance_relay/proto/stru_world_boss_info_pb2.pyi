import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldBossInfo(_message.Message):
    __slots__ = ("boss_stage", "boss_killed_num", "uuid", "boss_cfg_id", "err_code")
    BOSS_STAGE_FIELD_NUMBER: _ClassVar[int]
    BOSS_KILLED_NUM_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    BOSS_CFG_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    boss_stage: int
    boss_killed_num: int
    uuid: int
    boss_cfg_id: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, boss_stage: _Optional[int] = ..., boss_killed_num: _Optional[int] = ..., uuid: _Optional[int] = ..., boss_cfg_id: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
