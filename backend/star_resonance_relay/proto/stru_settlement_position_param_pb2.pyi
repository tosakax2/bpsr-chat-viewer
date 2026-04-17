import stru_settlement_position_pb2 as _stru_settlement_position_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettlementPositionParam(_message.Message):
    __slots__ = ("v_user_pos",)
    class VUserPosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_settlement_position_pb2.SettlementPosition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_settlement_position_pb2.SettlementPosition, _Mapping]] = ...) -> None: ...
    V_USER_POS_FIELD_NUMBER: _ClassVar[int]
    v_user_pos: _containers.MessageMap[int, _stru_settlement_position_pb2.SettlementPosition]
    def __init__(self, v_user_pos: _Optional[_Mapping[int, _stru_settlement_position_pb2.SettlementPosition]] = ...) -> None: ...
