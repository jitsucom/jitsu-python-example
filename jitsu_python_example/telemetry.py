# coding: utf-8

"""
    Telemetry

    Jitsu (jitsu.com) is an open-source data collection platform. It can write data to data-warehouse of your choice.
    You need just send events from python library via HTTP.
"""
import requests
import os
import platform


class JitsuApi:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = 's2s.gpon6lmpwquappfl07tuq.s9fiig3ifreqz3br6mdf6h'  # Your Jitsu server API key here
        self.api_key = api_key
        # It is a OS env flag for disabling Telemetry
        self.disabled = os.environ.get('TELEMETRY_DISABLED', 'false') == 'true'
        # Specify any parameters and pass them to request body
        self.os_platform = platform.system()
        self.os_version = platform.release()
        self.os_machine = platform.machine()

    def send_event(self, payload: dict = None):
        """send_event

        Send telemetry event to Jitsu with information about OS and machine architecture with 2 seconds timeout
        ignore errors

        :param payload dict with telemetry data
        """
        if self.disabled is not True:
            payload['parsed_ua'] = {'os_version': self.os_version, 'os_family': self.os_platform,
                                    'os_machine': self.os_machine}
            try:
                requests.post("https://t.jitsu.com/api/v1/s2s/event", params={'token': self.api_key}, json=payload,
                              timeout=2)
            except:
                pass
