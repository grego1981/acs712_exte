#pragma once

#include "esphome.h"
#include "ACS712.h"

namespace esphome {
namespace acs712_external {

class ACS712Sensor : public PollingComponent, public sensor::Sensor {
   public:
    ACS712Sensor() : PollingComponent(15000) {}

    void setup() override;
    void update() override;

    sensor::Sensor *current_sensor = new sensor::Sensor();
    sensor::Sensor *power_sensor = new sensor::Sensor();

   private:
    ACS712 *ACS = new ACS712(A0, 5, 1023, 100);
};

}  // namespace acs712_external
}  // namespace esphome
