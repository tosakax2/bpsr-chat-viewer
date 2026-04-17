import stru_battle_pass_pb2 as _stru_battle_pass_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyAllValidBattlePassData(_message.Message):
    __slots__ = ("all_valid_battle_passs_map",)
    class AllValidBattlePasssMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_battle_pass_pb2.BattlePass
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_battle_pass_pb2.BattlePass, _Mapping]] = ...) -> None: ...
    ALL_VALID_BATTLE_PASSS_MAP_FIELD_NUMBER: _ClassVar[int]
    all_valid_battle_passs_map: _containers.MessageMap[int, _stru_battle_pass_pb2.BattlePass]
    def __init__(self, all_valid_battle_passs_map: _Optional[_Mapping[int, _stru_battle_pass_pb2.BattlePass]] = ...) -> None: ...
