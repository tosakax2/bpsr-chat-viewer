import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendshipLevelBase(_message.Message):
    __slots__ = ("level", "exp", "is_award_level", "content", "function_unlock", "reward_id", "award_id")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    IS_AWARD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    level: int
    exp: int
    is_award_level: bool
    content: _table_basic_pb2.mlstring
    function_unlock: str
    reward_id: _table_basic_pb2.int_table
    award_id: int
    def __init__(self, level: _Optional[int] = ..., exp: _Optional[int] = ..., is_award_level: bool = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., function_unlock: _Optional[str] = ..., reward_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., award_id: _Optional[int] = ...) -> None: ...

class FriendshipLevelMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FriendshipLevelBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FriendshipLevelBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FriendshipLevelBase]
    def __init__(self, datas: _Optional[_Mapping[int, FriendshipLevelBase]] = ...) -> None: ...
