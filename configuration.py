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

#Ubidots
token    = '?token=XXXX-XXXXXXXXXXXXXXXXXXXXX'
device   = 'car-tracker-9087'
base_url = 'http://things.ubidots.com/api/v1.6/devices/'
position = '/position/values'

#Sampling period
period = 0.5

#OBD Port
obdport = '/dev/pts/18'

#GPS Port
gpsport = '/dev/ttyACM0'
#gpsport = 'test.nmea'
