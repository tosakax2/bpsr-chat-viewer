import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VisualLayerBase(_message.Message):
    __slots__ = ("id", "visual_layer_type", "main_ui", "revive_table_id", "audio_bank", "bgm", "black_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAIN_UI_FIELD_NUMBER: _ClassVar[int]
    REVIVE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BANK_FIELD_NUMBER: _ClassVar[int]
    BGM_FIELD_NUMBER: _ClassVar[int]
    BLACK_MASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    visual_layer_type: int
    main_ui: int
    revive_table_id: _table_basic_pb2.int_array
    audio_bank: _table_basic_pb2.string_array
    bgm: str
    black_mask: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., visual_layer_type: _Optional[int] = ..., main_ui: _Optional[int] = ..., revive_table_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., audio_bank: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., bgm: _Optional[str] = ..., black_mask: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class VisualLayerMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: VisualLayerBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[VisualLayerBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, VisualLayerBase]
    def __init__(self, datas: _Optional[_Mapping[int, VisualLayerBase]] = ...) -> None: ...
