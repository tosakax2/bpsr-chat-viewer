import stru_hero_key_item_info_pb2 as _stru_hero_key_item_info_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonHeroKeyInfo(_message.Message):
    __slots__ = ("char_id", "hero_key_item", "key_info", "use_item", "hero_key_award_item")
    class KeyInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_hero_key_item_info_pb2.HeroKeyItemInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_hero_key_item_info_pb2.HeroKeyItemInfo, _Mapping]] = ...) -> None: ...
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_KEY_ITEM_FIELD_NUMBER: _ClassVar[int]
    KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_ITEM_FIELD_NUMBER: _ClassVar[int]
    HERO_KEY_AWARD_ITEM_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    hero_key_item: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    key_info: _containers.MessageMap[int, _stru_hero_key_item_info_pb2.HeroKeyItemInfo]
    use_item: _stru_item_pb2.Item
    hero_key_award_item: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    def __init__(self, char_id: _Optional[int] = ..., hero_key_item: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., key_info: _Optional[_Mapping[int, _stru_hero_key_item_info_pb2.HeroKeyItemInfo]] = ..., use_item: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ..., hero_key_award_item: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ...) -> None: ...
