# (generated with --quick)

from typing import Any, Coroutine

async_fire_mqtt_message: Any
async_mock_mqtt_component: Any
async_subscribe_topics: Any
async_unsubscribe_topics: Any
callback: Any
mock: module

def test_modify_topics(hass, mqtt_mock, caplog) -> Coroutine[Any, Any, None]: ...
def test_no_change(hass, mqtt_mock, caplog) -> Coroutine[Any, Any, None]: ...
def test_qos_encoding_custom(hass, mqtt_mock, caplog) -> Coroutine[Any, Any, None]: ...
def test_qos_encoding_default(hass, mqtt_mock, caplog) -> Coroutine[Any, Any, None]: ...
def test_subscribe_topics(hass, mqtt_mock, caplog) -> Coroutine[Any, Any, None]: ...
