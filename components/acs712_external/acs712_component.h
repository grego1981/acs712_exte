#pragma once

#include "esphome.h"
#include "ACS712.h"

namespace esphome {
namespace acs712_external {

class ACS712Sensor : public PollingComponent, public sensor {
   public:
    ACS712Sensor() : PollingComponent(15000) {}

    void setup() override;
    void update() override;

    Sensor *current_sensor = new sensor();
    Sensor *power_sensor = new sensor();

   private:
    ACS712 *ACS = new ACS712(A0, 5, 1023, 100);
};

}  // namespace acs712_external
}  // namespace esphome
