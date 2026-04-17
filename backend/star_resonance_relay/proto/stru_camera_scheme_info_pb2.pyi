import enum_camera_pattern_type_pb2 as _enum_camera_pattern_type_pb2
import enum_camera_scheme_type_pb2 as _enum_camera_scheme_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class cameraSchemeInfo(_message.Message):
    __slots__ = ("camera_pattern_type", "camera_scheme_type", "scheme_key", "scheme_name", "scheme_time", "exposure", "contrast", "saturation", "horizontal", "vertical", "angle", "depth_tag", "aperture", "near_blend", "far_blend", "focus_tag", "focus", "world_time", "is_head_follow", "is_eye_follow", "show_entity_dicts", "show_ui_dicts", "filter_path", "id")
    class ShowEntityDictsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class ShowUiDictsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    CAMERA_PATTERN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMERA_SCHEME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEME_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEME_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    CONTRAST_FIELD_NUMBER: _ClassVar[int]
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    DEPTH_TAG_FIELD_NUMBER: _ClassVar[int]
    APERTURE_FIELD_NUMBER: _ClassVar[int]
    NEAR_BLEND_FIELD_NUMBER: _ClassVar[int]
    FAR_BLEND_FIELD_NUMBER: _ClassVar[int]
    FOCUS_TAG_FIELD_NUMBER: _ClassVar[int]
    FOCUS_FIELD_NUMBER: _ClassVar[int]
    WORLD_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_HEAD_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    IS_EYE_FOLLOW_FIELD_NUMBER: _ClassVar[int]
    SHOW_ENTITY_DICTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_UI_DICTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PATH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    camera_pattern_type: _enum_camera_pattern_type_pb2.CameraPatternType
    camera_scheme_type: _enum_camera_scheme_type_pb2.CameraSchemeType
    scheme_key: str
    scheme_name: str
    scheme_time: int
    exposure: float
    contrast: float
    saturation: float
    horizontal: float
    vertical: float
    angle: float
    depth_tag: bool
    aperture: float
    near_blend: float
    far_blend: float
    focus_tag: bool
    focus: float
    world_time: float
    is_head_follow: bool
    is_eye_follow: bool
    show_entity_dicts: _containers.ScalarMap[int, bool]
    show_ui_dicts: _containers.ScalarMap[int, bool]
    filter_path: str
    id: int
    def __init__(self, camera_pattern_type: _Optional[_Union[_enum_camera_pattern_type_pb2.CameraPatternType, str]] = ..., camera_scheme_type: _Optional[_Union[_enum_camera_scheme_type_pb2.CameraSchemeType, str]] = ..., scheme_key: _Optional[str] = ..., scheme_name: _Optional[str] = ..., scheme_time: _Optional[int] = ..., exposure: _Optional[float] = ..., contrast: _Optional[float] = ..., saturation: _Optional[float] = ..., horizontal: _Optional[float] = ..., vertical: _Optional[float] = ..., angle: _Optional[float] = ..., depth_tag: bool = ..., aperture: _Optional[float] = ..., near_blend: _Optional[float] = ..., far_blend: _Optional[float] = ..., focus_tag: bool = ..., focus: _Optional[float] = ..., world_time: _Optional[float] = ..., is_head_follow: bool = ..., is_eye_follow: bool = ..., show_entity_dicts: _Optional[_Mapping[int, bool]] = ..., show_ui_dicts: _Optional[_Mapping[int, bool]] = ..., filter_path: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...
