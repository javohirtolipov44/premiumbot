--
-- PostgreSQL database dump
--

\restrict 3BHKhvaI2ae1e7gOka210xiNG7rhDtlSQ0gEBL68klEzoHYBxwVn8dRkzaOFax6

-- Dumped from database version 15.15 (Debian 15.15-1.pgdg13+1)
-- Dumped by pg_dump version 15.15 (Debian 15.15-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ban_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ban_users (
    id integer NOT NULL,
    chat_id bigint NOT NULL,
    ban_time bigint NOT NULL
);


ALTER TABLE public.ban_users OWNER TO postgres;

--
-- Name: ban_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ban_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ban_users_id_seq OWNER TO postgres;

--
-- Name: ban_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ban_users_id_seq OWNED BY public.ban_users.id;


--
-- Name: bot_sleep; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bot_sleep (
    id integer NOT NULL,
    sleep_time bigint NOT NULL
);


ALTER TABLE public.bot_sleep OWNER TO postgres;

--
-- Name: bot_sleep_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bot_sleep_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bot_sleep_id_seq OWNER TO postgres;

--
-- Name: bot_sleep_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bot_sleep_id_seq OWNED BY public.bot_sleep.id;


--
-- Name: premium_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.premium_users (
    id integer NOT NULL,
    chat_id bigint NOT NULL,
    file_id character varying(255),
    start_at bigint NOT NULL,
    end_at bigint NOT NULL
);


ALTER TABLE public.premium_users OWNER TO postgres;

--
-- Name: premium_users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.premium_users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.premium_users_id_seq OWNER TO postgres;

--
-- Name: premium_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.premium_users_id_seq OWNED BY public.premium_users.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    chat_id bigint NOT NULL,
    full_name character varying(255) NOT NULL,
    username character varying(255) NOT NULL,
    file_id character varying(255)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: ban_users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ban_users ALTER COLUMN id SET DEFAULT nextval('public.ban_users_id_seq'::regclass);


--
-- Name: bot_sleep id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bot_sleep ALTER COLUMN id SET DEFAULT nextval('public.bot_sleep_id_seq'::regclass);


--
-- Name: premium_users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.premium_users ALTER COLUMN id SET DEFAULT nextval('public.premium_users_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: ban_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ban_users (id, chat_id, ban_time) FROM stdin;
\.


--
-- Data for Name: bot_sleep; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bot_sleep (id, sleep_time) FROM stdin;
\.


--
-- Data for Name: premium_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.premium_users (id, chat_id, file_id, start_at, end_at) FROM stdin;
4	7294235755	AgACAgIAAxkBAAIGwml3IruJ5rl4Qa2UfcQJvPAWihf4AAJoEmsbF2K4S9S8QQf9JIxpAQADAgADdwADOAQ	1769414612	1774512212
3	1179777869	AgACAgIAAxkBAAIGO2l3CvhpkemUcDS-ovfYj4OUGmh_AAJOC2sbZefAS70BlkqB1axrAQADAgADdwADOAQ	1769414571	1774512171
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, chat_id, full_name, username, file_id) FROM stdin;
1	652840346	𝙅𝘼𝙑𝙊𝙃𝙄𝙍	@javohir4418	\N
3	7294235755	Javohir	Mavjud emas	AgACAgIAAxkBAAIGwml3IruJ5rl4Qa2UfcQJvPAWihf4AAJoEmsbF2K4S9S8QQf9JIxpAQADAgADdwADOAQ
2	1179777869	Javohir ORK	@fleshmango	AgACAgIAAxkBAAIHGGl3JKAGw2tsDK1Au2OJkEUqHSYCAAJSDGsbZefAS96yk_1gzgI4AQADAgADdwADOAQ
\.


--
-- Name: ban_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ban_users_id_seq', 1, false);


--
-- Name: bot_sleep_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bot_sleep_id_seq', 1, false);


--
-- Name: premium_users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.premium_users_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: ban_users ban_users_chat_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ban_users
    ADD CONSTRAINT ban_users_chat_id_key UNIQUE (chat_id);


--
-- Name: ban_users ban_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ban_users
    ADD CONSTRAINT ban_users_pkey PRIMARY KEY (id);


--
-- Name: bot_sleep bot_sleep_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bot_sleep
    ADD CONSTRAINT bot_sleep_pkey PRIMARY KEY (id);


--
-- Name: premium_users premium_users_chat_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.premium_users
    ADD CONSTRAINT premium_users_chat_id_key UNIQUE (chat_id);


--
-- Name: premium_users premium_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.premium_users
    ADD CONSTRAINT premium_users_pkey PRIMARY KEY (id);


--
-- Name: users users_chat_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_chat_id_key UNIQUE (chat_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict 3BHKhvaI2ae1e7gOka210xiNG7rhDtlSQ0gEBL68klEzoHYBxwVn8dRkzaOFax6

