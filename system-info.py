import psutil
import cpuinfo
import platform
import wmi
import sys
import os
import locale
import ctypes

win_num = platform.win32_ver()[0]
win_edition = platform.win32_edition()
win_or = platform.architecture()[0]
device_name = platform.node()
ram = f'{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f}'
pc = wmi.WMI()
video = pc.Win32_VideoController()[0].name
windll = ctypes.windll.kernel32

print(f"Computer : {device_name.upper()}")
print(f"OS : Windows {win_num} {win_edition[:3]} {win_or[:2]}-{win_or[2:]}")
print(f"Architecture : x{platform.architecture()[0][:2]}")
print(f'System Language : {locale.windows_locale[windll.GetUserDefaultUILanguage()]}')
print(f'Processor : {cpuinfo.get_cpu_info()["brand_raw"]}')
print(f"Installed Memory (RAM) : {ram} GB")
print(f"Video Card : {video}")
