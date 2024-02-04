# The problem

The notification component for mycroft has been [disabled since Apr 27, 2023](https://github.com/home-assistant/core/commit/cdbffee7814380b10952f9ac7f8a1e6bc6e93861)
The component was depending on a really old abandoned project that was causing problems. See: [thread on mycroftapi==2.0 issue](https://github.com/pypa/pip/issues/10788#issuecomment-1012591304)

# The solution

This version of the component uses the MessageBusClient from [mycroft-messagebus-client>=0.9.4](https://github.com/MycroftAI/mycroft-messagebus-client) instead and allows for relaxing the requirements for the websocket-client version.

mycroft-messagebus-client>=0.9.4 depends on websocket-client>=0.54.0 and pyee==8.1.0 which is almost four years old now.

AFAIK, the pyee dependency is not causing problems yet, but we shall see.

# Issues

Report an issue, if you find a problem.

# Setup

1. Clone this repository
2. Copy the ```mycroft``` directory into the ```custom_components``` directory in your homeassistant ```config``` directory (the directory where the configuration.yaml file is)
3. Keep sending those notifications to your mycroft instance

# Configuration

If you have already configured the mycroft notification core component which was disabled, you will need no further configuration as this component is a drop in replacement for the core component. If you're setting up mycroft notifications for the first time, add this to your Home Assistant configuration.yaml:

```yaml
# Example configuration.yaml entry
mycroft:
  host: 0.0.0.0
```

Also add the mycroft platform under the notify section to enable notifications

```yaml
# Example configuration.yaml entry
notify:
  - platform: mycroft
    name: mycroft
```

# Licence

- Apache 2.0
