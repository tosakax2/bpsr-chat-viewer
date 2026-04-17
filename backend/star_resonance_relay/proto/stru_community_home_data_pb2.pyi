import stru_community_homeland_recipe_pb2 as _stru_community_homeland_recipe_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityHomeData(_message.Message):
    __slots__ = ("community_id", "homeland_id", "buy_count", "unlocked_recipes", "level")
    class UnlockedRecipesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_homeland_recipe_pb2.CommunityHomelandRecipe
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_homeland_recipe_pb2.CommunityHomelandRecipe, _Mapping]] = ...) -> None: ...
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_RECIPES_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    buy_count: int
    unlocked_recipes: _containers.MessageMap[int, _stru_community_homeland_recipe_pb2.CommunityHomelandRecipe]
    level: int
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., buy_count: _Optional[int] = ..., unlocked_recipes: _Optional[_Mapping[int, _stru_community_homeland_recipe_pb2.CommunityHomelandRecipe]] = ..., level: _Optional[int] = ...) -> None: ...
