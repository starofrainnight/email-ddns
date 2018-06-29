# -*- coding: utf-8 -*-


class EMailDDNSError(Exception):
    pass


class NoEMailError(EMailDDNSError):
    pass


class EMailFetchError(EMailDDNSError):
    pass
