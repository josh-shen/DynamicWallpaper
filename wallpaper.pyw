import time
import os
import ctypes

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

dawn_set = sunrise_set = day_early_set = noon_set = day_late_set = sunset_set = dusk_set = night_set = False

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

while True:
    current_time = time.localtime()
    t = (current_time.tm_hour * 60) + current_time.tm_min

    if (dawn <= t < sunrise):
        image = wallpapers[0]
        if dawn_set == True:
            continue
        else:
            set_wallpaper(image)
            dawn_set = True
            night_set = False
    elif (sunrise <= t < day_early):
        image = wallpapers[1]
        if sunrise_set == True:
            continue
        else:
            set_wallpaper(image)
            sunrise_set = True
            dawn_set = False
    elif (t > day_early) and (t < noon):
        image = wallpapers[2]
        if day_early_set == True:
            continue
        else:
            set_wallpaper(image)
            day_early_set = True
            sunrise_set = False
    elif (noon <= t < day_late):
        image = wallpapers[3]
        if noon_set == True:
            continue
        else:
            set_wallpaper(image)
            noon_set = True
            day_early_set = False
    elif (t > day_late) and (t < sunset):
        image = wallpapers[4]
        if day_late_set == True:
            continue
        else:
            set_wallpaper(image)
            day_late_set = True
            noon_set = False
    elif (sunset <= t < dusk):
        image = wallpapers[5]
        if sunset_set == True:
            continue
        else:
            set_wallpaper(image)
            sunset_set = True
            day_late_set = False
    elif (dusk <= t < night):
        image = wallpapers[6]
        if dusk_set == True:
            continue
        else:
            set_wallpaper(image)
            dusk_set = True
            sunset_set = False 
    elif (t > night) or (t < dawn):
        image = wallpapers[7]
        if night_set == True:
            continue
        else:
            set_wallpaper(image)
            night_set = True
            dusk_set = False

    #new day, update time markers
    if t == 0:
        loc = LocationInfo(timezone = 'US/Central', latitude = 0, longitude = 0)
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
    
    time.sleep(60)