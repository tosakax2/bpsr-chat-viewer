import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivationTableBase(_message.Message):
    __slots__ = ("id", "target_type", "scene_id", "param", "activation", "target_des")
    ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_DES_FIELD_NUMBER: _ClassVar[int]
    id: int
    target_type: int
    scene_id: int
    param: _table_basic_pb2.int_array
    activation: int
    target_des: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., target_type: _Optional[int] = ..., scene_id: _Optional[int] = ..., param: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., activation: _Optional[int] = ..., target_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class ActivationTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ActivationTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ActivationTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ActivationTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ActivationTableBase]] = ...) -> None: ...
