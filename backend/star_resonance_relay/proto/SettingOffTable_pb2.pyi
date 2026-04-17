import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingOffTableBase(_message.Message):
    __slots__ = ("id", "name", "pivot_id", "button", "setting_off_anim", "remind_radius")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PIVOT_ID_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    SETTING_OFF_ANIM_FIELD_NUMBER: _ClassVar[int]
    REMIND_RADIUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    pivot_id: int
    button: _table_basic_pb2.mlstring
    setting_off_anim: str
    remind_radius: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., pivot_id: _Optional[int] = ..., button: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., setting_off_anim: _Optional[str] = ..., remind_radius: _Optional[float] = ...) -> None: ...

class SettingOffTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SettingOffTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SettingOffTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SettingOffTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SettingOffTableBase]] = ...) -> None: ...
