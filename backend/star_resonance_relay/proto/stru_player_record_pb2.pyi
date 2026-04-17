import stru_player_record_info_pb2 as _stru_player_record_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRecord(_message.Message):
    __slots__ = ("player_record_infos",)
    class PlayerRecordInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_record_info_pb2.PlayerRecordInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_record_info_pb2.PlayerRecordInfo, _Mapping]] = ...) -> None: ...
    PLAYER_RECORD_INFOS_FIELD_NUMBER: _ClassVar[int]
    player_record_infos: _containers.MessageMap[int, _stru_player_record_info_pb2.PlayerRecordInfo]
    def __init__(self, player_record_infos: _Optional[_Mapping[int, _stru_player_record_info_pb2.PlayerRecordInfo]] = ...) -> None: ...
