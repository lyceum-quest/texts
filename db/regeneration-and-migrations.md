# Regeneration and Migration Policy

## Read-only reference databases

Applies to:

- `texts.db`
- `corpus.db`
- `editions.db`
- `morph.db`
- `lsj.db`

Rules:

1. Runtime code opens these databases read-only.
2. Schema changes should happen in the import/download/build scripts, not by hand-editing DB files.
3. Regenerate the DB, verify row counts and sample queries, then update release artifacts.
4. Release copies under `../release/` are artifacts, not schema sources.
5. If a schema differs between `reader` and `orchestrator`, document which file is canonical for runtime behavior.

## `users.db`

`users.db` is live local learner state.

Rules:

1. Back up `users.db`, `users.db-wal`, and `users.db-shm` before schema work.
2. Prefer additive migrations.
3. Do not destructively rebuild user data.
4. Test both fresh databases and existing historical databases.
5. Add versioned migrations in `../reader/internal/db/migrations.go`.
6. Keep compatibility notes for historical hosted-service columns/tables.

Current migration flow in reader code:

1. Open `data/users.db` read-write.
2. Enable WAL mode.
3. Create base tables in `../reader/internal/db/users.go`.
4. Run legacy compatibility alters.
5. Apply numbered migrations from `../reader/internal/db/migrations.go`.

Observed applied migrations:

| Version | Description |
|---:|---|
| 1 | Baseline schema from existing runMigrations |
| 2 | Add contexts column for accumulative vocabulary encounters |
