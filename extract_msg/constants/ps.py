"""
Property set identifier constants.
"""

__all__ = [
    'PSETID_ADDRESS',
    'PSETID_AIRSYNC',
    'PSETID_APPOINTMENT',
    'PSETID_ATTACHMENT',
    'PSETID_CALENDAR_ASSISTANT',
    'PSETID_COMMON',
    'PSETID_LOG',
    'PSETID_MEETING',
    'PSETID_MESSAGING',
    'PSETID_NOTE',
    'PSETID_POSTRSS',
    'PSETID_SHARING',
    'PSETID_TASK',
    'PSETID_UNIFIEDMESSAGING',
    'PSETID_XMLEXTRACTEDENTITIES',
    'PS_INTERNET_HEADERS',
    'PS_MAPI',
    'PS_PUBLIC_STRINGS',
]

from typing import Final


PS_MAPI : Final[str] = '{00020328-0000-0000-C000-000000000046}'
PS_PUBLIC_STRINGS : Final[str] = '{00020329-0000-0000-C000-000000000046}'
PSETID_COMMON : Final[str] = '{00062008-0000-0000-C000-000000000046}'
PSETID_ADDRESS : Final[str] = '{00062004-0000-0000-C000-000000000046}'
PS_INTERNET_HEADERS : Final[str] = '{00020386-0000-0000-C000-000000000046}'
PSETID_APPOINTMENT : Final[str] = '{00062002-0000-0000-C000-000000000046}'
PSETID_MEETING : Final[str] = '{6ED8DA90-450B-101B-98DA-00AA003F1305}'
PSETID_LOG : Final[str] = '{0006200A-0000-0000-C000-000000000046}'
PSETID_MESSAGING : Final[str] = '{41F28F13-83F4-4114-A584-EEDB5A6B0BFF}'
PSETID_NOTE : Final[str] = '{0006200E-0000-0000-C000-000000000046}'
PSETID_POSTRSS : Final[str] = '{00062041-0000-0000-C000-000000000046}'
PSETID_TASK : Final[str] = '{00062003-0000-0000-C000-000000000046}'
PSETID_UNIFIEDMESSAGING : Final[str] = '{4442858E-A9E3-4E80-B900-317A210CC15B}'
PSETID_AIRSYNC : Final[str] = '{71035549-0739-4DCB-9163-00F0580DBBDF}'
PSETID_SHARING : Final[str] = '{00062040-0000-0000-C000-000000000046}'
PSETID_XMLEXTRACTEDENTITIES : Final[str] = '{23239608-685D-4732-9C55-4C95CB4E8E33}'
PSETID_ATTACHMENT : Final[str] = '{96357F7F-59E1-47D0-99A7-46515C183B54}'
PSETID_CALENDAR_ASSISTANT : Final[str] = '{11000E07-B51B-40D6-AF21-CAA85EDAB1D0}'