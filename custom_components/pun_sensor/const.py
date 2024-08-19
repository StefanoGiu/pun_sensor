

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
