import stru_community_build_life_profession_info_list_pb2 as _stru_community_build_life_profession_info_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildLifeProfessionInfos(_message.Message):
    __slots__ = ("build_life_profession_infos",)
    class BuildLifeProfessionInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_build_life_profession_info_list_pb2.CommunityBuildLifeProfessionInfoList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_build_life_profession_info_list_pb2.CommunityBuildLifeProfessionInfoList, _Mapping]] = ...) -> None: ...
    BUILD_LIFE_PROFESSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    build_life_profession_infos: _containers.MessageMap[int, _stru_community_build_life_profession_info_list_pb2.CommunityBuildLifeProfessionInfoList]
    def __init__(self, build_life_profession_infos: _Optional[_Mapping[int, _stru_community_build_life_profession_info_list_pb2.CommunityBuildLifeProfessionInfoList]] = ...) -> None: ...
