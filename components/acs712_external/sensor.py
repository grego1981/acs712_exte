import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_AMPERE, UNIT_WATT, ICON_FLASH, ICON_CURRENT_AC

DEPENDENCIES = []

acs712_ns = cg.esphome_ns.namespace("acs712_external")
ACS712Sensor = acs712_ns.class_("ACS712Sensor", cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ACS712Sensor),
    cv.Optional("current"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        icon=ICON_CURRENT_AC,
        accuracy_decimals=2,
    ),
    cv.Optional("power"): sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        icon=ICON_FLASH,
        accuracy_decimals=2,
    ),
})

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)
    # Add the ACS712 library
    cg.add_library("RobTillaart/ACS712", "0.3.10")
    if "current" in config:
        sens = await sensor.new_sensor(config["current"])
        cg.add(var.set_current_sensor(sens))  # ✅ Use set_current_sensor()

    if "power" in config:
        sens = await sensor.new_sensor(config["power"])
        cg.add(var.set_power_sensor(sens))  # ✅ Use set_power_sensor()
