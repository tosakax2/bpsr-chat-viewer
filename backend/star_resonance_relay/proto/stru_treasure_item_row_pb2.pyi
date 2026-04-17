import stru_treasure_item_target_pb2 as _stru_treasure_item_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TreasureItemRow(_message.Message):
    __slots__ = ("config_id", "main_targets", "sub_targets")
    class MainTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_treasure_item_target_pb2.TreasureItemTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_treasure_item_target_pb2.TreasureItemTarget, _Mapping]] = ...) -> None: ...
    class SubTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_treasure_item_target_pb2.TreasureItemTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_treasure_item_target_pb2.TreasureItemTarget, _Mapping]] = ...) -> None: ...
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_TARGETS_FIELD_NUMBER: _ClassVar[int]
    SUB_TARGETS_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    main_targets: _containers.MessageMap[int, _stru_treasure_item_target_pb2.TreasureItemTarget]
    sub_targets: _containers.MessageMap[int, _stru_treasure_item_target_pb2.TreasureItemTarget]
    def __init__(self, config_id: _Optional[int] = ..., main_targets: _Optional[_Mapping[int, _stru_treasure_item_target_pb2.TreasureItemTarget]] = ..., sub_targets: _Optional[_Mapping[int, _stru_treasure_item_target_pb2.TreasureItemTarget]] = ...) -> None: ...
