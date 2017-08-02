# (C) Copyright 2017
#
# Embexus Embedded Systems Solutions, ayoub.zaki@embexus.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307 USA
#
import pynmea2
import requests
import json 
import time 
import sys
import configuration as cfg
from urlparse import urljoin

ubiurl_pos= urljoin(cfg.base_url, cfg.device + cfg.position + cfg.token )
print ubiurl_pos

gps_data = json.loads('{"value": 0, "context": {"lat": 0, "lng": 0}}')

gps_input = open(cfg.gpsport, "r")
streamreader = pynmea2.NMEAStreamReader(gps_input)

try:
   gps_input = open(cfg.gpsport, "r")

except IOError:
    print "Could not get GPS port:", fname
    sys.exit(1)


while (True):
    for msg in streamreader.next():
        if isinstance(msg, pynmea2.types.talker.RMC):
            gps_data['context']['lat'] = msg.latitude
            gps_data['context']['lng'] = msg.longitude
            print gps_data
            r = requests.post(ubiurl_pos, json=gps_data)
            time.sleep(cfg.period)
