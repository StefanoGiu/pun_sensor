from enum import StrEnum

# Dominio HomeAssistant
DOMAIN = "pun_sensor"

# Tipi di sensore da creare
PUN_FASCIA_MONO = 0
PUN_FASCIA_F1 = 1
PUN_FASCIA_F2 = 2
PUN_FASCIA_F3 = 3
PUN_FASCIA_F23 = 4

PUN_FASCIA_MONO_MP = 5
PUN_FASCIA_F1_MP = 6
PUN_FASCIA_F2_MP = 7
PUN_FASCIA_F3_MP = 8
PUN_FASCIA_F23_MP = 9

BILL_ENERGY_FIX_QUOTE = 10
BILL_ENERGY_ENERGY_QUOTE = 11
BILL_TRANSPORT_FIX_QUOTE = 12
BILL_TRANSPORT_POWER_QUOTE = 13
BILL_TRANSPORT_ENERGY_QUOTE = 14
BILL_ASOS_ARIM_QUOTE = 15
BILL_ACCISA_TAX = 16
BILL_IVA = 17
BILL_TOTAL = 18

# Tipi di aggiornamento
COORD_EVENT = "coordinator_event"
EVENT_UPDATE_FASCIA = "event_update_fascia"
EVENT_UPDATE_PUN = "event_update_pun"

# Parametri configurabili da configuration.yaml
CONF_SCAN_HOUR = "scan_hour"
CONF_ACTUAL_DATA_ONLY = "actual_data_only"
CONF_FIX_QUOTA_AGGR_MEASURE = "fix_quota_aggr_measure"
CONF_MONTHLY_FEE = "monthly_fee"
CONF_TARIFF_TYPE = "tariff_type"
CONF_NW_LOSS_PERCENTAGE = "nw_loss_percentage"
CONF_OTHER_FEE = "other_fee"
CONF_FIX_QUOTA_TRANSPORT = "fix_quota_transport"
CONF_QUOTA_POWER = "quota_power"
CONF_POWER_IN_USE = "power_in_use"
CONF_ENERGY_SC1 = "energy_sc1"
CONF_ASOS_SC1 = "asos_sc1"
CONF_ASOS_SC2 = "asos_sc2"
CONF_ARIM_SC1 = "arim_sc1"
CONF_ARIM_SC2 = "arim_sc2"
CONF_ACCISA_TAX = "accisa_tax"
CONF_IVA = "iva"
CONF_DISCOUNT = "discount"
CONF_TV_TAX = "tv_tax"
CONF_MONTHY_ENTITY_SENSOR = "monthly_entity_sensor"

class TARIFF_TYPES(StrEnum):
    tariff_mono = "tariff_mono"
    tariff_bi = "tariff_bi"
    tariff_tri = "tariff_tri"
