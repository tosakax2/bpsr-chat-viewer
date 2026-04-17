import enum_e_quest_step_status_pb2 as _enum_e_quest_step_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestData(_message.Message):
    __slots__ = ("id", "step_id", "state", "target_num", "target_max_num", "step_limit_time", "step_status", "add_limit_time", "target_type")
    class TargetNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class TargetMaxNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class TargetTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    TARGET_MAX_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_LIMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    STEP_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADD_LIMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    step_id: int
    state: int
    target_num: _containers.ScalarMap[int, int]
    target_max_num: _containers.ScalarMap[int, int]
    step_limit_time: int
    step_status: _enum_e_quest_step_status_pb2.EQuestStepStatus
    add_limit_time: int
    target_type: _containers.ScalarMap[int, int]
    def __init__(self, id: _Optional[int] = ..., step_id: _Optional[int] = ..., state: _Optional[int] = ..., target_num: _Optional[_Mapping[int, int]] = ..., target_max_num: _Optional[_Mapping[int, int]] = ..., step_limit_time: _Optional[int] = ..., step_status: _Optional[_Union[_enum_e_quest_step_status_pb2.EQuestStepStatus, str]] = ..., add_limit_time: _Optional[int] = ..., target_type: _Optional[_Mapping[int, int]] = ...) -> None: ...
