"""
PRACTICE WINDOWS DEBUGGER DEFS
"""

from ctypes import *

HANDLE  = c_void_p
LPBYTE  = POINTER(c_ubyte)
LPTSTR  = POINTER(c_char)
WORD    = c_ushort
DWORD   = c_ulong


DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

class STARTUP_INFO(Structure):
    cb:             DWORD
    lpReserved:     LPTSTR
    lpDesktop:      LPTSTR
    lpTitle:        LPTSTR
    dwX:            DWORD
    dwY:            DWORD
    dwXSize:        DWORD
    dwYSize:        DWORD
    dwXCountChars:  DWORD
    dwYCountChars:  DWORD
    dwFlags:        DWORD
    wShowWindow:    WORD
    cbReserved2:    WORD
    lpReserved2:    LPBYTE
    hStdInput:      HANDLE
    hStdOutput:     HANDLE
    hStdError:      HANDLE

class PROCESS_INFO(Structure):
    hProcess:       HANDLE
    hThread:        HANDLE
    dwProcessId:    DWORD
    dwThreadId:     DWORD
