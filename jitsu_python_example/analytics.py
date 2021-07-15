# coding: utf-8

"""
    Analytics

    Jitsu (jitsu.com) allows to send analytics events python library analytics and writes it to data-warehouse of your choice.
"""
import httpx
import os


class JitsuApi:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = 's2s.gpon6lmpwquappfl07tuq.s9fiig3ifreqz3br6mdf6h'
        self.api_key = api_key
        self.disabled = os.environ.get('TELEMETRY_DISABLED', 'false') == 'true'

    def send_event(self, payload: dict = None):
        """send_event

        Send analytics event to Jitsu asynchronously

        :param payload dict analytics data
        """
        if self.disabled is not True:
            client = httpx.AsyncClient()
            client.post(url="https://t.jitsu.com/api/v1/s2s/event", params={'token': self.api_key}, json=payload)

        return
