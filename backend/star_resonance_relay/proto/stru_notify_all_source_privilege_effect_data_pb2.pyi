import stru_source_privilege_effect_data_pb2 as _stru_source_privilege_effect_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyAllSourcePrivilegeEffectData(_message.Message):
    __slots__ = ("all_source_privilege_effects_map",)
    class AllSourcePrivilegeEffectsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_source_privilege_effect_data_pb2.SourcePrivilegeEffectData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_source_privilege_effect_data_pb2.SourcePrivilegeEffectData, _Mapping]] = ...) -> None: ...
    ALL_SOURCE_PRIVILEGE_EFFECTS_MAP_FIELD_NUMBER: _ClassVar[int]
    all_source_privilege_effects_map: _containers.MessageMap[int, _stru_source_privilege_effect_data_pb2.SourcePrivilegeEffectData]
    def __init__(self, all_source_privilege_effects_map: _Optional[_Mapping[int, _stru_source_privilege_effect_data_pb2.SourcePrivilegeEffectData]] = ...) -> None: ...
