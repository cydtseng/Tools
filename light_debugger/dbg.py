"""
PRACTICE WINDOWS DEBUGGER
"""

from ctypes import *
from dbg_defs import *

kernel32 = windll.kernel32

class dbg():
    def __init__(self):
        self.h_process              = None
        self.pid                    = None
        self.debugger_active        = False
	
    def load(self,path_to_exe):
        #creation_flags = CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS

        startup_info = STARTUP_INFO()
        process_info = PROCESS_INFO()

        startup_info.dwFlags = 0x1
        startup_info.wShowWindow = 0x0

        startup_info.cb = sizeof(startup_info)

        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startup_info),
                                   byref(process_info)):
            print("[*] Debugger Launched.")
            print("[*] PID: %d" % process_info.dwProcessId)
            self.h_process = self.open_process(process_info.dwProcessId)
        else:
            print("[*] Error Launching Debugger: 0x%08x." % kernel32.GetLastError())

    
    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,pid,False)
        return h_process

    def attach(self,pid):
        self.h_process = self.open_process(pid)
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid  = pid
            self.run()
        else:
            print("[*] Unable to attach to the process.")

    def run(self):
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE

        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
            raw_input("Please press a key to continue")
            self.debugger_active = False
            kernel32.ContinueDebugEvent(debug_event.dwProcessId, debug_event.dwThreadId, continue_status)

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Debugging Complete. Program terminated.")
            return True
        else:
            print ("[*] Error terminating Debugger.")
            return False
