from _utils import *

# [Weixin.dll]
dll = path(input("\nWeixin.dll: "))
data = load(dll)
# Block multi-instance check (Mutex)
# Search 'XWeChat_App_Instance_Identity_Mutex_Name' to find the function.
# Just let it return.
print(f"\n> Blocking multi-instance check")
UNMUTEX_PATTERN = """
55
41 57
41 56
41 54
56
57
53
48 81 EC ?? ?? ?? ??
48 8D AC 24 ?? ?? ?? ??
48 C7 85 ?? ?? ?? ?? FE FF FF FF
48 C7 45 ?? 00 00 00 00
"""
UNMUTEX_REPLACE = """
C3
...
"""
data = wildcard_replace(data, UNMUTEX_PATTERN, UNMUTEX_REPLACE)
# Backup and save
backup(dll)
save(dll, data)
pause()
