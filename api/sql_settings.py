import os

postgresql = {
    "pguser": os.getenv("PG_USER") or "postgres.agkxhhrlhamiyvutsgnb",
    "pgpasswd": os.getenv("PG_PASSWD") or "15tuse0WS50L2j4B",
    "pghost": os.getenv("PG_HOST") or "aws-0-eu-central-1.pooler.supabase.com",
    "pgport": os.getenv("PG_PORT") or 6543,
    "pgdb": os.getenv("PG_DB") or "postgres",
}
