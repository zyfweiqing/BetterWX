from _utils import *

# Number
n = input("\nNumber: (0~9): ")
if len(n) != 1 or not n in "0123456789":
    print(f"{RED}[ERR] Invalid number{RESET}")
    pause()
    exit()

# [Weixin.exe]
exe = exepath(input("\nWeixin.exe: "))
data = load(exe)
# Redirect Weixin.dll -> Weixin.dl2
print(f"\n> Redirecting Weixin.dll -> Weixin.dl{n}")
EXE_PATTERN = "\x00".join("Weixin.dll")
EXE_REPLACE = "\x00".join(f"Weixin.dl{n}")
data = replace(data, EXE_PATTERN, EXE_REPLACE)
# Rename Weixin.exe -> Weixin2.exe
new_exe = exe.with_name(f"Weixin{n}.exe")
save(new_exe, data)

# [Weixin.dll]
dll = dllpath(input("\nWeixin.dll: "))
data = load(dll)
# Redirect global_config -> global_conf2g
# Just search 'global_config' and you'll find the pattern.
# 48 B8:     67 6C 6F 62 61 6C 5F 63   // MOV RAX, "global_c" (0x5F6C61626F6C676)
# 48 89 05: [07 78 C3 07]              // MOV [RIP+offset], RAX
# C7 05:    [05 78 C3 07] 6F 6E 66 69  // MOV dword [RIP+offset], "onfi" (0x69666E6F)
# 66 C7 05: [00 78 C3 07] 67 00        // MOV word [RIP+offset], "g\0" (0x0067)
# Change "onfi" to "onf{n}" so we have "global_conf{n}g\0"
print(f"\n> Redirecting global_config -> global_conf{n}g")
COEXIST_CONFIG_PATTERN = """
48 B8 67 6C 6F 62 61 6C 5F 63
48 89 05 ?? ?? ?? ??
C7 05 ?? ?? ?? ?? 6F 6E 66 69
66 C7 05 ?? ?? ?? ?? 67 00
"""
COEXIST_CONFIG_REPLACE = f"""
...
C7 05 ?? ?? ?? ?? 6F 6E 66 {ord(n):02X}
66 C7 05 ?? ?? ?? ?? 67 00
"""
data = wildcard_replace(data, COEXIST_CONFIG_PATTERN, COEXIST_CONFIG_REPLACE)
# Redirect host-redirect.xml -> host-redirect.xm2
# This file affects the auto-login feature.
print(f"\n> Redirecting host-redirect.xml -> host-redirect.xm{n}")
AUTOLOGIN_PATTERN = "host-redirect.xml"
AUTOLOGIN_REPLACE = f"host-redirect.xm{n}"
data = replace(data, AUTOLOGIN_PATTERN, AUTOLOGIN_REPLACE)
# Block multi-instance check
# See `unmutex.py`.
print(f"\n> Blocking multi-instance check")
UNLOCK_PATTERN = """
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
UNLOCK_REPLACE = """
C3
...
"""
data = wildcard_replace(data, UNLOCK_PATTERN, UNLOCK_REPLACE)
# Rename Weixin.dll -> Weixin.dl2
new_dll = dll.with_name(f"Weixin.dl{n}")
save(new_dll, data)
pause()
