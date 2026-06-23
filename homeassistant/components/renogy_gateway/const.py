"""Constants for the Renogy Gateway integration."""

import logging

DOMAIN = "renogy_gateway"

CONF_GATEWAY_ID = "gateway_id"
CONF_GATEWAY_NAME = "gateway_name"

# Token keys stored in config entry data
CONF_REFRESH_TOKEN = "refresh_token"
CONF_RTM_TOKEN = "rtm_token"
CONF_RTM_DID = "rtm_did"
CONF_DEVICE_UUID = "device_uuid"

RTM_RECONNECT_DELAY_MIN = 2  # seconds
RTM_RECONNECT_DELAY_MAX = 30  # seconds

LOGGER = logging.getLogger(__name__)
