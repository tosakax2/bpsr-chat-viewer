import stru_map_sticker_info_pb2 as _stru_map_sticker_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapBookInfo(_message.Message):
    __slots__ = ("id", "map_sticker_map", "award_flag")
    class MapStickerMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_map_sticker_info_pb2.MapStickerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_map_sticker_info_pb2.MapStickerInfo, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MAP_STICKER_MAP_FIELD_NUMBER: _ClassVar[int]
    AWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    map_sticker_map: _containers.MessageMap[int, _stru_map_sticker_info_pb2.MapStickerInfo]
    award_flag: int
    def __init__(self, id: _Optional[int] = ..., map_sticker_map: _Optional[_Mapping[int, _stru_map_sticker_info_pb2.MapStickerInfo]] = ..., award_flag: _Optional[int] = ...) -> None: ...
