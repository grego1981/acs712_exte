#pragma once

#include "esphome/core/component.h"  // Core ESPHome component features
#include "esphome/components/sensor/sensor.h"  // Sensor class
#include "ACS712.h"

namespace esphome {
namespace acs712_external {

class ACS712Sensor : public PollingComponent {
   public:
    ACS712Sensor() : PollingComponent(15000) {}

    void setup() override;
    void update() override;

    sensor::Sensor *current_sensor = new sensor::Sensor();  // Correct sensor class
    sensor::Sensor *power_sensor = new sensor::Sensor();  // Correct sensor class

   private:
    ACS712 *ACS = new ACS712(A0, 5, 1023, 100);
};

}  // namespace acs712_external
}  // namespace esphome
