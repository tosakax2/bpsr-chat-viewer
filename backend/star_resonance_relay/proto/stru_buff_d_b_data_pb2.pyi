from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffDBData(_message.Message):
    __slots__ = ("buff_uuid", "firer_id", "buff_config_id", "base_id", "level", "layer", "duration", "count", "create_time", "part_id", "create_scene_id", "custom_params_key", "custom_params")
    BUFF_UUID_FIELD_NUMBER: _ClassVar[int]
    FIRER_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PART_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PARAMS_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    buff_uuid: int
    firer_id: int
    buff_config_id: int
    base_id: int
    level: int
    layer: int
    duration: int
    count: int
    create_time: int
    part_id: int
    create_scene_id: int
    custom_params_key: _containers.RepeatedScalarFieldContainer[str]
    custom_params: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, buff_uuid: _Optional[int] = ..., firer_id: _Optional[int] = ..., buff_config_id: _Optional[int] = ..., base_id: _Optional[int] = ..., level: _Optional[int] = ..., layer: _Optional[int] = ..., duration: _Optional[int] = ..., count: _Optional[int] = ..., create_time: _Optional[int] = ..., part_id: _Optional[int] = ..., create_scene_id: _Optional[int] = ..., custom_params_key: _Optional[_Iterable[str]] = ..., custom_params: _Optional[_Iterable[int]] = ...) -> None: ...
