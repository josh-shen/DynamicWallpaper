from astral.sun import sun, golden_hour, blue_hour
from astral import LocationInfo, SunDirection
from datetime import timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# set - dawn/sunrise/noon/sunset/dusk times
loc = LocationInfo(timezone='US/Central', latitude=32.9493409, longitude=-96.6362936)
s = sun(loc.observer, tzinfo = 'US/Central')

dawn_time = s['dawn']            
sunrise_time = s['sunrise']
day_early_time = utc_to_local(golden_hour(loc.observer, direction=SunDirection.RISING)[1])   
noon_time = s['noon']
golden_time = utc_to_local(golden_hour(loc.observer, direction=SunDirection.SETTING)[0])
sunset_time = s['sunset']
blue_time = utc_to_local(blue_hour(loc.observer, direction=SunDirection.SETTING)[0])
dusk_time = s['dusk']       

# time markers
dawn = (dawn_time.hour * 60) + dawn_time.minute                 #dynamic_1.bmp 
sunrise = (sunrise_time.hour * 60) + sunrise_time.minute        #dynamic_2.bmp
day_early = (day_early_time.hour * 60) + day_early_time.minute  #dynamic_3.bmp
noon = (noon_time.hour * 60) + noon_time.minute                 #dynamic_4.bmp
golden = (golden_time.hour * 60) + golden_time.minute           #dynamic_5.bmp
sunset = (sunset_time.hour * 60) + sunset_time.minute           #dynamic_6.bmp
blue = (blue_time.hour * 60) + blue_time.minute                 #dynamic_7.bmp
dusk = (dusk_time.hour * 60) + dusk_time.minute                 #dynamic_8.bmp                           

# clear existing contents of file
f = open("times.txt", "w").close()

# write times to file
f = open("times.txt", "a")
f.write(str(dawn) + "\n")
f.write(str(sunrise) + "\n")
f.write(str(day_early) + "\n")
f.write(str(noon) + "\n")
f.write(str(golden) + "\n")
f.write(str(sunset) + "\n")
f.write(str(blue) + "\n")
f.write(str(dusk) + "\n")