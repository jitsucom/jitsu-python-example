# Getting Started with Jitsu and python

This project shows how to track telemetry events with [Jitsu](https://jitsu) and python.

## How to use

Just send telemetry events via HTTP in:
- [setup.py](https://github.com/jitsucom/jitsu-python-example/blob/main/setup.py): event will be sent on every package install (when your library user executes `pip install <your library>`)
- [__init__.py](https://github.com/jitsucom/jitsu-python-example/blob/main/jitsu_python_example/__init__.py): event will be sent on every running instance (1 event per run)

### Steps

1. Create an account on [Cloud.Jitsu](https://cloud.jitsu.com) or [deploy Jitsu](https://jitsu.com/docs/deployment)
2. Create an API Key and a Destination (for [Cloud.Jitsu](https://cloud.jitsu.com) users we offer free demo Postgres destination) in Jitsu UI.
3. Put HTTP calls into setup.py and __init__.py
4. Analyze telemetry events in your Destination!

### HTTP example
```python
import requests
requests.post("https://t.jitsu.com/api/v1/s2s/event", params={'token': <YOUR_SERVER_API_KEY>}, json=payload, timeout=2)
```

## About Jitsu

[Jitsu](https://jitsu.com) is an open-source data collection platform. Our mission is to ensure that all your business data is consolidated in a
single database and ready for analysis.
