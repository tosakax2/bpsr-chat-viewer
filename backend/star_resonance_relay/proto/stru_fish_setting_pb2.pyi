import stru_fish_record_pb2 as _stru_fish_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishSetting(_message.Message):
    __slots__ = ("bait_id", "experiences", "research_fish_id", "fish_records", "fish_rod_durability", "rod_uuid", "level_reward", "zero_fish_times")
    class FishRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fish_record_pb2.FishRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fish_record_pb2.FishRecord, _Mapping]] = ...) -> None: ...
    class FishRodDurabilityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelRewardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ZeroFishTimesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BAIT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCES_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_FISH_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_RECORDS_FIELD_NUMBER: _ClassVar[int]
    FISH_ROD_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    ROD_UUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_REWARD_FIELD_NUMBER: _ClassVar[int]
    ZERO_FISH_TIMES_FIELD_NUMBER: _ClassVar[int]
    bait_id: int
    experiences: int
    research_fish_id: int
    fish_records: _containers.MessageMap[int, _stru_fish_record_pb2.FishRecord]
    fish_rod_durability: _containers.ScalarMap[int, int]
    rod_uuid: int
    level_reward: _containers.ScalarMap[int, bool]
    zero_fish_times: _containers.ScalarMap[int, int]
    def __init__(self, bait_id: _Optional[int] = ..., experiences: _Optional[int] = ..., research_fish_id: _Optional[int] = ..., fish_records: _Optional[_Mapping[int, _stru_fish_record_pb2.FishRecord]] = ..., fish_rod_durability: _Optional[_Mapping[int, int]] = ..., rod_uuid: _Optional[int] = ..., level_reward: _Optional[_Mapping[int, bool]] = ..., zero_fish_times: _Optional[_Mapping[int, int]] = ...) -> None: ...
