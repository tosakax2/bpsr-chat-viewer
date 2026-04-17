from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionTalentInfo(_message.Message):
    __slots__ = ("used_talent_points", "talent_node_ids", "talent_stage_cfg_id", "talent_ilegal_reset_count", "used_attack_mark", "used_guard_mark", "used_heal_mark")
    USED_TALENT_POINTS_FIELD_NUMBER: _ClassVar[int]
    TALENT_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    TALENT_STAGE_CFG_ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ILEGAL_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    USED_ATTACK_MARK_FIELD_NUMBER: _ClassVar[int]
    USED_GUARD_MARK_FIELD_NUMBER: _ClassVar[int]
    USED_HEAL_MARK_FIELD_NUMBER: _ClassVar[int]
    used_talent_points: int
    talent_node_ids: _containers.RepeatedScalarFieldContainer[int]
    talent_stage_cfg_id: int
    talent_ilegal_reset_count: int
    used_attack_mark: int
    used_guard_mark: int
    used_heal_mark: int
    def __init__(self, used_talent_points: _Optional[int] = ..., talent_node_ids: _Optional[_Iterable[int]] = ..., talent_stage_cfg_id: _Optional[int] = ..., talent_ilegal_reset_count: _Optional[int] = ..., used_attack_mark: _Optional[int] = ..., used_guard_mark: _Optional[int] = ..., used_heal_mark: _Optional[int] = ...) -> None: ...
