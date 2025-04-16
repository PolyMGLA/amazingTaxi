CREATE SCHEMA IF NOT EXISTS blinov_oboldin;

CREATE TABLE IF NOT EXISTS blinov_oboldin.Users
(
    id_user bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    full_name text COLLATE pg_catalog."default" NOT NULL,
    phone text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id_user),
    CONSTRAINT name_phone UNIQUE (full_name, phone)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Taxi
(
    id_Taxi bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    CONSTRAINT "Taxi_pkey" PRIMARY KEY (id_Taxi)
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
    id_shift bigint,
    start_addr text COLLATE pg_catalog."default" NOT NULL,
    end_addr text COLLATE pg_catalog."default" NOT NULL,
    order_time text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Order_pkey" PRIMARY KEY (id_order)
);