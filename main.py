"""Homework scaffold — postgresql lesson `l2_backups_and_pitr` (Vibe Learn).

Задача: pg_basebackup → MinIO, archive_command для WAL, PITR-восстановление и чек-сумма.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

Драйвер: psycopg (v3). DSN берётся из env DATABASE_URL.
"""

import os

import psycopg


def database_url() -> str:
    """DSN PostgreSQL из env. Дефолт совпадает с docker-compose.yml."""
    return os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/postgres",
    )


def connect() -> "psycopg.Connection":
    """Открыть соединение psycopg из DATABASE_URL."""
    return psycopg.connect(database_url())


# ----- TODO #1: take_basebackup -----
def take_basebackup(dsn: str, dest_dir: str) -> str:
    """запустить pg_basebackup (формат tar) в dest_dir; вернуть путь к архиву"""
    raise NotImplementedError("take_basebackup: реализуй меня")


# ----- TODO #2: checksum_tables -----
def checksum_tables(conn, tables: list[str]) -> dict[str, str]:
    """посчитать стабильную чек-сумму (md5 от ORDER BY-выборки) ключевых таблиц"""
    raise NotImplementedError("checksum_tables: реализуй меня")


# ----- TODO #3: restore_to_point -----
def restore_to_point(backup_dir: str, target_time: str, out_dir: str) -> None:
    """поднять отдельный кластер из бэкапа с recovery_target_time = target_time (PITR)"""
    raise NotImplementedError("restore_to_point: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — postgresql lesson scaffold up")
    print(f"DATABASE_URL: {database_url()}")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
