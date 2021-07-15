# coding: utf-8

"""
    Telemetry

    Jitsu (jitsu.com) is an open-source data collection platform. It can write data to data-warehouse of your choice.
    You need just send events from python library via HTTP.
"""
import requests
import os
import platform

def send_usage_event(payload: dict = None):
    jitsu_api_key = 's2s.gpon6lmpwquappfl07tuq.s9fiig3ifreqz3br6mdf6h'  # Your Jitsu server API key here
    if os.environ.get('TELEMETRY_DISABLED', 'false') == 'true':
        return

    if payload is None:
        payload = {}

    payload['parsed_ua'] = {'os_version': platform.release(), 'os_family': platform.system(), 'os_machine': platform.machine()}
    try:
        requests.post("https://t.jitsu.com/api/v1/s2s/event", params={'token': jitsu_api_key}, json=payload, timeout=2)
    except:
        pass