import stru_common_award_info_pb2 as _stru_common_award_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalWorldBossInfo(_message.Message):
    __slots__ = ("score", "score_award_info", "boss_award_info", "uuid")
    class ScoreAwardInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_common_award_info_pb2.CommonAwardInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_common_award_info_pb2.CommonAwardInfo, _Mapping]] = ...) -> None: ...
    class BossAwardInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_common_award_info_pb2.CommonAwardInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_common_award_info_pb2.CommonAwardInfo, _Mapping]] = ...) -> None: ...
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_AWARD_INFO_FIELD_NUMBER: _ClassVar[int]
    BOSS_AWARD_INFO_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    score: int
    score_award_info: _containers.MessageMap[int, _stru_common_award_info_pb2.CommonAwardInfo]
    boss_award_info: _containers.MessageMap[int, _stru_common_award_info_pb2.CommonAwardInfo]
    uuid: int
    def __init__(self, score: _Optional[int] = ..., score_award_info: _Optional[_Mapping[int, _stru_common_award_info_pb2.CommonAwardInfo]] = ..., boss_award_info: _Optional[_Mapping[int, _stru_common_award_info_pb2.CommonAwardInfo]] = ..., uuid: _Optional[int] = ...) -> None: ...
