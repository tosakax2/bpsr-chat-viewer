import stru_cultivate_area_data_pb2 as _stru_cultivate_area_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CultivateLineSubTypeData(_message.Message):
    __slots__ = ("cultivate_line_data_map", "cultivate_line_area_list")
    class CultivateLineDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_area_data_pb2.CultivateAreaData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_area_data_pb2.CultivateAreaData, _Mapping]] = ...) -> None: ...
    CULTIVATE_LINE_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    CULTIVATE_LINE_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    cultivate_line_data_map: _containers.MessageMap[int, _stru_cultivate_area_data_pb2.CultivateAreaData]
    cultivate_line_area_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, cultivate_line_data_map: _Optional[_Mapping[int, _stru_cultivate_area_data_pb2.CultivateAreaData]] = ..., cultivate_line_area_list: _Optional[_Iterable[int]] = ...) -> None: ...
