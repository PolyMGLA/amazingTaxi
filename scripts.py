SCHEME_QUERY = "CREATE SCHEMA IF NOT EXISTS blinov_oboldin;"
TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS blinov_oboldin.Users
(
    id_users bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    fio text COLLATE pg_catalog."default" NOT NULL,
    telephone text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id_users),
    CONSTRAINT fio_telephone UNIQUE (fio, telephone)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Taxi
(
    "id_Taxi" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    CONSTRAINT "Taxi_pkey" PRIMARY KEY ("id_Taxi")
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Driver
(
    id_dreiver bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    CONSTRAINT "Driver_pkey" PRIMARY KEY (id_dreiver)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Shift
(
    id_shift bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_taxi bigint NOT NULL,
    id_driver bigint NOT NULL,
    date date NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Shift_pkey" PRIMARY KEY (id_shift)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Order
(
    id_order bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_user bigint NOT NULL,
    id_shift bigint NOT NULL,
    start text COLLATE pg_catalog."default" NOT NULL,
    "end" text COLLATE pg_catalog."default" NOT NULL,
    "time" text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Order_pkey" PRIMARY KEY (id_order)
);
"""

def INIT_SCHEME(cur):
    cur.execute(SCHEME_QUERY)
    cur.execute(TABLE_QUERY)