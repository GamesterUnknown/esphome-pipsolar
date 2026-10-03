import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor

from .. import CONF_PIPSOLAR_ID, PIPSOLAR_COMPONENT_SCHEMA

DEPENDENCIES = ["uart"]

CONF_DEVICE_MODE = "device_mode"
CONF_LAST_QPIGS = "last_qpigs"
CONF_LAST_QPIGS2 = "last_qpigs2"
CONF_LAST_QPIRI = "last_qpiri"
CONF_LAST_QMOD = "last_qmod"
CONF_LAST_QFLAG = "last_qflag"
CONF_LAST_QPIWS = "last_qpiws"
CONF_LAST_QT = "last_qt"
CONF_LAST_QMN = "last_qmn"
CONF_LAST_QBATCD = "last_qbatcd"
CONF_CUSTOM_COMMAND = "last_custom_command"
CONF_CURRENT_DATA_TIME = "current_data_time"
CONF_LAST_HGEN = "last_hgen"
CONF_LAST_HGRID = "last_hgrid"
CONF_LAST_HOP = "last_hop"
CONF_LAST_HPV = "last_hpv"
CONF_LAST_HBAT = "last_hbat"
CONF_LAST_HTEMP = "last_htemp"
CONF_LAST_HIMSG1 = "last_himsg1"
CONF_HIMSG1_FIRMWARE_VERSION = "himsg1_firmware_version"
CONF_HIMSG1_MANUFACTURE_DATE = "himsg1_manufacture_date"
CONF_LAST_HEEP1 = "last_heep1"
CONF_LAST_HSTS = "last_hsts"
CONF_HSTS_FLAGS1 = "hsts_flags1"
CONF_HSTS_FLAGS2 = "hsts_flags2"
CONF_LAST_QPRTL = "last_qprtl"
CONF_QPRTL_PROTOCOL_ID = "qprtl_protocol_id"
CONF_LAST_HBMS1 = "last_hbms1"
CONF_LAST_HBMS2 = "last_hbms2"
CONF_LAST_HBMS3 = "last_hbms3"
CONF_LAST_HEEP2 = "last_heep2"
CONF_LAST_HPVB = "last_hpvb"
CONF_INVERTER_DATE = "inverter_date"
CONF_INVERTER_TIME = "inverter_time"
CONF_LAST_QPGS0 = "last_qpgs0"
CONF_LAST_QET = "last_qet"
CONF_LAST_QLT = "last_qlt"
CONF_LAST_QMCHGCR = "last_qmchgcr"
CONF_LAST_QMUCHGCR = "last_qmuchgcr"
CONF_LAST_Q1 = "last_q1"
CONF_LAST_QBMS = "last_qbms"
CONF_WORK_MODE_0 = "work_mode_0"
CONF_INVERTER_CHARGE_STATUS = "inverter_charge_status"

TYPES = [
    CONF_DEVICE_MODE,
    CONF_LAST_QPIGS,
    CONF_LAST_QPIGS2,
    CONF_LAST_QPIRI,
    CONF_LAST_QMOD,
    CONF_LAST_QFLAG,
    CONF_LAST_QPIWS,
    CONF_LAST_QT,
    CONF_LAST_QMN,
    CONF_LAST_QBATCD,
#    CONF_LAST_MUCHGC,
#    CONF_LAST_MCHGC,
    CONF_CUSTOM_COMMAND,
    CONF_CURRENT_DATA_TIME,
    CONF_LAST_HGEN,
    CONF_LAST_HGRID,
    CONF_LAST_HOP,
    CONF_LAST_HPV,
    CONF_LAST_HBAT,
    CONF_LAST_HTEMP,
    CONF_LAST_HIMSG1,
    CONF_HIMSG1_FIRMWARE_VERSION,
    CONF_HIMSG1_MANUFACTURE_DATE,
    CONF_LAST_HEEP1,
    CONF_LAST_HSTS,
    CONF_HSTS_FLAGS1,
    CONF_HSTS_FLAGS2,
    CONF_LAST_QPRTL,
    CONF_QPRTL_PROTOCOL_ID,
    CONF_LAST_HBMS1,
    CONF_LAST_HBMS2,
    CONF_LAST_HBMS3,
    CONF_LAST_HEEP2,
    CONF_LAST_HPVB,
    CONF_INVERTER_DATE,
    CONF_INVERTER_TIME,
    CONF_LAST_QPGS0,
    CONF_LAST_QET,
    CONF_LAST_QLT,
    CONF_LAST_QMCHGCR,
    CONF_LAST_QMUCHGCR,
    CONF_LAST_Q1,
    CONF_LAST_QBMS,
    CONF_WORK_MODE_0,
    CONF_INVERTER_CHARGE_STATUS,
]

CONFIG_SCHEMA = PIPSOLAR_COMPONENT_SCHEMA.extend(
    {cv.Optional(type): text_sensor.text_sensor_schema() for type in TYPES}
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_PIPSOLAR_ID])

    for type in TYPES:
        if type in config:
            conf = config[type]
            var = await text_sensor.new_text_sensor(conf)
            cg.add(getattr(paren, f"set_{type}")(var))
