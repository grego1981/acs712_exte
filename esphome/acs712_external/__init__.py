from esphome.components import sensor
from esphome import automation
import esphome.codegen as cg

acs712_ns = cg.esphome_ns.namespace('acs712_external')
ACS712Sensor = acs712_ns.class_('ACS712Sensor', cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema().extend(
    {
        # Add any configuration parameters here if needed
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
