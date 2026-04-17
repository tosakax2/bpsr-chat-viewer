import stru_dancer_info_pb2 as _stru_dancer_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DanceBall(_message.Message):
    __slots__ = ("dance_id", "begin_time", "end_time", "rand_index", "dancers", "buff_id", "npc_id", "npc_pos_index", "sum_dance_score", "has_notify_npc")
    class DancersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dancer_info_pb2.DancerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dancer_info_pb2.DancerInfo, _Mapping]] = ...) -> None: ...
    DANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    RAND_INDEX_FIELD_NUMBER: _ClassVar[int]
    DANCERS_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_ID_FIELD_NUMBER: _ClassVar[int]
    NPC_POS_INDEX_FIELD_NUMBER: _ClassVar[int]
    SUM_DANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    HAS_NOTIFY_NPC_FIELD_NUMBER: _ClassVar[int]
    dance_id: int
    begin_time: int
    end_time: int
    rand_index: int
    dancers: _containers.MessageMap[int, _stru_dancer_info_pb2.DancerInfo]
    buff_id: int
    npc_id: int
    npc_pos_index: int
    sum_dance_score: int
    has_notify_npc: bool
    def __init__(self, dance_id: _Optional[int] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ..., rand_index: _Optional[int] = ..., dancers: _Optional[_Mapping[int, _stru_dancer_info_pb2.DancerInfo]] = ..., buff_id: _Optional[int] = ..., npc_id: _Optional[int] = ..., npc_pos_index: _Optional[int] = ..., sum_dance_score: _Optional[int] = ..., has_notify_npc: bool = ...) -> None: ...
