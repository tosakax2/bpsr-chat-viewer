import stru_dance_ball_pb2 as _stru_dance_ball_pb2
import stru_union_base_data_pb2 as _stru_union_base_data_pb2
import stru_union_event_pb2 as _stru_union_event_pb2
import stru_union_official_pb2 as _stru_union_official_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionInfo(_message.Message):
    __slots__ = ("base_info", "union_events", "officials", "auto_pass", "create_time", "change_name_time", "join_crow_fund_num", "dance_ball", "group_id", "group_type", "is_name_regist")
    class OfficialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_official_pb2.UnionOfficial
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_official_pb2.UnionOfficial, _Mapping]] = ...) -> None: ...
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    UNION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    OFFICIALS_FIELD_NUMBER: _ClassVar[int]
    AUTO_PASS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CHANGE_NAME_TIME_FIELD_NUMBER: _ClassVar[int]
    JOIN_CROW_FUND_NUM_FIELD_NUMBER: _ClassVar[int]
    DANCE_BALL_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_NAME_REGIST_FIELD_NUMBER: _ClassVar[int]
    base_info: _stru_union_base_data_pb2.UnionBaseData
    union_events: _containers.RepeatedCompositeFieldContainer[_stru_union_event_pb2.UnionEvent]
    officials: _containers.MessageMap[int, _stru_union_official_pb2.UnionOfficial]
    auto_pass: bool
    create_time: int
    change_name_time: int
    join_crow_fund_num: int
    dance_ball: _stru_dance_ball_pb2.DanceBall
    group_id: str
    group_type: int
    is_name_regist: bool
    def __init__(self, base_info: _Optional[_Union[_stru_union_base_data_pb2.UnionBaseData, _Mapping]] = ..., union_events: _Optional[_Iterable[_Union[_stru_union_event_pb2.UnionEvent, _Mapping]]] = ..., officials: _Optional[_Mapping[int, _stru_union_official_pb2.UnionOfficial]] = ..., auto_pass: bool = ..., create_time: _Optional[int] = ..., change_name_time: _Optional[int] = ..., join_crow_fund_num: _Optional[int] = ..., dance_ball: _Optional[_Union[_stru_dance_ball_pb2.DanceBall, _Mapping]] = ..., group_id: _Optional[str] = ..., group_type: _Optional[int] = ..., is_name_regist: bool = ...) -> None: ...
