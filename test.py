import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="hornet",
    password="akali",
    dbname="weather_pipeline_ml",
    port=5432
)

print("Conectado com sucesso!")