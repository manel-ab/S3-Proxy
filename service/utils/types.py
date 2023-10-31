"""Types for the service"""
from typing import TypedDict, Literal

type _statusCode = Literal[201, 422, 500]
type _ObjectUrl = str
type _Message = str


class _ObjectReference(TypedDict):
    """
    Object reference value on service response for upload_file endpoint.
    """

    url: _ObjectUrl


class _ErrorReference(TypedDict):
    """Type when an error occurred and a message needs to be sent."""

    message: _Message


type _Body = _ErrorReference | _ObjectReference


class ServiceResponse(TypedDict):
    "General service response."
    statusCode: _statusCode
    body: _Body
