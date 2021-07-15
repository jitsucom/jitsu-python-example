# Overview

This project demostrates how [Jitsu](https://jitsu.com) can be used to track anonymous usage events (aka Telemetry) for pip package. Basic
os info (version, platform it's) is being sent through [Jitsu.API](https://jitsu.com/docs/sending-data/api). On backend the data 
is enriched with location (Country, City) and other usefull parameters.

## How it works

Please note, that this repository is not a python package itself, but a demostration how Jitsu can work
as a **Telemetry** backend. Just copy the code to enable telemetry collection in your package.

The code sends two types of events:

 - `install` — when pip package is installed (via [setup.py](https://github.com/jitsucom/jitsu-python-example/blob/main/setup.py))
 - `module_init` — when module is initialized, see [\_\_init\_\_.py](https://github.com/jitsucom/jitsu-python-example/blob/main/jitsu_python_example/__init__.py)

 See the underlying code in [telemetry.py](https://github.com/jitsucom/jitsu-python-example/blob/main/jitsu_python_example/telemetry.py)


### Prerequisites

1. [telemetry.py](https://github.com/jitsucom/jitsu-python-example/blob/main/jitsu_python_example/telemetry.py) is using [Jitsu](https://jitsu.com) as a backend: [Deploy Jitsu](https://jitsu.com/docs/deployment) or signup for [Jitsu.Cloud](https://cloud.jitsu.com)
2. Create an API Key and a Destination (for [Cloud.Jitsu](https://cloud.jitsu.com) users we offer free demo Postgres destination) in Jitsu UI.
3. Put HTTP calls into `telemetry.py`


### Disabling Telemetry

This example allows to opt-out for tracking by setting `TELEMETRY_DISABLED` to `true`.

## About Jitsu

[Jitsu](https://jitsu.com) is an open-source data collection platform. 
