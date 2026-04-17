import stru_medal_hole_pb2 as _stru_medal_hole_pb2
import stru_medal_node_pb2 as _stru_medal_node_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonMedalInfo(_message.Message):
    __slots__ = ("season_id", "normal_hole_infos", "core_hole_info", "core_hole_node_infos")
    class NormalHoleInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_medal_hole_pb2.MedalHole
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_medal_hole_pb2.MedalHole, _Mapping]] = ...) -> None: ...
    class CoreHoleNodeInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_medal_node_pb2.MedalNode
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_medal_node_pb2.MedalNode, _Mapping]] = ...) -> None: ...
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    NORMAL_HOLE_INFOS_FIELD_NUMBER: _ClassVar[int]
    CORE_HOLE_INFO_FIELD_NUMBER: _ClassVar[int]
    CORE_HOLE_NODE_INFOS_FIELD_NUMBER: _ClassVar[int]
    season_id: int
    normal_hole_infos: _containers.MessageMap[int, _stru_medal_hole_pb2.MedalHole]
    core_hole_info: _stru_medal_hole_pb2.MedalHole
    core_hole_node_infos: _containers.MessageMap[int, _stru_medal_node_pb2.MedalNode]
    def __init__(self, season_id: _Optional[int] = ..., normal_hole_infos: _Optional[_Mapping[int, _stru_medal_hole_pb2.MedalHole]] = ..., core_hole_info: _Optional[_Union[_stru_medal_hole_pb2.MedalHole, _Mapping]] = ..., core_hole_node_infos: _Optional[_Mapping[int, _stru_medal_node_pb2.MedalNode]] = ...) -> None: ...
