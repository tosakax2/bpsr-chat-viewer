import stru_cultivate_big_node_data_pb2 as _stru_cultivate_big_node_data_pb2
import stru_cultivate_middle_node_data_pb2 as _stru_cultivate_middle_node_data_pb2
import stru_cultivate_normal_node_data_pb2 as _stru_cultivate_normal_node_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CultivateAreaData(_message.Message):
    __slots__ = ("cultivate_normal_node_map", "cultivate_middle_node_map", "cultivate_big_node_map", "activate_effect_score", "is_active")
    class CultivateNormalNodeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_normal_node_data_pb2.CultivateNormalNodeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_normal_node_data_pb2.CultivateNormalNodeData, _Mapping]] = ...) -> None: ...
    class CultivateMiddleNodeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_middle_node_data_pb2.CultivateMiddleNodeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_middle_node_data_pb2.CultivateMiddleNodeData, _Mapping]] = ...) -> None: ...
    class CultivateBigNodeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_big_node_data_pb2.CultivateBigNodeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_big_node_data_pb2.CultivateBigNodeData, _Mapping]] = ...) -> None: ...
    CULTIVATE_NORMAL_NODE_MAP_FIELD_NUMBER: _ClassVar[int]
    CULTIVATE_MIDDLE_NODE_MAP_FIELD_NUMBER: _ClassVar[int]
    CULTIVATE_BIG_NODE_MAP_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_EFFECT_SCORE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    cultivate_normal_node_map: _containers.MessageMap[int, _stru_cultivate_normal_node_data_pb2.CultivateNormalNodeData]
    cultivate_middle_node_map: _containers.MessageMap[int, _stru_cultivate_middle_node_data_pb2.CultivateMiddleNodeData]
    cultivate_big_node_map: _containers.MessageMap[int, _stru_cultivate_big_node_data_pb2.CultivateBigNodeData]
    activate_effect_score: int
    is_active: bool
    def __init__(self, cultivate_normal_node_map: _Optional[_Mapping[int, _stru_cultivate_normal_node_data_pb2.CultivateNormalNodeData]] = ..., cultivate_middle_node_map: _Optional[_Mapping[int, _stru_cultivate_middle_node_data_pb2.CultivateMiddleNodeData]] = ..., cultivate_big_node_map: _Optional[_Mapping[int, _stru_cultivate_big_node_data_pb2.CultivateBigNodeData]] = ..., activate_effect_score: _Optional[int] = ..., is_active: bool = ...) -> None: ...
