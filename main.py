#NoFlash
from pymem import Pymem, process
from re import search

patch = b'\x0f\x82'
location = rb'\x0f\x83....\x48\x8b\x1d....\x40\x38\x73' 
# 0f 83 ? ? ? ? 48 8b 1d ? ? ? ? 40 38 73

pm = Pymem('cs2.exe')

client = process.module_from_name(pm.process_handle, 'client.dll')
clientBytes = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage) 

address = client.lpBaseOfDll + search(location, clientBytes).start()
pm.write_bytes(address, patch, len(patch))