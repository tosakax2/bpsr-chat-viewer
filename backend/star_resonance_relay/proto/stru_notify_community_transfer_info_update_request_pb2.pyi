import stru_community_transfer_pb2 as _stru_community_transfer_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityTransferInfoUpdateRequest(_message.Message):
    __slots__ = ("transfer_community",)
    TRANSFER_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    transfer_community: _stru_community_transfer_pb2.CommunityTransfer
    def __init__(self, transfer_community: _Optional[_Union[_stru_community_transfer_pb2.CommunityTransfer, _Mapping]] = ...) -> None: ...
