import os.path
import  pygeoip
from string import split

def find_country(IP):
    gi = pygeoip.GeoIP(os.path.dirname(__file__) + '/db/geoip/GeoIP.dat')
    address = split(IP, ':', 8)[0]
    country = gi.country_code_by_addr(address)
    return country.lower()
    
def find_extcountry(IP):
    gi = pygeoip.GeoIP(os.path.dirname(__file__) + '/db/geoip/GeoIP.dat')
    address = split(IP, ':', 8)[0]
    country = gi.country_name_by_addr(address)
    return country
