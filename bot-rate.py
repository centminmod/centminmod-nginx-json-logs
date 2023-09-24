#!/usr/bin/env python2.7
# Usage:
# ./bot-rate.py /var/log/nginx/access.log.json
# ./bot-rate.py /var/log/nginx/access.log.json keyword
# ./bot-rate.py /var/log/nginx/access.log.json keyword field_name

from __future__ import print_function
import json
import io
import sys
import gzip
import zstandard as zstd
from collections import defaultdict
from datetime import datetime, timedelta

# Check for the required number of arguments
if len(sys.argv) < 2:
    print("Usage: {} <path_to_log_file> [keyword] [field_name]".format(sys.argv[0]))
    sys.exit(1)

log_file_path = sys.argv[1]
keyword = sys.argv[2] if len(sys.argv) > 2 else "Bytespider"
field_name = sys.argv[3] if len(sys.argv) > 3 else None

# Create counters for each interval
per_second = defaultdict(int)
per_minute = defaultdict(int)
per_hour = defaultdict(int)
per_day = defaultdict(int)

# Buffer size in bytes
BUFFER_SIZE = 512 * 1024 * 1024

# Function to determine how to open the file based on its extension
def file_open(path, **kwargs):
    if path.endswith('.gz'):
        return gzip.open(path, 'rb', **kwargs)
    elif path.endswith('.zst'):
        dctx = zstd.ZstdDecompressor()
        decompressed_data = dctx.decompressobj().decompress(io.open(path, 'rb').read())
        return io.BytesIO(decompressed_data)
    else:
        return io.open(path, 'rb', **kwargs)

# Open the JSON log file with a specified buffer size and process line by line
with file_open(log_file_path, buffering=BUFFER_SIZE) as f:
    for line in f:
        line = line.decode('utf-8', 'replace')  # Decode with replacement for invalid bytes
        entry = json.loads(line)

        # Check if keyword is present in the specified field or in any field if no field is specified
        if field_name:
            if field_name not in entry or keyword not in str(entry[field_name]):
                continue
        elif not any(keyword in str(value) for value in entry.values()):
            continue

        timestamp = entry["time_iso8601"]
        dt_without_tz = datetime.strptime(timestamp[:-6], "%Y-%m-%dT%H:%M:%S")
        offset_hours = int(timestamp[-5:-3])
        offset_minutes = int(timestamp[-2:])
        if timestamp[-6] == '-':
            dt = dt_without_tz - timedelta(hours=offset_hours, minutes=offset_minutes)
        else:
            dt = dt_without_tz + timedelta(hours=offset_hours, minutes=offset_minutes)

        per_second[dt.strftime('%Y-%m-%dT%H:%M:%S')] += 1
        per_minute[dt.strftime('%Y-%m-%dT%H:%M')] += 1
        per_hour[dt.strftime('%Y-%m-%dT%H')] += 1
        per_day[dt.strftime('%Y-%m-%d')] += 1

# Function to print in three columns
def print_three_columns(data):
    sorted_data = sorted(data.items())
    for i in range(0, len(sorted_data), 3):
        line_entries = sorted_data[i:i+3]
        line_str = "\t".join(["{} ({})".format(entry[0], entry[1]) for entry in line_entries])
        print(line_str)

# Print the results
print("Requests with keyword '{}':".format(keyword))
if field_name:
    print("Filtered by field: '{}'".format(field_name))
print("Requests per second:")
print_three_columns(per_second)

print("\nRequests per minute:")
print_three_columns(per_minute)

print("\nRequests per hour:")
print_three_columns(per_hour)

print("\nRequests per day:")
print_three_columns(per_day)
