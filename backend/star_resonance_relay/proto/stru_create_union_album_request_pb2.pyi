import enum_e_album_right_pb2 as _enum_e_album_right_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUnionAlbumRequest(_message.Message):
    __slots__ = ("union_id", "name", "access")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    name: str
    access: _enum_e_album_right_pb2.EAlbumRight
    def __init__(self, union_id: _Optional[int] = ..., name: _Optional[str] = ..., access: _Optional[_Union[_enum_e_album_right_pb2.EAlbumRight, str]] = ...) -> None: ...
