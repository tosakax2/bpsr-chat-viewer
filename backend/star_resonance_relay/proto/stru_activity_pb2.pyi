import stru_activity_award_pb2 as _stru_activity_award_pb2
import enum_e_activity_status_pb2 as _enum_e_activity_status_pb2
import enum_e_activity_type_pb2 as _enum_e_activity_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Activity(_message.Message):
    __slots__ = ("activity_uuid", "activity_config_id", "activity_name", "activity_type", "start_time", "end_time", "notice", "order_id", "status", "award_list")
    class ActivityNameEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class NoticeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class AwardListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_activity_award_pb2.ActivityAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_activity_award_pb2.ActivityAward, _Mapping]] = ...) -> None: ...
    ACTIVITY_UUID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AWARD_LIST_FIELD_NUMBER: _ClassVar[int]
    activity_uuid: int
    activity_config_id: int
    activity_name: _containers.ScalarMap[int, str]
    activity_type: _enum_e_activity_type_pb2.EActivityType
    start_time: int
    end_time: int
    notice: _containers.ScalarMap[int, str]
    order_id: int
    status: _enum_e_activity_status_pb2.EActivityStatus
    award_list: _containers.MessageMap[int, _stru_activity_award_pb2.ActivityAward]
    def __init__(self, activity_uuid: _Optional[int] = ..., activity_config_id: _Optional[int] = ..., activity_name: _Optional[_Mapping[int, str]] = ..., activity_type: _Optional[_Union[_enum_e_activity_type_pb2.EActivityType, str]] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., notice: _Optional[_Mapping[int, str]] = ..., order_id: _Optional[int] = ..., status: _Optional[_Union[_enum_e_activity_status_pb2.EActivityStatus, str]] = ..., award_list: _Optional[_Mapping[int, _stru_activity_award_pb2.ActivityAward]] = ...) -> None: ...
