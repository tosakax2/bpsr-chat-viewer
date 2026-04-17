import stru_cultivate_line_data_pb2 as _stru_cultivate_line_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonCultivateLineData(_message.Message):
    __slots__ = ("season_cultivate_line_map",)
    class SeasonCultivateLineMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_line_data_pb2.CultivateLineData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_line_data_pb2.CultivateLineData, _Mapping]] = ...) -> None: ...
    SEASON_CULTIVATE_LINE_MAP_FIELD_NUMBER: _ClassVar[int]
    season_cultivate_line_map: _containers.MessageMap[int, _stru_cultivate_line_data_pb2.CultivateLineData]
    def __init__(self, season_cultivate_line_map: _Optional[_Mapping[int, _stru_cultivate_line_data_pb2.CultivateLineData]] = ...) -> None: ...
