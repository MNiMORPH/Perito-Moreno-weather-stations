#! /usr/bin/python3

# OrlocPlot

import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
import glob

###############################
# IMPORT AND CONCATENATE DATA #
###############################

infilename = '../data/WS3-Orloc-full.csv'
df = pd.read_csv(infilename, header=1, infer_datetime_format=True, parse_dates=True, index_col='Time [UTC]', dtype=float, na_values=[' NAN', 50])

dfhr = df.resample('H').mean()
dfhr_s = df.resample('H').sum()

register_matplotlib_converters()

# All hourly
fig = plt.figure(figsize=(9,4.5))

"""
# Battery voltage
ax1 = plt.subplot(5, 1, 1)
plt.plot(dfhr['Bat [V]'], 'k-')
plt.ylabel('Battery voltage [V]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Temperature
ax2 = plt.subplot(5, 1, 2)
plt.plot(dfhr['TempOB [C]'], 'g-')
plt.ylabel('On-board\ntemperature [$^\circ$C]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board Atmospheric pressure
ax3 = plt.subplot(5, 1, 3)
plt.plot(dfhr['PresOB [mBar]'], 'g-')
plt.ylabel('On-boar atmospheric\npressure [millibar]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# On-board relative humidity
ax4 = plt.subplot(5, 1, 4)
plt.plot(dfhr['RH_OB [%]'], 'g-')
plt.ylabel('On-board\nrelative humidity [%]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
"""

"""
# Wind direction
ax1 = plt.subplot(3, 1, 1)
plt.plot(dfhr['Wind direction [degrees]'], 'k-')
plt.ylabel('Wind direction [$^\circ$]')
plt.ylim((0,360))
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
"""

"""
# IR temperature
ax3 = plt.subplot(5, 1, 3)
plt.plot(dfhr['IR_Long [C]'], 'g-')
plt.ylabel('IR temperature [$^\circ$C]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Air temperature / ground temperature
ax3 = plt.subplot(5, 1, 3)
plt.plot(dfhr['Temp Atmos [C]']/dfhr['PyrgT [C]'], 'g-')
plt.ylabel('On-board\ntemperature [$^\circ$C]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
"""

# Ground temperature
ax1 = plt.subplot(2, 1, 1)
plt.plot(dfhr['PyrgT [C]'], 'r-')
plt.ylabel('Ground temperature\n(pyrgeometer) [$^\circ$C]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())

# Rainfall
ax2 = plt.subplot(2, 1, 2)
plt.plot(dfhr_s['Rain bucket tips [0.01in]']*0.254, 'b-')
#plt.ylim(plt.ylim()[::-1])
plt.ylabel('Precipitation\n[mm hr$^{-1}$]')
#plt.xlim(( plt.xlim()[0] + plus_days, plt.xlim()[1] - minus_days ))
#plt.xticks(rotation=45)
fig.autofmt_xdate() # Better rotation

plt.xlabel('Date')
plt.tight_layout()
plt.savefig('OrlocData.pdf')
plt.show()

