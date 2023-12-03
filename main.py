# NoFlash
from pymem import *

patch = b'\x0f\x82'
location = b'\x0f\x83....\x48\x8b\x1d....\x40\x38\x73' 
# 0f 83 ? ? ? ? 48 8b 1d ? ? ? ? 40 38 73

pm = Pymem('cs2.exe')
client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

address = pymem.pattern.pattern_scan_module(pm.process_handle, client, location)
pm.write_bytes(address, patch, len(patch))
