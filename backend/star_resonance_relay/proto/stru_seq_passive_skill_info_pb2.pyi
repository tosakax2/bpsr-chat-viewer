import stru_passive_skill_info_pb2 as _stru_passive_skill_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeqPassiveSkillInfo(_message.Message):
    __slots__ = ("ActorUuid", "PassiveInfos")
    ACTORUUID_FIELD_NUMBER: _ClassVar[int]
    PASSIVEINFOS_FIELD_NUMBER: _ClassVar[int]
    ActorUuid: int
    PassiveInfos: _containers.RepeatedCompositeFieldContainer[_stru_passive_skill_info_pb2.PassiveSkillInfo]
    def __init__(self, ActorUuid: _Optional[int] = ..., PassiveInfos: _Optional[_Iterable[_Union[_stru_passive_skill_info_pb2.PassiveSkillInfo, _Mapping]]] = ...) -> None: ...
