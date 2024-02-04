"""Mycroft AI notification platform."""
from __future__ import annotations

import logging

from mycroft_bus_client import MessageBusClient, Message

from homeassistant.components.notify import BaseNotificationService
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> MycroftNotificationService:
    """Get the Mycroft notification service."""
    return MycroftNotificationService(hass.data["mycroft"])


class MycroftNotificationService(BaseNotificationService):
    """The Mycroft Notification Service."""

    def __init__(self, mycroft_ip):
        """Initialize the service."""
        self.mycroft_ip = mycroft_ip
        self.bus = MessageBusClient(host=self.mycroft_ip)
        self.bus.run_in_thread()

    def send_message(self, message="", **kwargs):
        """Send a message mycroft to speak on instance."""

        if self.bus is not None:
            self.bus.emit(Message('speak', data={'utterance': message}))
        else:
            _LOGGER.log("Could not reach this instance of mycroft")
