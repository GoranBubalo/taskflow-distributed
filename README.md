# TaskFlow Distributed System

## Opis

TaskFlow je distribuirani sustav za upravljanje zadacima, razvijen u Pythonu koristeći FastAPI, SQLAlchemy, Celery, PostgreSQL i Redis.  
Aplikacija koristi višeslojnu arhitekturu (API, servisni i repozitorijski sloj) te je u potpunosti dockerizirana radi jednostavnog pokretanja i razvoja.

---

## Preduvjeti

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Pokretanje aplikacije

1. **Kloniraj repozitorij:**
   ```sh
   git clone https://github.com/your-username/taskflow-distributed.git
   cd taskflow-distributed/src/docker
   ```

2. **Buildaj i pokreni sve servise:**
   ```sh
   docker-compose up --build
   ```
   Ovo će pokrenuti:
   - FastAPI API server (na portu 8000)
   - Celery worker (za obradu zadataka u pozadini)
   - PostgreSQL bazu podataka (na portu 5432)
   - Redis (za Celery broker i rezultate, na portu 6379)

3. **Pristupi API dokumentaciji:**
   - Otvori preglednik i idi na: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Ovdje možeš isprobati sve dostupne API endpointove.

---

## Korištenje aplikacije

### Korisnički endpointi

- `POST /users/` – Kreiraj korisnika
- `GET /users/` – Dohvati sve korisnike
- `GET /users/{user_id}` – Dohvati korisnika po ID-u
- `PUT /users/{user_id}` – Ažuriraj korisnika
- `DELETE /users/{user_id}` – Obriši korisnika

### Task endpointi

- `POST /tasks/` – Kreiraj zadatak
- `GET /tasks/` – Dohvati sve zadatke
- `GET /tasks/{task_id}` – Dohvati zadatak po ID-u
- `PUT /tasks/{task_id}` – Ažuriraj zadatak
- `DELETE /tasks/{task_id}` – Obriši zadatak

---

## Zaustavljanje sustava

Za zaustavljanje svih servisa pritisni `CTRL+C` u terminalu ili pokreni:
```sh
docker-compose down
```

---

## Napomene

- Svi servisi i konfiguracije definirani su u `src/docker/docker-compose.yml`.
- Za promjene u kodu, ponovno buildaj i pokreni kontejnere s `docker-compose up --build`.
- Ako koristiš Windows, provjeri da su svi `.sh` skripte s Unix (LF) line ending-ima.

---

## Rješavanje problema

- Ako ne možeš pristupiti bazi ili API-ju, provjeri da su Docker i svi potrebni portovi (`8000`, `5432`, `6379`) slobodni.
- Ako dobiješ grešku vezanu uz `wait-for-postgres.sh`, provjeri da je skripta kopirana u `/app` direktorij u kontejneru i da ima ispravne (LF) line ending-e.

