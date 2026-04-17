import stru_hero_key_roll_info_pb2 as _stru_hero_key_roll_info_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroKeyItemInfo(_message.Message):
    __slots__ = ("item", "roll_info")
    class RollInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hero_key_roll_info_pb2.HeroKeyRollInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hero_key_roll_info_pb2.HeroKeyRollInfo, _Mapping]] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ROLL_INFO_FIELD_NUMBER: _ClassVar[int]
    item: _stru_item_pb2.Item
    roll_info: _containers.MessageMap[int, _stru_hero_key_roll_info_pb2.HeroKeyRollInfo]
    def __init__(self, item: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ..., roll_info: _Optional[_Mapping[int, _stru_hero_key_roll_info_pb2.HeroKeyRollInfo]] = ...) -> None: ...
