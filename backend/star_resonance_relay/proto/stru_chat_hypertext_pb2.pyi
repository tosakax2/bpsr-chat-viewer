import stru_place_holder_pb2 as _stru_place_holder_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatHypertext(_message.Message):
    __slots__ = ("config_id", "hypertext_contents")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    HYPERTEXT_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    hypertext_contents: _containers.RepeatedCompositeFieldContainer[_stru_place_holder_pb2.PlaceHolder]
    def __init__(self, config_id: _Optional[int] = ..., hypertext_contents: _Optional[_Iterable[_Union[_stru_place_holder_pb2.PlaceHolder, _Mapping]]] = ...) -> None: ...
