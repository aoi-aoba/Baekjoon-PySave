import sys

def solve():
    lines = sys.stdin.readlines()

    for line in lines:
        if not line.strip():
            continue
        try:
            k, m = map(int, line.split())
        except ValueError:
            continue
        diff_per_day = abs(k - m)
        days_to_sync = 43200.0 / diff_per_day
        total_seconds_moved = days_to_sync * (84600.0 + (1800.0 - k))  # 86400 - k
        final_seconds = total_seconds_moved % 43200.0
        total_minutes = int((final_seconds + 30.0) // 60)
        total_minutes %= 720

        hours = total_minutes // 60
        mins = total_minutes % 60

        if hours == 0:
            hours = 12
        print(f"{k} {m} {hours:02d}:{mins:02d}")

if __name__ == "__main__":
    solve()