from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPictureReviewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EPictureReviewNull: _ClassVar[EPictureReviewType]
    EPictureReviewFail: _ClassVar[EPictureReviewType]
    EPictureReviewed: _ClassVar[EPictureReviewType]
    EPictureReviewing: _ClassVar[EPictureReviewType]
EPictureReviewNull: EPictureReviewType
EPictureReviewFail: EPictureReviewType
EPictureReviewed: EPictureReviewType
EPictureReviewing: EPictureReviewType
