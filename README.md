# AvWx Brief

Aviation Weather Brief (AvWx Brief) - A script that compiles a weather briefing for a pre-defined flight using data derived from aviationweather.gov API.

## Why AvWx Brief?

Often times when pilots obtain a weather briefing, they are faced with the choice of examining the data themselves on aviationweather.gov or calling the hotline to get a brief over the phone.
This can become remedial for pilots making regular flights from their HUB, or pilots whose primary operations are within the vicinity of one particular field. 
For Part 61/107 pilots, there isn't an easily transparent tool to use to obtain useful weather data compared to Part 121 pilots, whose companies with sophisticated software can provide detailed briefings of their scheduled flights.

AvWx Brief shortens the time a pilot will take on the ground obtaining a data-driven, textual, and complete weather briefing instead of manually parsing the information using aviationweather.gov.

## Features

  - Obtains current METAR
  - Obtains current TAF
  - Obtains PIREPS and AIRMETs within a predefined radius
  - Allows easy user configuration within configuration file

## Upcoming Features

  - Winds Aloft Data
  - Store Enroute weather information
  - Minor flight planning features such as Velocity & Altitude information
  - Output result to HTML

## How to Use

  - Install Python, download and install this package to a directory of your choice.
  - Open config.ini, plug in the parameters of your choice
  - Run script
