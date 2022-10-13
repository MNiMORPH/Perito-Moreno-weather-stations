# Perito-Moreno-weather-stations
Data from UMN-deployed and Northern-Widget-provided weather stations along the southern side of Glacar Perito Moreno (Feb-Mar, 2022)

GNU GPL v3 license applies to software.

CC-BY 4.0 license applies to data.

## Locations

**Station**|**Lon**|**Lat**
-----|-----|-----
WS-1: turistica|-73.05851|-50.49192
WS-2: Buscaini|-73.12766|-50.51844
WS-3: Orloc|-73.13902|-50.53026

## Data collection timeline

*All data were collected from the time of deployment to our last visit on 2020-03-12. Due to the onset of the COVID-19 pandemic and our thereafter rapid departure from Patagonia, no further data were downloaded, though if the stations are intact, they likely have recorded substantial additional data.*

**Station**|**Start Date**|**Latest Collection Date**
-----|-----|-----
WS-1: turistica|2020-02-21|2020-03-12
WS-2: Buscaini|2020-02-23|2020-03-12
WS-3: Orloc|2020-02-23|2020-03-12


## Data columns

**CSV column**|**Description**
-----|-----
Time [UTC]|Universal Coordinated Time
PressOB [mBar]|Atmospheric pressure from the on-board (and housing-enclosed) BME280 sensor [degrees Celsius]
RH\_OB [%]|Atmospheric relative humidity from the on-board (and housing-enclosed) BME280 sensor [degrees Celsius]
TempOB [C]|Atmospheric temperature from the on-board (and housing-enclosed) BME280 sensor [degrees Celsius]
Temp RTC [C]|Atmospheric temperature from the on-board DS3231 real-time clock [degrees Celsius]
Bat [V]|Voltage of the batteries comprising the main power supply; during the 2021–2022 deployment, this was provided by 3x AA cells in series [volts]
R\_u [deg]|Roll of the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [degrees from horizontal]
P\_u [deg]|Pitch of the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [degrees from horizontal]
UVA\_u|Ultraviolet A radiation received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
UVB\_u|Ultraviolet B radiation received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
White\_u|Broad-spectrum visible white light received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
Vis\_u (lx)|Broad-spectrum visible light received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
IR\_S\_u|Short-wavelength infrared radiation received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
IR\_M\_u|Mid-wavelength infrared radiation received by the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
PyroT\_u [C]|Temperature on the upwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer circuit board [degrees Celsius]
R\_d [deg]|Roll of the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [degrees from horizontal]
P\_d [deg]|Pitch of the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [degrees from horizontal]
UVA\_d|Ultraviolet A radiation received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
UVB\_d|Ultraviolet B radiation received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
White\_d|Broad-spectrum visible white light received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [arbitrary sensor units]
Vis\_d (lx)|Broad-spectrum visible light received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
IR\_S\_d|Short-wavelength infrared radiation received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
IR\_M\_d|Mid-wavelength infrared radiation received by the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer [lux]
PyroT\_d [C]|Temperature on the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyranometer circuit board
IR\_Long [mV]|Voltage from the downwards-facing [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) pyrgeometer (long-wave infrared thermometer) [millivolts]
IR\_Long [C]|Inferred ground temperature from the [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) downwards-facing pyrgeometer (long-wave infrared thermometer) [degrees Celsius]
PyrgT [C]|Temperature on the [Project Monarch](https://github.com/NorthernWidget-Skunkworks/Project-Monarch) downwards-facing pyrgeometer (long-wave infrared thermometer) circuit board [degrees Celsius]
NumTicks [Cnt]|Number of recorded anemometer revolutions since the last data logging interval. -9999 is the error value. Can be converted into wind speed. [unitless]
Wind direction [degrees]|Wind direction. WS-2 and WS-3 should be corrected by 180 degrees. [azimuth: degrees]
Humidity [%]|Relative humidity [percent]
Temp Atmos [C]|Atmospheric temperature [degrees Celsius]
Distance [mm]|Distance from ultrasonic rangefinder to surface (rock or snow) [millimeters]
Rain bucket tips [0.01in]|The number of tipping-bucket rain gauge bucket tips [count]


## Field Notes

1. WS1's anemometer was set north while pointing into the wind (i.e., direction wind is coming from). WS2 and WS3 were set pointing away from the wind. Correct WS2 and WS3 by 180 degrees.
2. Tipping-bucket rain gauge data seems to freeze on all "1" on WS2 and WS3. Could be that the bucket is stuck in the middle. This also causes the logger to reset from time to time, but data continue to be recorded.
3. To combine multiple data files, retain the same header and merge rows.
4. On the first time step, a comma is missing near the end of the line. Include it (and note it / update the software that caused this problem).


## Deployment images



## Funding support

<img src="https://www.nsf.gov/news/mmg/media/images/nsf_logo_f_ba321daf-8607-41d7-94bc-1db6039d7893.jpg" alt="NSF" width="240px">

<img src="https://northernwidget.com/assets/images/NWseal_600px.png" alt="Northern Widget LLC" width="160px">

