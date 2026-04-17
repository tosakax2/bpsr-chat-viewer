import stru_drop_award_history_pb2 as _stru_drop_award_history_pb2
import stru_drop_container_single_pb2 as _stru_drop_container_single_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DropContainerInfo(_message.Message):
    __slots__ = ("drop_containers", "drop_award_histories")
    class DropContainersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_drop_container_single_pb2.DropContainerSingle
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_drop_container_single_pb2.DropContainerSingle, _Mapping]] = ...) -> None: ...
    class DropAwardHistoriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_drop_award_history_pb2.DropAwardHistory
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_drop_award_history_pb2.DropAwardHistory, _Mapping]] = ...) -> None: ...
    DROP_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    DROP_AWARD_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    drop_containers: _containers.MessageMap[int, _stru_drop_container_single_pb2.DropContainerSingle]
    drop_award_histories: _containers.MessageMap[int, _stru_drop_award_history_pb2.DropAwardHistory]
    def __init__(self, drop_containers: _Optional[_Mapping[int, _stru_drop_container_single_pb2.DropContainerSingle]] = ..., drop_award_histories: _Optional[_Mapping[int, _stru_drop_award_history_pb2.DropAwardHistory]] = ...) -> None: ...
