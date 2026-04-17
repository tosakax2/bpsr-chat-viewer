import stru_community_build_life_profession_info_pb2 as _stru_community_build_life_profession_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildLifeProfessionInfoList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_community_build_life_profession_info_pb2.CommunityBuildLifeProfessionInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[_stru_community_build_life_profession_info_pb2.CommunityBuildLifeProfessionInfo, _Mapping]]] = ...) -> None: ...
