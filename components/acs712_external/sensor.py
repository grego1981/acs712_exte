import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    UNIT_AMPERE,
    ICON_CURRENT_AC,
    CONF_ID,
)

DEPENDENCIES = []

acs712_ns = cg.esphome_ns.namespace('acs712_external')
ACS712Sensor = acs712_ns.class_('ACS712Sensor', cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = sensor.sensor_schema(
    ACS712Sensor, unit_of_measurement=UNIT_AMPERE, icon=ICON_CURRENT_AC, accuracy_decimals=2).extend(cv.polling_component_schema('60s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    cg.add_library("RobTillaart/ACS712", "0.3.10")
