import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_BATTERY_VOLTAGE,
    CONF_BUS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_FREQUENCY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_ENERGY,
    ICON_CURRENT_AC,
    STATE_CLASS_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_HERTZ,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_VOLT_AMPS,
    UNIT_WATT,
    STATE_CLASS_TOTAL_INCREASING, 
)

from .. import CONF_PIPSOLAR_ID, PIPSOLAR_COMPONENT_SCHEMA

DEPENDENCIES = ["uart"]

UNIT_KILOWATT_HOUR = "kWh"

# HGEN sensors
CONF_PV_GEN_CURRENT_DAY = "pv_gen_current_day"
CONF_PV_GEN_CURRENT_MONTH = "pv_gen_current_month"
CONF_PV_GEN_CURRENT_YEAR = "pv_gen_current_year"
CONF_PV_GEN_TOTAL = "pv_gen_total"

# QPIRI sensors
CONF_GRID_RATING_VOLTAGE = "grid_rating_voltage"
CONF_GRID_RATING_CURRENT = "grid_rating_current"
CONF_AC_OUTPUT_RATING_VOLTAGE = "ac_output_rating_voltage"
CONF_AC_OUTPUT_RATING_FREQUENCY = "ac_output_rating_frequency"
CONF_AC_OUTPUT_RATING_CURRENT = "ac_output_rating_current"
CONF_AC_OUTPUT_RATING_APPARENT_POWER = "ac_output_rating_apparent_power"
CONF_AC_OUTPUT_RATING_ACTIVE_POWER = "ac_output_rating_active_power"
CONF_BATTERY_RATING_VOLTAGE = "battery_rating_voltage"
CONF_BATTERY_RECHARGE_VOLTAGE = "battery_recharge_voltage"
CONF_BATTERY_UNDER_VOLTAGE = "battery_under_voltage"
CONF_BATTERY_BULK_VOLTAGE = "battery_bulk_voltage"
CONF_BATTERY_FLOAT_VOLTAGE = "battery_float_voltage"
CONF_BATTERY_TYPE = "battery_type"
CONF_CURRENT_MAX_AC_CHARGING_CURRENT = "current_max_ac_charging_current"
CONF_CURRENT_MAX_CHARGING_CURRENT = "current_max_charging_current"
CONF_INPUT_VOLTAGE_RANGE = "input_voltage_range"
CONF_OUTPUT_SOURCE_PRIORITY = "output_source_priority"
CONF_CHARGER_SOURCE_PRIORITY = "charger_source_priority"
CONF_PARALLEL_MAX_NUM = "parallel_max_num"
CONF_MACHINE_TYPE = "machine_type"
CONF_TOPOLOGY = "topology"
CONF_OUTPUT_MODE = "output_mode"
CONF_BATTERY_REDISCHARGE_VOLTAGE = "battery_redischarge_voltage"
CONF_PV_OK_CONDITION_FOR_PARALLEL = "pv_ok_condition_for_parallel"
CONF_PV_POWER_BALANCE = "pv_power_balance"

# QPIGS sensors

CONF_GRID_VOLTAGE = "grid_voltage"
CONF_GRID_FREQUENCY = "grid_frequency"
CONF_AC_OUTPUT_VOLTAGE = "ac_output_voltage"
CONF_AC_OUTPUT_FREQUENCY = "ac_output_frequency"
CONF_AC_OUTPUT_APPARENT_POWER = "ac_output_apparent_power"
CONF_AC_OUTPUT_ACTIVE_POWER = "ac_output_active_power"
CONF_OUTPUT_LOAD_PERCENT = "output_load_percent"
CONF_BATTERY_CHARGING_CURRENT = "battery_charging_current"
CONF_BATTERY_CAPACITY_PERCENT = "battery_capacity_percent"
CONF_INVERTER_HEAT_SINK_TEMPERATURE = "inverter_heat_sink_temperature"
CONF_PV1_INPUT_CURRENT = "pv1_input_current"
CONF_PV1_INPUT_VOLTAGE = "pv1_input_voltage"
CONF_BATTERY_VOLTAGE_SCC = "battery_voltage_scc"
CONF_BATTERY_DISCHARGE_CURRENT = "battery_discharge_current"
CONF_ADD_SBU_PRIORITY_VERSION = "add_sbu_priority_version"
CONF_CONFIGURATION_STATUS = "configuration_status"
CONF_SCC_FIRMWARE_VERSION = "scc_firmware_version"
CONF_BATTERY_VOLTAGE_OFFSET_FOR_FANS_ON = "battery_voltage_offset_for_fans_on"
CONF_EEPROM_VERSION = "eeprom_version"
CONF_PV1_CHARGING_POWER = "pv1_charging_power"

# QPIGS2 sensors

CONF_PV2_INPUT_CURRENT = "pv2_input_current"
CONF_PV2_INPUT_VOLTAGE = "pv2_input_voltage"
CONF_PV2_CHARGING_POWER = "pv2_charging_power"


TYPES = {
    CONF_PV_GEN_CURRENT_DAY: sensor.sensor_schema(
        unit_of_measurement="kWh",
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_PV_GEN_CURRENT_MONTH: sensor.sensor_schema(
        unit_of_measurement="kWh",
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_PV_GEN_CURRENT_YEAR: sensor.sensor_schema(
        unit_of_measurement="kWh",
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_PV_GEN_TOTAL: sensor.sensor_schema(
        unit_of_measurement="kWh",
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    CONF_GRID_RATING_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_GRID_RATING_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_RATING_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_RATING_FREQUENCY: sensor.sensor_schema(
        unit_of_measurement=UNIT_HERTZ,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_FREQUENCY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_RATING_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_RATING_APPARENT_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT_AMPS,
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_RATING_ACTIVE_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_RATING_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_RECHARGE_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_UNDER_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_BULK_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_FLOAT_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_TYPE: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_CURRENT_MAX_AC_CHARGING_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_CURRENT,
    ),
    CONF_CURRENT_MAX_CHARGING_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_CURRENT,
    ),
    CONF_INPUT_VOLTAGE_RANGE: sensor.sensor_schema(
        accuracy_decimals=1,
    ),
    CONF_OUTPUT_SOURCE_PRIORITY: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_CHARGER_SOURCE_PRIORITY: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_PARALLEL_MAX_NUM: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_MACHINE_TYPE: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_TOPOLOGY: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_OUTPUT_MODE: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_BATTERY_REDISCHARGE_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_PV_OK_CONDITION_FOR_PARALLEL: sensor.sensor_schema(
        accuracy_decimals=1,
    ),
    CONF_PV_POWER_BALANCE: sensor.sensor_schema(
        accuracy_decimals=1,
    ),
    CONF_GRID_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_GRID_FREQUENCY: sensor.sensor_schema(
        unit_of_measurement=UNIT_HERTZ,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_FREQUENCY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_FREQUENCY: sensor.sensor_schema(
        unit_of_measurement=UNIT_HERTZ,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_FREQUENCY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_APPARENT_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT_AMPS,
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_AC_OUTPUT_ACTIVE_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_OUTPUT_LOAD_PERCENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BUS_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_CHARGING_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_CAPACITY_PERCENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_INVERTER_HEAT_SINK_TEMPERATURE: sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_PV1_INPUT_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_PV1_INPUT_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_VOLTAGE_SCC: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_DISCHARGE_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_BATTERY_VOLTAGE_OFFSET_FOR_FANS_ON: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_EEPROM_VERSION: sensor.sensor_schema(
        accuracy_decimals=1,
    ),
    CONF_PV1_CHARGING_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_PV2_INPUT_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_PV2_INPUT_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_PV2_CHARGING_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    # QET / QLT
    "total_pv_generated_energy": sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOUR,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    "total_output_load_energy": sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOUR,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
    ),
    # Q1
    "time_until_absorb_charging": sensor.sensor_schema(accuracy_decimals=0),
    "time_until_float_charging": sensor.sensor_schema(accuracy_decimals=0),
    "charge_average_current": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
    "scc_pwm_temperature": sensor.sensor_schema(unit_of_measurement=UNIT_CELSIUS, accuracy_decimals=1, device_class=DEVICE_CLASS_TEMPERATURE),
    "inverter_temperature": sensor.sensor_schema(unit_of_measurement=UNIT_CELSIUS, accuracy_decimals=1, device_class=DEVICE_CLASS_TEMPERATURE),
    "battery_temperature": sensor.sensor_schema(unit_of_measurement=UNIT_CELSIUS, accuracy_decimals=1, device_class=DEVICE_CLASS_TEMPERATURE),
    "transformer_temperature": sensor.sensor_schema(unit_of_measurement=UNIT_CELSIUS, accuracy_decimals=1, device_class=DEVICE_CLASS_TEMPERATURE),
    "fan_pwm_speed": sensor.sensor_schema(accuracy_decimals=0),
    "scc_charge_power": sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER),
    "sync_frequency": sensor.sensor_schema(unit_of_measurement=UNIT_HERTZ, accuracy_decimals=1, device_class=DEVICE_CLASS_FREQUENCY),
    # QPGS0
    "serial_number_0": sensor.sensor_schema(accuracy_decimals=0),
    "fault_code_0": sensor.sensor_schema(accuracy_decimals=0),
    "grid_voltage_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=1, device_class=DEVICE_CLASS_VOLTAGE),
    "grid_frequency_0": sensor.sensor_schema(unit_of_measurement=UNIT_HERTZ, accuracy_decimals=1, device_class=DEVICE_CLASS_FREQUENCY),
    "ac_output_voltage_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=1, device_class=DEVICE_CLASS_VOLTAGE),
    "ac_output_frequency_0": sensor.sensor_schema(unit_of_measurement=UNIT_HERTZ, accuracy_decimals=1, device_class=DEVICE_CLASS_FREQUENCY),
    "ac_output_apparent_power_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT_AMPS, accuracy_decimals=1),
    "ac_output_active_power_0": sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER),
    "load_percent_0": sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=1),
    "battery_voltage_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=1, device_class=DEVICE_CLASS_VOLTAGE),
    "battery_charging_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
    "battery_capacity_0": sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=0),
    "pv1_input_voltage_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=1, device_class=DEVICE_CLASS_VOLTAGE),
    "total_charging_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
    "total_ac_output_apparent_power_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT_AMPS, accuracy_decimals=1),
    "total_output_active_power_0": sensor.sensor_schema(unit_of_measurement=UNIT_WATT, accuracy_decimals=1, device_class=DEVICE_CLASS_POWER),
    "total_ac_output_percentage_0": sensor.sensor_schema(unit_of_measurement=UNIT_PERCENT, accuracy_decimals=1),
    "inverter_status_battery_0": sensor.sensor_schema(accuracy_decimals=0),
    "output_mode_0": sensor.sensor_schema(accuracy_decimals=0),
    "charger_source_priority_0": sensor.sensor_schema(accuracy_decimals=0),
    "max_charger_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=0, device_class=DEVICE_CLASS_CURRENT),
    "max_charger_range_0": sensor.sensor_schema(accuracy_decimals=0),
    "max_ac_charger_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=0, device_class=DEVICE_CLASS_CURRENT),
    "pv1_input_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
    "battery_discharge_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
    "pv2_input_voltage_0": sensor.sensor_schema(unit_of_measurement=UNIT_VOLT, accuracy_decimals=1, device_class=DEVICE_CLASS_VOLTAGE),
    "pv2_input_current_0": sensor.sensor_schema(unit_of_measurement=UNIT_AMPERE, accuracy_decimals=1, device_class=DEVICE_CLASS_CURRENT),
}

CONFIG_SCHEMA = PIPSOLAR_COMPONENT_SCHEMA.extend(
    {cv.Optional(type): schema for type, schema in TYPES.items()}
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_PIPSOLAR_ID])

    for type, _ in TYPES.items():
        if type in config:
            conf = config[type]
            sens = await sensor.new_sensor(conf)
            cg.add(getattr(paren, f"set_{type}")(sens))
