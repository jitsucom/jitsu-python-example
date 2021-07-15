"""Top-level package for jitsu-python-example."""

__author__ = """Vladimir Klimontovich"""
__email__ = 'hello@jitsu.com'
__version__ = '0.0.1'

from jitsu_python_example.analytics import JitsuApi

jitsuApi = JitsuApi()
jitsuApi.send_event({
    'event_type': 'python'
})
