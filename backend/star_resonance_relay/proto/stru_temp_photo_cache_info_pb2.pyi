from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class tempPhotoCacheInfo(_message.Message):
    __slots__ = ("id", "temp_photo", "temp_ori_photo", "temp_thumb_photo", "shot_time", "shot_time_str", "shot_place", "decorate_data", "height", "width")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMP_PHOTO_FIELD_NUMBER: _ClassVar[int]
    TEMP_ORI_PHOTO_FIELD_NUMBER: _ClassVar[int]
    TEMP_THUMB_PHOTO_FIELD_NUMBER: _ClassVar[int]
    SHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOT_TIME_STR_FIELD_NUMBER: _ClassVar[int]
    SHOT_PLACE_FIELD_NUMBER: _ClassVar[int]
    DECORATE_DATA_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    id: str
    temp_photo: str
    temp_ori_photo: str
    temp_thumb_photo: str
    shot_time: int
    shot_time_str: str
    shot_place: str
    decorate_data: str
    height: int
    width: int
    def __init__(self, id: _Optional[str] = ..., temp_photo: _Optional[str] = ..., temp_ori_photo: _Optional[str] = ..., temp_thumb_photo: _Optional[str] = ..., shot_time: _Optional[int] = ..., shot_time_str: _Optional[str] = ..., shot_place: _Optional[str] = ..., decorate_data: _Optional[str] = ..., height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...
