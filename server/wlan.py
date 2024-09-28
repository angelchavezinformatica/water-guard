import network

import environ as env

WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(env.WLAN_SSID, env.WLAN_PASSWORD)
