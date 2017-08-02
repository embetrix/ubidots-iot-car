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
import obd
import requests
import json 
import time 
import sys
import configuration as cfg
from urlparse import urljoin

ubiurl_obd= urljoin(cfg.base_url, cfg.device + cfg.token)
obd_data = json.loads('{"rpm": 0, "speed": 0, "fuel": 0, "maf" : 0, "load" : 0, "temp" : 0}')
 
def callback_rpm(r):
    obd_data['rpm']   = r.value.magnitude

def callback_speed(s):
    obd_data['speed'] = s.value.magnitude

def callback_fuel(f):
    obd_data['fuel']  = f.value.magnitude

def callback_maf(m):
    obd_data['maf']   = m.value.magnitude

def callback_load(l):
    obd_data['load']  = l.value.magnitude

def callback_temp(t):
    obd_data['temp']  = t.value.magnitude

connection = obd.Async(cfg.obdport)
connection.watch(obd.commands.RPM, callback=callback_rpm)
connection.watch(obd.commands.SPEED, callback=callback_speed)
connection.watch(obd.commands.FUEL_LEVEL, callback=callback_fuel)
connection.watch(obd.commands.MAF, callback=callback_maf)
connection.watch(obd.commands.ENGINE_LOAD, callback=callback_load)
connection.watch(obd.commands.COOLANT_TEMP, callback=callback_temp)
connection.start()

if not connection.is_connected():
    print 'ODB connection failed!'
    sys.exit(1)

while(True):
     print obd_data
     r = requests.post(ubiurl_obd, json=obd_data)
     time.sleep(cfg.period)
