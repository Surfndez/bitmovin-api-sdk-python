# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PresetConfiguration(Enum):
    LIVE_ULTRAHIGH_QUALITY = "LIVE_ULTRAHIGH_QUALITY"
    LIVE_VERYHIGH_QUALITY = "LIVE_VERYHIGH_QUALITY"
    LIVE_HIGH_QUALITY = "LIVE_HIGH_QUALITY"
    LIVE_STANDARD = "LIVE_STANDARD"
    LIVE_LOW_LATENCY = "LIVE_LOW_LATENCY"
    LIVE_LOWER_LATENCY = "LIVE_LOWER_LATENCY"
    LIVE_VERYLOW_LATENCY = "LIVE_VERYLOW_LATENCY"
    VOD_HIGH_QUALITY = "VOD_HIGH_QUALITY"
    VOD_QUALITY = "VOD_QUALITY"
    VOD_STANDARD = "VOD_STANDARD"
    VOD_SPEED = "VOD_SPEED"
    VOD_HIGH_SPEED = "VOD_HIGH_SPEED"
    VOD_VERYHIGH_SPEED = "VOD_VERYHIGH_SPEED"
    VOD_EXTRAHIGH_SPEED = "VOD_EXTRAHIGH_SPEED"
    VOD_SUPERHIGH_SPEED = "VOD_SUPERHIGH_SPEED"
    VOD_ULTRAHIGH_SPEED = "VOD_ULTRAHIGH_SPEED"
