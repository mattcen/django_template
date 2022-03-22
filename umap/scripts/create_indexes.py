import psycopg2
from os import environ as env

POSTGRES_HOST = env.get('POSTGRES_HOST', 'localhost')
POSTGRES_PASSWORD = env.get('POSTGRES_PASSWORD', 'password')
POSTGRES_PORT = env.get('POSTGRES_PORT', '5432')
POSTGRES_USER = env.get('POSTGRES_USER', 'postgres')
POSTGRES_DB = env.get('POSTGRES_DB', 'postgres')
UMAP_LEAFLET_LONGITUDE = int(env.get('UMAP_LEAFLET_LONGITUDE', 2))
UMAP_LEAFLET_LATITUDE = int(env.get('UMAP_LEAFLET_LATITUDE', 51))

start_coords = f'SRID=4326;POINT({UMAP_LEAFLET_LONGITUDE} {UMAP_LEAFLET_LATITUDE})'



with psycopg2.connect(host=POSTGRES_HOST,
                      port=POSTGRES_PORT,
                      database=POSTGRES_DB,
                      user=POSTGRES_USER,
                      password=POSTGRES_PASSWORD) as conn:
    with conn.cursor() as curs:
        curs.execute('CREATE EXTENSION IF NOT EXISTS unaccent;')
        curs.execute('CREATE EXTENSION IF NOT EXISTS btree_gin;')
        curs.execute('ALTER FUNCTION unaccent(text) IMMUTABLE;')
        curs.execute('ALTER FUNCTION to_tsvector(text) IMMUTABLE;')
        curs.execute('''CREATE INDEX search_idx ON umap_map
                        USING gin(to_tsvector(unaccent(name)), share_status);''')
        curs.execute('''CREATE INDEX umap_map_optim
                        ON umap_map (modified_at) WHERE
                        ("umap_map"."share_status" = 1
                        AND ST_Distance("umap_map"."center", ST_GeomFromEWKT(%s)) > 1000.0);''',
                     (start_coords,))

