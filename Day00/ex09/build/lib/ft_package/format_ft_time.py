import time

# Get the current Unix timestamp
timestamp = time.time()
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
# Convert the timestamp to a human-readable format
human_readable_time = time.strftime("%b %d %Y", time.localtime(timestamp))
print(human_readable_time)