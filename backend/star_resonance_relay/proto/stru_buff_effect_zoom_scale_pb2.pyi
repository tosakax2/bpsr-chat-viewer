from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectZoomScale(_message.Message):
    __slots__ = ("zoom_ratio_add", "zoom_ratio_max")
    ZOOM_RATIO_ADD_FIELD_NUMBER: _ClassVar[int]
    ZOOM_RATIO_MAX_FIELD_NUMBER: _ClassVar[int]
    zoom_ratio_add: float
    zoom_ratio_max: float
    def __init__(self, zoom_ratio_add: _Optional[float] = ..., zoom_ratio_max: _Optional[float] = ...) -> None: ...
