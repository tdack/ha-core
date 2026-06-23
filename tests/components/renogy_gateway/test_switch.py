"""Tests for the Renogy Gateway switch platform."""

from unittest.mock import MagicMock

from homeassistant.components.renogy_gateway.switch import RenogySwitch
from homeassistant.core import HomeAssistant

from .conftest import FIELD_RELAY, MOCK_BOX_DEVICE


async def test_switch_turn_on_writes_true(
    hass: HomeAssistant,
    mock_coordinator,
) -> None:
    """Turn on calls coordinator.async_write with True."""
    switch = RenogySwitch(mock_coordinator, MOCK_BOX_DEVICE, FIELD_RELAY)
    switch.hass = hass

    await switch.async_turn_on()
    mock_coordinator.async_write.assert_awaited_once_with(FIELD_RELAY.sp, True)


async def test_switch_turn_off_writes_false(
    hass: HomeAssistant,
    mock_coordinator,
) -> None:
    """Turn off calls coordinator.async_write with False."""
    switch = RenogySwitch(mock_coordinator, MOCK_BOX_DEVICE, FIELD_RELAY)
    switch.hass = hass

    await switch.async_turn_off()
    mock_coordinator.async_write.assert_awaited_once_with(FIELD_RELAY.sp, False)


async def test_switch_state_from_telemetry(
    hass: HomeAssistant,
    mock_coordinator,
) -> None:
    """Switch is_on reflects telemetry push."""
    switch = RenogySwitch(mock_coordinator, MOCK_BOX_DEVICE, FIELD_RELAY)
    switch.hass = hass
    switch.async_write_ha_state = MagicMock()

    assert switch.is_on is None

    switch._handle_telemetry(True)
    assert switch.is_on is True

    switch._handle_telemetry(False)
    assert switch.is_on is False


async def test_switch_has_user_label(
    hass: HomeAssistant,
    mock_coordinator,
) -> None:
    """Switch name comes from user-assigned label."""
    switch = RenogySwitch(mock_coordinator, MOCK_BOX_DEVICE, FIELD_RELAY)
    assert switch.name == "Cooling Fan"


async def test_switch_seeds_value_from_coordinator_cache(
    hass: HomeAssistant,
    mock_coordinator,
) -> None:
    """A cached live value from the coordinator seeds is_on immediately."""
    mock_coordinator.get_value.return_value = True
    switch = RenogySwitch(mock_coordinator, MOCK_BOX_DEVICE, FIELD_RELAY)
    switch.hass = hass
    switch.entity_id = "switch.test_relay"
    switch.async_write_ha_state = MagicMock()

    await switch.async_added_to_hass()
    assert switch.is_on is True
