import stru_cultivate_line_sub_type_data_pb2 as _stru_cultivate_line_sub_type_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CultivateLineData(_message.Message):
    __slots__ = ("cultivate_line_map",)
    class CultivateLineMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cultivate_line_sub_type_data_pb2.CultivateLineSubTypeData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cultivate_line_sub_type_data_pb2.CultivateLineSubTypeData, _Mapping]] = ...) -> None: ...
    CULTIVATE_LINE_MAP_FIELD_NUMBER: _ClassVar[int]
    cultivate_line_map: _containers.MessageMap[int, _stru_cultivate_line_sub_type_data_pb2.CultivateLineSubTypeData]
    def __init__(self, cultivate_line_map: _Optional[_Mapping[int, _stru_cultivate_line_sub_type_data_pb2.CultivateLineSubTypeData]] = ...) -> None: ...
