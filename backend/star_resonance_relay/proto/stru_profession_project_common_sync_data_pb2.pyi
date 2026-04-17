from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionProjectCommonSyncData(_message.Message):
    __slots__ = ("profession_id", "project_name", "equip_info_map", "mod_info_map", "current_talent_stage_cfg_id")
    class EquipInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ModInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    EQUIP_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    MOD_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TALENT_STAGE_CFG_ID_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    project_name: str
    equip_info_map: _containers.ScalarMap[int, int]
    mod_info_map: _containers.ScalarMap[int, int]
    current_talent_stage_cfg_id: int
    def __init__(self, profession_id: _Optional[int] = ..., project_name: _Optional[str] = ..., equip_info_map: _Optional[_Mapping[int, int]] = ..., mod_info_map: _Optional[_Mapping[int, int]] = ..., current_talent_stage_cfg_id: _Optional[int] = ...) -> None: ...
