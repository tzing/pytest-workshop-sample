import logging
import random

import psycopg2


def add(a: int, b: int) -> int:
    return a + b


def add_random(a: int, max_: int = 100) -> int:
    if max_ <= 0:
        raise ValueError("Arg max_ must be positive")
    return a + random.randint(0, max_)


def get_row_count(client: "psycopg2.connection", schema: str, table: str) -> int:
    with client.cursor() as cursor:
        try:
            cursor.execute(
                f"""
                    SELECT
                        COUNT(1)
                    FROM
                        "{schema}"."{table}"
                """
            )
            (count,) = cursor.fetchone()
        except psycopg2.Error:
            logging.exception("failed to read counts")
            return -1

    return count
