#! /usr/bin/python3

# OrlocPlot

import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
import glob
import numpy as np

###############################
# IMPORT AND CONCATENATE DATA #
###############################

infilename = '../data/WS3-Orloc-full.csv'
#infilename = '../data/WS2-Buscaini-full.csv'
#infilename = '../data/WS1-turistica-full.csv'
df = pd.read_csv(infilename, header=1, infer_datetime_format=True, parse_dates=True, index_col='Time [UTC]', dtype=float, na_values=[' NAN', 50])

dfhr = df.resample('H').mean()
dfhr_s = df.resample('H').sum()

register_matplotlib_converters()

# All hourly
fig = plt.figure(figsize=(10,16))

# Battery voltage
ax = plt.subplot(10, 1, 1)
plt.plot(dfhr['Bat [V]'], 'k-')
plt.ylabel('Battery\nvoltage [V]', fontweight='bold')
plt.ylim(4.5, 4.7)
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Temperature
ax = plt.subplot(10, 1, 2)
plt.plot(dfhr['TempOB [C]'], 'g-')
plt.ylabel('On-board\ntemperature\n[$^\circ$C]', fontweight='bold')
plt.ylim(0, 27)
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Atmospheric pressure
ax = plt.subplot(10, 1, 3)
plt.plot(dfhr['PresOB [mBar]'], 'g-')
plt.ylabel('On-board\natmospheric\npressure\n[millibar]', fontweight='bold')
plt.ylim(880, 920)
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board relative humidity
ax = plt.subplot(10, 1, 4)
plt.plot(dfhr['RH_OB [%]'], 'g-')
plt.ylabel('On-board\nrelative\nhumidity [%]', fontweight='bold')
plt.ylim(0, 100)
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Wind direction
ax = plt.subplot(10, 1, 5)
# Note -- it could be backwards
#_wind_dir = dfhr['Wind direction [degrees]']
_wind_dir = dfhr['Wind direction [degrees]'] - 180
_wind_dir[_wind_dir<0] = 360+_wind_dir
plt.plot(_wind_dir, 'k.')
plt.ylabel('Wind\ndirection [$^\circ$]', fontweight='bold')
plt.ylim((0,360))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Wind speed
# Wind speed fit from SAFL wind-tunnel experiments
# https://github.com/NorthernWidget-Skunkworks/Project-Tally/tree/master/Data
# R2 = 0.959
# Measured once per minute. So:
rps = dfhr['NumTicks [Cnt]']/60.
wind_speed = 0.905*rps + 0.468
# InSpeed states that ~3 mph is their minimum valid speed
wind_speed[wind_speed<1.4] = np.nan
ax = plt.subplot(10, 1, 6)
# Note -- it could be backwards
#_wind_dir = dfhr['Wind direction [degrees]']
plt.plot(wind_speed, 'k')
plt.ylabel('Wind\nspeed [m s$^{-1}$]', fontweight='bold')
#plt.ylim((0,360))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Ground temperature
ax = plt.subplot(10, 1, 7)
plt.plot(dfhr['PyrgT [C]'], 'r-')
plt.ylabel('Ground\ntemperature\n(pyrgeometer)\n[$^\circ$C]', fontweight='bold')
plt.ylim((0,27))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Air temperature
ax = plt.subplot(10, 1, 8)
plt.plot(dfhr['Temp Atmos [C]'], 'r-')
plt.ylabel('Atmospheric\ntemperature\n[$^\circ$C]', fontweight='bold')
plt.ylim((0,27))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Relative humidity
ax = plt.subplot(10, 1, 9)
plt.plot(dfhr['Humidity [%]'], 'b-')
plt.ylim((0,100))
plt.ylabel('Relative\nhumidity [%]', fontweight='bold')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Rainfall
ax = plt.subplot(10, 1, 10)
plt.plot(dfhr_s['Rain bucket tips [0.01in]']*0.254, 'b-')
#plt.ylim(plt.ylim()[::-1])
plt.ylabel('Precipitation\n[mm hr$^{-1}$]', fontweight='bold')
plt.ylim((0,10))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
#plt.xticks(rotation=45)
fig.autofmt_xdate() # Better rotation

plt.xlabel('Date', fontweight='bold'  )
plt.tight_layout()
plt.savefig('OrlocData.pdf')
#plt.show()

