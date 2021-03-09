def clean_telco(telco):
    telco.loc[(telco.phone_service == 'Yes') & (telco.multiple_lines == 'Yes'), 'phone_service'] = 'Multiple'
    telco.loc[(telco.phone_service == 'Yes') & (telco.multiple_lines == 'No'), 'phone_service'] = 'One'
    telco.loc[(telco.phone_service == 'No') & (telco.multiple_lines == 'No phone service'), 'phone_service'] = 'None'
    telco.loc[(telco.partner == 'No') & (telco.dependents == 'Yes'), 'partner'] = 'single family'
    telco.loc[(telco.partner == 'Yes') & (telco.dependents == 'Yes'), 'partner'] = 'partnered family'
    telco.loc[(telco.partner == 'Yes') & (telco.dependents == 'No'), 'partner'] = 'partnered'
    telco.loc[(telco.partner == 'No') & (telco.dependents == 'No'), 'partner'] = 'single'
    telco.loc[(telco.streaming_tv == 'No') & (telco.streaming_movies == 'No'), 'streaming_tv'] = 'None'
    telco.loc[(telco.streaming_tv == 'Yes') & (telco.streaming_movies == 'No'), 'streaming_tv'] = 'tv'
    telco.loc[(telco.streaming_tv == 'No') & (telco.streaming_movies == 'Yes'), 'streaming_tv'] = 'movies'
    telco.loc[(telco.streaming_tv == 'Yes') & (telco.streaming_movies == 'Yes'), 'streaming_tv'] = 'both'
    telco.loc[(telco.online_security == 'Yes') & (telco.online_backup == 'Yes'), 'online_security'] = 'both'
    telco.loc[(telco.online_security == 'No') & (telco.online_backup == 'Yes'), 'online_security'] = 'backup'
    telco.loc[(telco.online_security == 'Yes') & (telco.online_backup == 'No'), 'online_security'] = 'security'
    telco.loc[(telco.online_security == 'No') & (telco.online_backup == 'No'), 'online_security'] = 'None'
    telco.rename(columns={"phone_service": "phone_lines", 'online_security': 'online_services', 
                      "partner": "fam_status", 'streaming_tv': 'streaming', 'gender': 'is_female'}, inplace = True)
    telco.drop(columns = ['internet_service_type_id', 'multiple_lines', 'device_protection',
                          'dependents', 'streaming_movies', 'online_backup'], inplace = True)
    telco['years_held'] = round((telco['tenure'] / 12), 2)
    telco['churn'] = telco.churn.replace({'Yes': 1, 'No': 0})
    telco['is_female'] = telco.is_female.replace({'Female': 1, 'Male': 0})
    telco['paperless_billing'] = telco.paperless_billing.replace({'Yes': 1, 'No': 0})
    telco.total_charges = pd.to_numeric(telco.total_charges, errors='coerce').astype('float64')
    telco.total_charges = telco.total_charges.fillna(value=0)

    def modeling_telco(telco):
    model_telco = telco
    dummies_fam = pd.get_dummies(telco[['fam_status']], drop_first = True)
    dummies_phone_lines = pd.get_dummies(telco[['phone_lines']], drop_first = True)
    dummies_online_services = pd.get_dummies(telco[['online_services']], drop_first = True)
    dummies_tech_support = pd.get_dummies(telco[['tech_support']], drop_first = True)
    dummies_streaming = pd.get_dummies(telco[['streaming']], drop_first = True)
    dummies_internet_service_type = pd.get_dummies(telco[['internet_service_type']], drop_first = True)

    model_telco.drop(columns = ['fam_status', 'phone_lines', 'online_services', 'tech_support',
                                'streaming', 'internet_service_type', 'customer_id'], inplace = True)
    model_telco = pd.concat([model_telco, dummies_fam, dummies_phone_lines, dummies_online_services,
                             dummies_tech_support, dummies_streaming, dummies_internet_service_type], axis=1)
    return model_telco