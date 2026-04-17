import stru_privilege_effect_list_data_pb2 as _stru_privilege_effect_list_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SourcePrivilegeEffectData(_message.Message):
    __slots__ = ("privilege_effects_map",)
    class PrivilegeEffectsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_privilege_effect_list_data_pb2.PrivilegeEffectListData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_privilege_effect_list_data_pb2.PrivilegeEffectListData, _Mapping]] = ...) -> None: ...
    PRIVILEGE_EFFECTS_MAP_FIELD_NUMBER: _ClassVar[int]
    privilege_effects_map: _containers.MessageMap[int, _stru_privilege_effect_list_data_pb2.PrivilegeEffectListData]
    def __init__(self, privilege_effects_map: _Optional[_Mapping[int, _stru_privilege_effect_list_data_pb2.PrivilegeEffectListData]] = ...) -> None: ...
