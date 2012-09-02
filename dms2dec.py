"""
Converting Degrees, Minutes, Seconds formatted coordinate strings to decimal. 

Formula:
DEC = (DEG + (MIN * 1/60) + (SEC * 1/60 * 1/60))

Assumes S/W are negative. 

"""

import re

def dms2dec(dms_str):
    
    dms_str = re.sub(r'\s', '', dms_str)
    
    if re.match('[swSW]', dms_str):
        sign = -1
    else:
        sign = 1
    
    (degree, minute, second, frac_seconds, junk) = re.split('\D+', dms_str, maxsplit=4)
    
    return sign * (int(degree) + float(minute) / 60 + float(second) / 3600 + float(frac_seconds) / 36000)