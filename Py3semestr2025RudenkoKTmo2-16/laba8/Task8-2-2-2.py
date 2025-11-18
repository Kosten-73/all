import sqlite3
import argparse
import socket
import os
import sys

DB_NAME = "visits.db"


def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "127.0.0.1"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        user_fio TEXT,
        ip TEXT,
        user_agent TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_visit(user_fio, ip, user_agent):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO visits (user_fio, ip, user_agent)
    VALUES (?, ?, ?)
    """, (user_fio, ip, user_agent))

    conn.commit()
    conn.close()


def print_last_visits(limit=10):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(f"""
        SELECT id, timestamp, user_fio, ip, user_agent
        FROM visits
        ORDER BY id DESC
        LIMIT {limit}
    """)

    rows = cur.fetchall()
    conn.close()

    print("\nПоследние посещения:")
    print("-" * 60)
    for row in rows:
        print(f"ID: {row[0]}, Время: {row[1]}, Пользователь: {row[2]}, IP: {row[3]}")
        print(f"User-Agent: {row[4]}")
        print("-" * 60)


def main():
    init_db()
    parser = argparse.ArgumentParser(description="Логгер посещений")
    parser.add_argument("--user", type=str, default="Неизвестный пользователь",
                        help="ФИО пользователя")
    args = parser.parse_args()
    user_fio = args.user
    ip = get_ip()
    user_agent = f"Python/{sys.version.split()[0]} on {os.name}"
    log_visit(user_fio, ip, user_agent)
    print_last_visits(10)


if __name__ == "__main__":
    main()

# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba8\Task8-2-2-2.py
#
# Последние посещения:
# ------------------------------------------------------------
# ID: 4, Время: 2025-11-18 20:16:06, Пользователь: Неизвестный пользователь, IP: 10.0.85.2
# User-Agent: Python/3.9.13 on nt
# ------------------------------------------------------------
# ID: 3, Время: 2025-11-18 20:09:44, Пользователь: Неизвестный пользователь, IP: 10.0.85.2
# User-Agent: Python/3.9.13 on nt
# ------------------------------------------------------------
# ID: 2, Время: 2025-11-18 20:04:11, Пользователь: Неизвестный пользователь, IP: 10.0.85.2
# User-Agent: Python/3.9.13 on nt
# ------------------------------------------------------------
# ID: 1, Время: 2025-11-18 20:04:00, Пользователь: Неизвестный пользователь, IP: 10.0.85.2
# User-Agent: Python/3.9.13 on nt
# ------------------------------------------------------------
#
# Process finished with exit code 0
