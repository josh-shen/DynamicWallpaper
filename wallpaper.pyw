import time
import os
import ctypes
from ctypes import wintypes
from astral.sun import sun
from astral import LocationInfo

#set - dawn/sunrise/noon/sunset/dusk times
loc = LocationInfo(timezone = 'US/Central', latitude = 0, longitude = 0)
s = sun(loc.observer, tzinfo = 'US/Central')

dawn_time = s['dawn']            
sunrise_time = s['sunrise']      
noon_time = s['noon']            
sunset_time = s['sunset']       
dusk_time = s['dusk']           

#time markers
dawn = (dawn_time.hour * 60) + dawn_time.minute           
sunrise = (sunrise_time.hour * 60) + sunrise_time.minute       
day_early = sunrise + 75                                     
noon = (noon_time.hour * 60) + noon_time.minute                
day_late = noon + 315                                       
sunset = (sunset_time.hour * 60) + sunset_time.minute         
dusk = (dusk_time.hour * 60) + dusk_time.minute - 5            
night = dusk + 5                                             

#wallpapers file path
wallpapers = [
    
]

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

while True:
    # get current time
    current_time = time.localtime()
    t = (current_time.tm_hour * 60) + current_time.tm_min
    # get current wallpaper
    SPI_GETDESKWALLPAPER = 0x0073

    dll = ctypes.WinDLL('user32')
    dll.SystemParametersInfoW.argtypes = wintypes.UINT, wintypes.UINT, wintypes.LPVOID, wintypes.UINT
    dll.SystemParametersInfoW.restype = wintypes.BOOL

    path = ctypes.create_unicode_buffer(260)
    dll.SystemParametersInfoW(SPI_GETDESKWALLPAPER, ctypes.sizeof(path), path, 0)

    if (dawn <= t < sunrise):
        image = wallpapers[0]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (sunrise <= t < day_early):
        image = wallpapers[1]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (t > day_early) and (t < noon):
        image = wallpapers[2]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (noon <= t < day_late):
        image = wallpapers[3]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (t > day_late) and (t < sunset):
        image = wallpapers[4]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (sunset <= t < dusk):
        image = wallpapers[5]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (dusk <= t < night):
        image = wallpapers[6]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)
    elif (t > night) or (t < dawn):
        image = wallpapers[7]
        if path.value == image:
            continue
        else:
            set_wallpaper(image)

    time.sleep(30)

    #new day, update time markers
    if t == 0:
        loc = LocationInfo(timezone = 'US/Central', latitude = 32.97447, longitude = -96.75368)
        s = sun(loc.observer, tzinfo = 'US/Central')

        dawn_time = s['dawn']            
        sunrise_time = s['sunrise']      
        noon_time = s['noon']            
        sunset_time = s['sunset']       
        dusk_time = s['dusk']           

        dawn = (dawn_time.hour * 60) + dawn_time.minute 
        sunrise = (sunrise_time.hour * 60) + sunrise_time.minute
        day_early = sunrise + 10
        noon = (noon_time.hour * 60) + noon_time.minute
        day_late = noon + 300
        sunset = (sunset_time.hour * 60) + sunset_time.minute
        dusk = (dusk_time.hour * 60) + dusk_time.minute - 10
        night = dusk + 10
    else:
        continue
