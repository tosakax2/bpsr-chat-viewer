import stru_map_sticker_task_info_pb2 as _stru_map_sticker_task_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapStickerInfo(_message.Message):
    __slots__ = ("sticker_map", "finish_map", "award_flag")
    class StickerMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_map_sticker_task_info_pb2.MapStickerTaskInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_map_sticker_task_info_pb2.MapStickerTaskInfo, _Mapping]] = ...) -> None: ...
    STICKER_MAP_FIELD_NUMBER: _ClassVar[int]
    FINISH_MAP_FIELD_NUMBER: _ClassVar[int]
    AWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    sticker_map: _containers.MessageMap[int, _stru_map_sticker_task_info_pb2.MapStickerTaskInfo]
    finish_map: _containers.RepeatedScalarFieldContainer[int]
    award_flag: int
    def __init__(self, sticker_map: _Optional[_Mapping[int, _stru_map_sticker_task_info_pb2.MapStickerTaskInfo]] = ..., finish_map: _Optional[_Iterable[int]] = ..., award_flag: _Optional[int] = ...) -> None: ...
