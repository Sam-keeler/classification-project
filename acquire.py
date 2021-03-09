def get_telco_data(host = host, user = user, password = password):
    db = 'telco_churn'
    return pd.read_sql('SELECT * FROM customers JOIN internet_service_types ON (customers.internet_service_type_id = internet_service_types.internet_service_type_id)', f'mysql+pymysql://{user}:{password}@{host}/{db}')

telco = get_telco_data()