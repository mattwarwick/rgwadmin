"""
rgwadmin.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the rgwadmin exceptions.

"""


class RGWAdminException(RuntimeError):
    """There was a unlabled exception that was raised durning your request"""


class AccessDenied(RGWAdminException):
    """Access was denied for the request."""


class UserExists(RGWAdminException):
    """Attempt to create existing user."""


class InvalidAccessKey(RGWAdminException):
    """Invalid access key specified."""


class InvalidKeyType(RGWAdminException):
    """Invalid key type specified."""


class InvalidSecretKey(RGWAdminException):
    """Invalid secret key specified."""


class InvalidKeyType(RGWAdminException):
    """Invalid key type specified."""


class KeyExists(RGWAdminException):
    """Provided access key exists and belongs to another user."""


class EmailExists(RGWAdminException):
    """Provided email address exists."""


class InvalidCap(RGWAdminException):
    """Attempt to grant invalid admin capability."""


class SubuserExists(RGWAdminException):
    """Specified subuser exists."""


class InvalidAccess(RGWAdminException):
    """Invalid subuser access specified."""


class IndexRepairFailed(RGWAdminException):
    """Bucket index repair failed."""


class BucketNotEmpty(RGWAdminException):
    """Attempted to delete non-empty bucket."""


class ObjectRemovalFailed(RGWAdminException):
    """Unable to remove objects."""


class BucketUnlinkFailed(RGWAdminException):
    """Unable to unlink bucket from specified user."""


class BucketLinkFailed(RGWAdminException):
    """Unable to link bucket to specified user."""


class NoSuchObject(RGWAdminException):
    """Specified object does not exist."""


class IncompleteBody(RGWAdminException):
    """Either bucket was not specified for a bucket policy request or bucket
       and object were not specified for an object policy request."""


class InvalidCap(RGWAdminException):
    """Attempt to grant invalid admin capability."""


class NoSuchCap(RGWAdminException):
    """User does not possess specified capability."""


class InternalError(RGWAdminException):
    """Internal server error."""


class NoSuchUser(RGWAdminException):
    """User does not exist."""


class NoSuchBucket(RGWAdminException):
    """Bucket does not exist."""


class NoSuchKey(RGWAdminException):
    """No such access key."""