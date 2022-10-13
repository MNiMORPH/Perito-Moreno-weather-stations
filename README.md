# Perito-Moreno-weather-stations
Data from UMN-deployed and Northern-Widget-provided weather stations along the southern side of Glacar Perito Moreno (Feb-Mar, 2022)

GNU GPL v3 license applies to software.

CC-BY 4.0 license applies to data.


## Field Notes

1. WS1's anemometer was set north while pointing into the wind (i.e., direction wind is coming from). WS2 and WS3 were set pointing away from the wind. Correct WS2 and WS3 by 180 degrees.
2. Tipping-bucket rain gauge data seems to freeze on all "1" on WS2 and WS3. Could be that the bucket is stuck in the middle. This also causes the logger to reset from time to time, but data continue to be recorded.
3. To combine multiple data files, retain the same header and merge rows.
4. On the first time step, a comma is missing near the end of the line. Include it (and note it / update the software that caused this problem).


