
from jitsu_python_example.telemetry import send_usage_event

# JitsuApi sends usage event on every running instance
send_usage_event({'event_type': 'module_initi'})
