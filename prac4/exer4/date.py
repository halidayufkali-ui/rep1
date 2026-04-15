from datetime import datetime, timedelta

# 1. Current date and date five days ago
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print( today)
print( five_days_ago)


# 2. Yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print( yesterday.date())
print( today.date())
print( tomorrow.date())


# 3. Drop microseconds
microseconds = today.replace(microsecond=0)
print( today)
print(microseconds)


# 4. Difference in seconds

date1 = datetime(2026, 3, 1, 12, 0, 0)
date2 = datetime(2026, 3, 3, 14, 30, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print(seconds)