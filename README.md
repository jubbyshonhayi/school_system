# Multi-Tenant School Management System

Production-style Django starter for a SaaS-like school management platform with strict tenant isolation.

## Stack
- Django + CBVs
- Django Templates
- Modern CSS + vanilla JavaScript
- SQLite (dev default), PostgreSQL-ready configuration

## Apps
- `accounts`: custom user model + auth URLs
- `schools`: school tenant model
- `students`: student CRUD
- `core`: dashboard + tenant mixins

## Multi-tenant isolation
1. **View-level**: `SchoolScopedMixin` blocks unauthenticated, unassigned, and superuser frontend access.
2. **Queryset-level**: `SchoolQuerysetMixin` enforces `school=request.user.school` in `get_queryset`.
3. **Database-level filtering**: each student row links to a school FK; all CRUD is school-bound and uses filtered queryset methods to prevent IDOR.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Demo workflow
1. Login as superuser in `/admin`.
2. Create `School` record(s).
3. Create users and assign each user to exactly one school (`role=SCHOOL_USER`).
4. Login with school user at `/accounts/login/` and manage only that school's students.

## PostgreSQL migration notes
1. Install psycopg (`pip install psycopg[binary]`).
2. Set env vars:
   - `DB_ENGINE=django.db.backends.postgresql`
   - `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
3. Run `python manage.py migrate`.
4. Keep indexes/constraints already defined in models for scale-friendly queries.

## Scaling guidance (thousands of schools)
- Keep every business query tenant-filtered first (`school_id=...`).
- Add caching for dashboard counters and frequently used lists.
- Use PostgreSQL with connection pooling and read replicas.
- Add async task queue for heavy imports/exports.
- Consider row-level security or schema/database-per-tenant if contractual isolation demands increase.

## Deployment basics
- Set `DJANGO_DEBUG=False`, secure secret key, and strict `ALLOWED_HOSTS`.
- Serve static files via CDN or reverse proxy.
- Use gunicorn/uvicorn behind nginx.
- Run CI checks (`check`, tests, lint) before deploy.
