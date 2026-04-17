import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CutsceneTextTableBase(_message.Message):
    __slots__ = ("id", "speaker_name", "text_content", "plot_characters_id", "voice_event_name", "voice_control_event")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    VOICE_CONTROL_EVENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    speaker_name: _table_basic_pb2.mlstring
    text_content: _table_basic_pb2.mlstring
    plot_characters_id: int
    voice_event_name: str
    voice_control_event: str
    def __init__(self, id: _Optional[int] = ..., speaker_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., text_content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., plot_characters_id: _Optional[int] = ..., voice_event_name: _Optional[str] = ..., voice_control_event: _Optional[str] = ...) -> None: ...

class CutsceneTextTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CutsceneTextTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CutsceneTextTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CutsceneTextTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CutsceneTextTableBase]] = ...) -> None: ...
