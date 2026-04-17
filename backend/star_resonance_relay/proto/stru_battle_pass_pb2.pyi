import stru_battle_pass_award_info_pb2 as _stru_battle_pass_award_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePass(_message.Message):
    __slots__ = ("id", "level", "curexp", "week_exp", "exp_last_time", "is_unlock", "buy_normal_pas", "buy_prime_pass", "award", "is_valid", "is_sended_mail")
    class AwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_battle_pass_award_info_pb2.BattlePassAwardInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_battle_pass_award_info_pb2.BattlePassAwardInfo, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUREXP_FIELD_NUMBER: _ClassVar[int]
    WEEK_EXP_FIELD_NUMBER: _ClassVar[int]
    EXP_LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    BUY_NORMAL_PAS_FIELD_NUMBER: _ClassVar[int]
    BUY_PRIME_PASS_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    IS_SENDED_MAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: int
    curexp: int
    week_exp: int
    exp_last_time: int
    is_unlock: bool
    buy_normal_pas: bool
    buy_prime_pass: bool
    award: _containers.MessageMap[int, _stru_battle_pass_award_info_pb2.BattlePassAwardInfo]
    is_valid: bool
    is_sended_mail: bool
    def __init__(self, id: _Optional[int] = ..., level: _Optional[int] = ..., curexp: _Optional[int] = ..., week_exp: _Optional[int] = ..., exp_last_time: _Optional[int] = ..., is_unlock: bool = ..., buy_normal_pas: bool = ..., buy_prime_pass: bool = ..., award: _Optional[_Mapping[int, _stru_battle_pass_award_info_pb2.BattlePassAwardInfo]] = ..., is_valid: bool = ..., is_sended_mail: bool = ...) -> None: ...
