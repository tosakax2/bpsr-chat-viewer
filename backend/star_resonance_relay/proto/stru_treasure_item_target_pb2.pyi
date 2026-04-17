import stru_treasure_item_pb2 as _stru_treasure_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TreasureItemTarget(_message.Message):
    __slots__ = ("target_id", "target_num", "reward")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    target_num: int
    reward: _stru_treasure_item_pb2.TreasureItem
    def __init__(self, target_id: _Optional[int] = ..., target_num: _Optional[int] = ..., reward: _Optional[_Union[_stru_treasure_item_pb2.TreasureItem, _Mapping]] = ...) -> None: ...
