
    async def async_step_step3(self, user_input=None):
        """Gestione prima configurazione da Home Assistant"""
        self.data.update(user_input)
        errors = {}
        data_schema = {
            vol.Required(CONF_ASOS_SC1, default=0.029809) : cv.positive_float,
            vol.Required(CONF_ASOS_SC2, default=0.029809) : cv.positive_float,
            vol.Required(CONF_ARIM_SC1, default=0.008828) : cv.positive_float,
            vol.Required(CONF_ARIM_SC2, default=0.008828) : cv.positive_float,
        }
        # Mostra la schermata di configurazione, con gli eventuali errori
        return self.async_show_form(
            step_id="step4", data_schema=vol.Schema(data_schema), errors=errors, 
        )

    async def async_step_step4(self, user_input=None):
        """Gestione prima configurazione da Home Assistant"""
        self.data.update(user_input)
        errors = {}
        data_schema = {
            vol.Required(CONF_ACCISA_TAX, default=0.022700) : cv.positive_float,
            vol.Required(CONF_IVA, default=10) : vol.All(cv.positive_int, vol.Range(min=0, max=100)),
            vol.Required(CONF_DISCOUNT, default=1) : cv.positive_float,
            vol.Required(CONF_TV_TAX, default=7) : cv.positive_float,
        }
        # Mostra la schermata di configurazione, con gli eventuali errori
        return self.async_show_form(
            step_id="step5", data_schema=vol.Schema(data_schema), errors=errors, 
        )

    async def async_step_step5(self, user_input=None):
        """Gestione prima configurazione da Home Assistant"""
        self.data.update(user_input)
        errors = {}
        data_schema = {
            vol.Required(CONF_MONTHY_ENTITY_SENSOR) : selector.selector({
				"entity": {
					"multiple": "false",
				    "filter": [{"domain" : "sensor", "device_class" : "energy"}],
				}
			}),
            vol.Required(CONF_SCAN_HOUR, default=1): vol.All(cv.positive_int, vol.Range(min=0, max=23)),
            vol.Optional(CONF_ACTUAL_DATA_ONLY, default=False): cv.boolean,
        }
        # Mostra la schermata di configurazione, con gli eventuali errori
        return self.async_show_form(
            step_id="step6", data_schema=vol.Schema(data_schema), errors=errors, 
        )

    async def async_step_step6(self, user_input=None):
        """Gestione prima configurazione da Home Assistant"""
        self.data.update(user_input)
        if user_input is not None:
            # Configurazione valida (validazione integrata nello schema)
            return self.async_create_entry(
                title='Bolletta',
                data=self.data
            )
