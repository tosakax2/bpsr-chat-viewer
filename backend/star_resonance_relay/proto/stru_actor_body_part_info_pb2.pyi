import enum_body_part_state_pb2 as _enum_body_part_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorBodyPartInfo(_message.Message):
    __slots__ = ("PartId", "Hp", "MaxHp", "State", "FleshyId")
    PARTID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FLESHYID_FIELD_NUMBER: _ClassVar[int]
    PartId: int
    Hp: int
    MaxHp: int
    State: _enum_body_part_state_pb2.BodyPartState
    FleshyId: int
    def __init__(self, PartId: _Optional[int] = ..., Hp: _Optional[int] = ..., MaxHp: _Optional[int] = ..., State: _Optional[_Union[_enum_body_part_state_pb2.BodyPartState, str]] = ..., FleshyId: _Optional[int] = ...) -> None: ...
