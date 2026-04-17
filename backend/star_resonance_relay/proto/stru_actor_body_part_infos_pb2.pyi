import stru_actor_body_part_info_pb2 as _stru_actor_body_part_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorBodyPartInfos(_message.Message):
    __slots__ = ("Uuid", "Infos")
    UUID_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    Infos: _containers.RepeatedCompositeFieldContainer[_stru_actor_body_part_info_pb2.ActorBodyPartInfo]
    def __init__(self, Uuid: _Optional[int] = ..., Infos: _Optional[_Iterable[_Union[_stru_actor_body_part_info_pb2.ActorBodyPartInfo, _Mapping]]] = ...) -> None: ...
