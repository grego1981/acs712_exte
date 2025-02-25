#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "ACS712.h"

namespace esphome {
namespace acs712_external {

class ACS712Sensor : public PollingComponent {
   public:
    ACS712Sensor() : PollingComponent(15000) {}

    void setup() override;
    void update() override;

    // ✅ Declare setter functions correctly
    void set_current_sensor(sensor::Sensor *sensor) { this->current_sensor = sensor; }
    void set_power_sensor(sensor::Sensor *sensor) { this->power_sensor = sensor; }

   private:
    sensor::Sensor *current_sensor = nullptr;  // ✅ Initialize to nullptr
    sensor::Sensor *power_sensor = nullptr;
    ACS712 *ACS = new ACS712(A0, 5, 1023, 100);
};

}  // namespace acs712_external
}  // namespace esphome
