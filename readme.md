Tools for parsing Centmin Mod Nginx JSON log format based logging as per https://community.centminmod.com/threads/how-to-configure-nginx-for-json-based-access-logging.19641/

* [bot-rate.py parser](#bot-ratepy-parser)
* [Centmin Mod Nginx JSON Logs](#centmin-mod-nginx-json-logs)
* [Nginx JSON Format Logs with Cloudflare Proxy](#nginx-json-format-logs-with-cloudflare-proxy)

# bot-rate.py parser

The `bot-rate.py` script will parse Centmin Mod Nginx JSON log fields for specific case-sensitive keyword i.e. `botname` and calculate the request rate for per second, minute, hour and day.


## Requirements

`bot-rate.py` supports gzip and zstd compressed JSON logs too.

```
pip install zstandard
```

```
./bot-rate.py /home/nginx/domains/domain.com/log/access_log.json.gz botname

./bot-rate.py /home/nginx/domains/domain.com/log/access_log.json.zst botname
```

## Examples

```
./bot-rate.py 
Usage: ./bot-rate.py <path_to_log_file> [keyword] [field_name]
```

```
./bot-rate.py /home/nginx/domains/domain.com/log/access_log.json botname
```

```
./bot-rate.py /home/nginx/domains/domain.com/log/access_log.json botname

Requests with keyword 'botname':
Requests per second:
2023-09-23T03:40:04 (1) 2023-09-23T03:45:04 (1) 2023-09-23T03:50:04 (1)
2023-09-23T03:55:05 (1) 2023-09-23T04:00:04 (1) 2023-09-23T04:05:04 (1)
2023-09-23T04:10:04 (1) 2023-09-23T04:15:05 (1) 2023-09-23T04:20:04 (1)
2023-09-23T04:25:05 (1) 2023-09-23T04:30:04 (1) 2023-09-23T04:35:04 (1)
2023-09-23T04:40:05 (1) 2023-09-23T04:45:04 (1) 2023-09-23T04:50:04 (1)
2023-09-23T04:55:04 (1) 2023-09-23T05:00:04 (1) 2023-09-23T05:05:04 (1)
2023-09-23T05:10:04 (1) 2023-09-23T05:15:04 (1) 2023-09-23T05:20:05 (1)
2023-09-23T05:25:04 (1) 2023-09-23T05:30:04 (1) 2023-09-23T05:35:05 (1)
2023-09-23T05:40:04 (1) 2023-09-23T05:45:05 (1) 2023-09-23T05:50:05 (1)
2023-09-23T05:55:04 (1) 2023-09-23T06:00:05 (1) 2023-09-23T06:05:04 (1)
2023-09-23T06:10:04 (1) 2023-09-23T06:15:05 (1) 2023-09-23T06:20:04 (1)
2023-09-23T06:25:05 (1) 2023-09-23T06:30:04 (1) 2023-09-23T06:35:04 (1)
2023-09-23T06:40:05 (1) 2023-09-23T06:45:04 (1) 2023-09-23T06:50:04 (1)
2023-09-23T06:55:04 (1) 2023-09-23T07:00:04 (1) 2023-09-23T07:05:04 (1)
2023-09-23T07:10:04 (1) 2023-09-23T07:15:04 (1) 2023-09-23T07:20:05 (1)
2023-09-23T07:25:04 (1) 2023-09-23T07:30:05 (1) 2023-09-23T07:35:04 (1)
2023-09-23T07:40:04 (1) 2023-09-23T07:45:05 (1) 2023-09-23T07:50:04 (1)
2023-09-23T07:55:04 (1) 2023-09-23T08:00:04 (1) 2023-09-23T08:05:04 (1)
2023-09-23T08:10:04 (1) 2023-09-23T08:15:04 (1) 2023-09-23T08:20:05 (1)
2023-09-23T08:25:05 (1) 2023-09-23T08:30:04 (1) 2023-09-23T08:35:04 (1)
2023-09-23T08:40:04 (1) 2023-09-23T08:45:04 (1) 2023-09-23T08:50:05 (1)
2023-09-23T08:55:04 (1) 2023-09-23T09:00:05 (1) 2023-09-23T09:05:05 (1)
2023-09-23T09:10:04 (1) 2023-09-23T09:15:04 (1) 2023-09-23T09:20:04 (1)
2023-09-23T09:25:05 (1) 2023-09-23T09:30:05 (1) 2023-09-23T09:35:04 (1)
2023-09-23T09:40:04 (1) 2023-09-23T09:45:04 (1) 2023-09-23T09:50:05 (1)
2023-09-23T09:55:05 (1) 2023-09-23T10:00:04 (1) 2023-09-23T10:05:04 (1)
2023-09-23T10:10:04 (1) 2023-09-23T10:15:04 (1) 2023-09-23T10:20:04 (1)
2023-09-23T10:25:04 (1) 2023-09-23T10:30:04 (1) 2023-09-23T10:35:05 (1)
2023-09-23T10:40:04 (1) 2023-09-23T10:45:05 (1) 2023-09-23T10:50:04 (1)
2023-09-23T10:55:04 (1) 2023-09-23T11:00:04 (1) 2023-09-23T11:05:04 (1)
2023-09-23T11:10:04 (1) 2023-09-23T11:15:04 (1) 2023-09-23T11:20:04 (1)
2023-09-23T11:25:04 (1) 2023-09-23T11:30:04 (1) 2023-09-23T11:35:04 (1)
2023-09-23T11:40:04 (1) 2023-09-23T11:45:04 (1) 2023-09-23T11:50:04 (1)
2023-09-23T11:55:04 (1) 2023-09-23T12:00:04 (1) 2023-09-23T12:05:04 (1)
2023-09-23T12:10:04 (1) 2023-09-23T12:15:04 (1) 2023-09-23T12:20:05 (1)
2023-09-23T12:25:04 (1) 2023-09-23T12:30:04 (1) 2023-09-23T12:35:05 (1)
2023-09-23T12:40:04 (1) 2023-09-23T12:45:04 (1) 2023-09-23T12:50:04 (1)
2023-09-23T12:55:04 (1) 2023-09-23T13:00:05 (1) 2023-09-23T13:05:04 (1)
2023-09-23T13:10:04 (1) 2023-09-23T13:15:05 (1) 2023-09-23T13:20:04 (1)
2023-09-23T13:25:05 (1) 2023-09-23T13:30:04 (1) 2023-09-23T13:35:05 (1)
2023-09-23T13:40:04 (1) 2023-09-23T13:45:04 (1) 2023-09-23T13:50:05 (1)
2023-09-23T13:55:04 (1) 2023-09-23T14:00:04 (1) 2023-09-23T14:05:04 (1)
2023-09-23T14:10:04 (1) 2023-09-23T14:15:04 (1) 2023-09-23T14:20:04 (1)
2023-09-23T14:25:04 (1) 2023-09-23T14:30:04 (1) 2023-09-23T14:35:04 (1)
2023-09-23T14:40:04 (1) 2023-09-23T14:45:04 (1) 2023-09-23T14:50:04 (1)
2023-09-23T14:55:04 (1) 2023-09-23T15:00:04 (1) 2023-09-23T15:05:04 (1)
2023-09-23T15:10:05 (1) 2023-09-23T15:15:04 (1) 2023-09-23T15:20:04 (1)
2023-09-23T15:25:04 (1) 2023-09-23T15:30:04 (1) 2023-09-23T15:35:04 (1)
2023-09-23T15:40:04 (1) 2023-09-23T15:45:05 (1) 2023-09-23T15:50:04 (1)
2023-09-23T15:55:04 (1) 2023-09-23T16:00:04 (1) 2023-09-23T16:05:05 (1)
2023-09-23T16:10:04 (1) 2023-09-23T16:15:04 (1) 2023-09-23T16:20:04 (1)
2023-09-23T16:25:04 (1) 2023-09-23T16:30:04 (1) 2023-09-23T16:35:05 (1)
2023-09-23T16:40:04 (1) 2023-09-23T16:45:04 (1) 2023-09-23T16:50:05 (1)
2023-09-23T16:55:04 (1) 2023-09-23T17:00:05 (1) 2023-09-23T17:05:04 (1)
2023-09-23T17:10:04 (1) 2023-09-23T17:15:05 (1) 2023-09-23T17:20:04 (1)
2023-09-23T17:25:04 (1) 2023-09-23T17:30:04 (1) 2023-09-23T17:35:04 (1)
2023-09-23T17:40:04 (1) 2023-09-23T17:45:05 (1) 2023-09-23T17:50:04 (1)
2023-09-23T17:55:04 (1) 2023-09-23T18:00:04 (1) 2023-09-23T18:05:05 (1)
2023-09-23T18:10:04 (1) 2023-09-23T18:15:05 (1) 2023-09-23T18:20:04 (1)
2023-09-23T18:25:04 (1) 2023-09-23T18:30:04 (1) 2023-09-23T18:35:04 (1)
2023-09-23T18:40:04 (1) 2023-09-23T18:45:04 (1) 2023-09-23T18:50:04 (1)
2023-09-23T18:55:05 (1) 2023-09-23T19:00:04 (1) 2023-09-23T19:05:04 (1)
2023-09-23T19:10:04 (1) 2023-09-23T19:15:04 (1) 2023-09-23T19:20:04 (1)
2023-09-23T19:25:04 (1) 2023-09-23T19:30:04 (1) 2023-09-23T19:35:04 (1)
2023-09-23T19:40:05 (1) 2023-09-23T19:45:04 (1) 2023-09-23T19:50:04 (1)
2023-09-23T19:55:04 (1) 2023-09-23T20:00:04 (1) 2023-09-23T20:05:04 (1)
2023-09-23T20:10:04 (1) 2023-09-23T20:15:05 (1) 2023-09-23T20:20:05 (1)
2023-09-23T20:25:05 (1) 2023-09-23T20:30:04 (1) 2023-09-23T20:35:05 (1)
2023-09-23T20:40:04 (1) 2023-09-23T20:45:04 (1) 2023-09-23T20:50:04 (1)
2023-09-23T20:55:04 (1) 2023-09-23T21:00:04 (1) 2023-09-23T21:05:04 (1)
2023-09-23T21:10:04 (1) 2023-09-23T21:15:04 (1) 2023-09-23T21:20:04 (1)
2023-09-23T21:25:05 (1) 2023-09-23T21:30:05 (1) 2023-09-23T21:35:04 (1)
2023-09-23T21:40:04 (1) 2023-09-23T21:45:04 (1) 2023-09-23T21:50:04 (1)
2023-09-23T21:55:05 (1) 2023-09-23T22:00:04 (1) 2023-09-23T22:05:05 (1)
2023-09-23T22:10:05 (1) 2023-09-23T22:15:05 (1) 2023-09-23T22:20:05 (1)
2023-09-23T22:25:05 (1) 2023-09-23T22:30:04 (1) 2023-09-23T22:35:04 (1)
2023-09-23T22:40:04 (1) 2023-09-23T22:45:04 (1) 2023-09-23T22:50:04 (1)
2023-09-23T22:55:04 (1) 2023-09-23T23:00:04 (1) 2023-09-23T23:05:04 (1)
2023-09-23T23:10:05 (1) 2023-09-23T23:15:05 (1) 2023-09-23T23:20:04 (1)
2023-09-23T23:25:05 (1) 2023-09-23T23:30:04 (1) 2023-09-23T23:35:04 (1)
2023-09-23T23:40:05 (1) 2023-09-23T23:45:04 (1) 2023-09-23T23:50:04 (1)
2023-09-23T23:55:04 (1) 2023-09-24T00:00:05 (1) 2023-09-24T00:05:04 (1)
2023-09-24T00:10:05 (1) 2023-09-24T00:15:04 (1) 2023-09-24T00:20:04 (1)
2023-09-24T00:25:05 (1) 2023-09-24T00:30:04 (1) 2023-09-24T00:35:04 (1)
2023-09-24T00:40:05 (1) 2023-09-24T00:45:05 (1) 2023-09-24T00:50:05 (1)
2023-09-24T00:55:04 (1) 2023-09-24T01:00:04 (1) 2023-09-24T01:05:05 (1)
2023-09-24T01:10:04 (1) 2023-09-24T01:15:04 (1) 2023-09-24T01:20:04 (1)
2023-09-24T01:25:04 (1) 2023-09-24T01:30:04 (1) 2023-09-24T01:35:05 (1)
2023-09-24T01:40:05 (1) 2023-09-24T01:45:05 (1) 2023-09-24T01:50:05 (1)
2023-09-24T01:55:04 (1) 2023-09-24T02:00:04 (1) 2023-09-24T02:05:04 (1)
2023-09-24T02:10:04 (1) 2023-09-24T02:15:04 (1) 2023-09-24T02:20:04 (1)
2023-09-24T02:25:05 (1) 2023-09-24T02:30:04 (1) 2023-09-24T02:35:04 (1)
2023-09-24T02:40:04 (1) 2023-09-24T02:45:04 (1) 2023-09-24T02:50:05 (1)
2023-09-24T02:55:04 (1) 2023-09-24T03:00:04 (1) 2023-09-24T03:05:04 (1)
2023-09-24T03:10:04 (1) 2023-09-24T03:15:04 (1) 2023-09-24T03:20:04 (1)
2023-09-24T03:25:04 (1) 2023-09-24T03:30:04 (1)

Requests per minute:
2023-09-23T03:40 (1)    2023-09-23T03:45 (1)    2023-09-23T03:50 (1)
2023-09-23T03:55 (1)    2023-09-23T04:00 (1)    2023-09-23T04:05 (1)
2023-09-23T04:10 (1)    2023-09-23T04:15 (1)    2023-09-23T04:20 (1)
2023-09-23T04:25 (1)    2023-09-23T04:30 (1)    2023-09-23T04:35 (1)
2023-09-23T04:40 (1)    2023-09-23T04:45 (1)    2023-09-23T04:50 (1)
2023-09-23T04:55 (1)    2023-09-23T05:00 (1)    2023-09-23T05:05 (1)
2023-09-23T05:10 (1)    2023-09-23T05:15 (1)    2023-09-23T05:20 (1)
2023-09-23T05:25 (1)    2023-09-23T05:30 (1)    2023-09-23T05:35 (1)
2023-09-23T05:40 (1)    2023-09-23T05:45 (1)    2023-09-23T05:50 (1)
2023-09-23T05:55 (1)    2023-09-23T06:00 (1)    2023-09-23T06:05 (1)
2023-09-23T06:10 (1)    2023-09-23T06:15 (1)    2023-09-23T06:20 (1)
2023-09-23T06:25 (1)    2023-09-23T06:30 (1)    2023-09-23T06:35 (1)
2023-09-23T06:40 (1)    2023-09-23T06:45 (1)    2023-09-23T06:50 (1)
2023-09-23T06:55 (1)    2023-09-23T07:00 (1)    2023-09-23T07:05 (1)
2023-09-23T07:10 (1)    2023-09-23T07:15 (1)    2023-09-23T07:20 (1)
2023-09-23T07:25 (1)    2023-09-23T07:30 (1)    2023-09-23T07:35 (1)
2023-09-23T07:40 (1)    2023-09-23T07:45 (1)    2023-09-23T07:50 (1)
2023-09-23T07:55 (1)    2023-09-23T08:00 (1)    2023-09-23T08:05 (1)
2023-09-23T08:10 (1)    2023-09-23T08:15 (1)    2023-09-23T08:20 (1)
2023-09-23T08:25 (1)    2023-09-23T08:30 (1)    2023-09-23T08:35 (1)
2023-09-23T08:40 (1)    2023-09-23T08:45 (1)    2023-09-23T08:50 (1)
2023-09-23T08:55 (1)    2023-09-23T09:00 (1)    2023-09-23T09:05 (1)
2023-09-23T09:10 (1)    2023-09-23T09:15 (1)    2023-09-23T09:20 (1)
2023-09-23T09:25 (1)    2023-09-23T09:30 (1)    2023-09-23T09:35 (1)
2023-09-23T09:40 (1)    2023-09-23T09:45 (1)    2023-09-23T09:50 (1)
2023-09-23T09:55 (1)    2023-09-23T10:00 (1)    2023-09-23T10:05 (1)
2023-09-23T10:10 (1)    2023-09-23T10:15 (1)    2023-09-23T10:20 (1)
2023-09-23T10:25 (1)    2023-09-23T10:30 (1)    2023-09-23T10:35 (1)
2023-09-23T10:40 (1)    2023-09-23T10:45 (1)    2023-09-23T10:50 (1)
2023-09-23T10:55 (1)    2023-09-23T11:00 (1)    2023-09-23T11:05 (1)
2023-09-23T11:10 (1)    2023-09-23T11:15 (1)    2023-09-23T11:20 (1)
2023-09-23T11:25 (1)    2023-09-23T11:30 (1)    2023-09-23T11:35 (1)
2023-09-23T11:40 (1)    2023-09-23T11:45 (1)    2023-09-23T11:50 (1)
2023-09-23T11:55 (1)    2023-09-23T12:00 (1)    2023-09-23T12:05 (1)
2023-09-23T12:10 (1)    2023-09-23T12:15 (1)    2023-09-23T12:20 (1)
2023-09-23T12:25 (1)    2023-09-23T12:30 (1)    2023-09-23T12:35 (1)
2023-09-23T12:40 (1)    2023-09-23T12:45 (1)    2023-09-23T12:50 (1)
2023-09-23T12:55 (1)    2023-09-23T13:00 (1)    2023-09-23T13:05 (1)
2023-09-23T13:10 (1)    2023-09-23T13:15 (1)    2023-09-23T13:20 (1)
2023-09-23T13:25 (1)    2023-09-23T13:30 (1)    2023-09-23T13:35 (1)
2023-09-23T13:40 (1)    2023-09-23T13:45 (1)    2023-09-23T13:50 (1)
2023-09-23T13:55 (1)    2023-09-23T14:00 (1)    2023-09-23T14:05 (1)
2023-09-23T14:10 (1)    2023-09-23T14:15 (1)    2023-09-23T14:20 (1)
2023-09-23T14:25 (1)    2023-09-23T14:30 (1)    2023-09-23T14:35 (1)
2023-09-23T14:40 (1)    2023-09-23T14:45 (1)    2023-09-23T14:50 (1)
2023-09-23T14:55 (1)    2023-09-23T15:00 (1)    2023-09-23T15:05 (1)
2023-09-23T15:10 (1)    2023-09-23T15:15 (1)    2023-09-23T15:20 (1)
2023-09-23T15:25 (1)    2023-09-23T15:30 (1)    2023-09-23T15:35 (1)
2023-09-23T15:40 (1)    2023-09-23T15:45 (1)    2023-09-23T15:50 (1)
2023-09-23T15:55 (1)    2023-09-23T16:00 (1)    2023-09-23T16:05 (1)
2023-09-23T16:10 (1)    2023-09-23T16:15 (1)    2023-09-23T16:20 (1)
2023-09-23T16:25 (1)    2023-09-23T16:30 (1)    2023-09-23T16:35 (1)
2023-09-23T16:40 (1)    2023-09-23T16:45 (1)    2023-09-23T16:50 (1)
2023-09-23T16:55 (1)    2023-09-23T17:00 (1)    2023-09-23T17:05 (1)
2023-09-23T17:10 (1)    2023-09-23T17:15 (1)    2023-09-23T17:20 (1)
2023-09-23T17:25 (1)    2023-09-23T17:30 (1)    2023-09-23T17:35 (1)
2023-09-23T17:40 (1)    2023-09-23T17:45 (1)    2023-09-23T17:50 (1)
2023-09-23T17:55 (1)    2023-09-23T18:00 (1)    2023-09-23T18:05 (1)
2023-09-23T18:10 (1)    2023-09-23T18:15 (1)    2023-09-23T18:20 (1)
2023-09-23T18:25 (1)    2023-09-23T18:30 (1)    2023-09-23T18:35 (1)
2023-09-23T18:40 (1)    2023-09-23T18:45 (1)    2023-09-23T18:50 (1)
2023-09-23T18:55 (1)    2023-09-23T19:00 (1)    2023-09-23T19:05 (1)
2023-09-23T19:10 (1)    2023-09-23T19:15 (1)    2023-09-23T19:20 (1)
2023-09-23T19:25 (1)    2023-09-23T19:30 (1)    2023-09-23T19:35 (1)
2023-09-23T19:40 (1)    2023-09-23T19:45 (1)    2023-09-23T19:50 (1)
2023-09-23T19:55 (1)    2023-09-23T20:00 (1)    2023-09-23T20:05 (1)
2023-09-23T20:10 (1)    2023-09-23T20:15 (1)    2023-09-23T20:20 (1)
2023-09-23T20:25 (1)    2023-09-23T20:30 (1)    2023-09-23T20:35 (1)
2023-09-23T20:40 (1)    2023-09-23T20:45 (1)    2023-09-23T20:50 (1)
2023-09-23T20:55 (1)    2023-09-23T21:00 (1)    2023-09-23T21:05 (1)
2023-09-23T21:10 (1)    2023-09-23T21:15 (1)    2023-09-23T21:20 (1)
2023-09-23T21:25 (1)    2023-09-23T21:30 (1)    2023-09-23T21:35 (1)
2023-09-23T21:40 (1)    2023-09-23T21:45 (1)    2023-09-23T21:50 (1)
2023-09-23T21:55 (1)    2023-09-23T22:00 (1)    2023-09-23T22:05 (1)
2023-09-23T22:10 (1)    2023-09-23T22:15 (1)    2023-09-23T22:20 (1)
2023-09-23T22:25 (1)    2023-09-23T22:30 (1)    2023-09-23T22:35 (1)
2023-09-23T22:40 (1)    2023-09-23T22:45 (1)    2023-09-23T22:50 (1)
2023-09-23T22:55 (1)    2023-09-23T23:00 (1)    2023-09-23T23:05 (1)
2023-09-23T23:10 (1)    2023-09-23T23:15 (1)    2023-09-23T23:20 (1)
2023-09-23T23:25 (1)    2023-09-23T23:30 (1)    2023-09-23T23:35 (1)
2023-09-23T23:40 (1)    2023-09-23T23:45 (1)    2023-09-23T23:50 (1)
2023-09-23T23:55 (1)    2023-09-24T00:00 (1)    2023-09-24T00:05 (1)
2023-09-24T00:10 (1)    2023-09-24T00:15 (1)    2023-09-24T00:20 (1)
2023-09-24T00:25 (1)    2023-09-24T00:30 (1)    2023-09-24T00:35 (1)
2023-09-24T00:40 (1)    2023-09-24T00:45 (1)    2023-09-24T00:50 (1)
2023-09-24T00:55 (1)    2023-09-24T01:00 (1)    2023-09-24T01:05 (1)
2023-09-24T01:10 (1)    2023-09-24T01:15 (1)    2023-09-24T01:20 (1)
2023-09-24T01:25 (1)    2023-09-24T01:30 (1)    2023-09-24T01:35 (1)
2023-09-24T01:40 (1)    2023-09-24T01:45 (1)    2023-09-24T01:50 (1)
2023-09-24T01:55 (1)    2023-09-24T02:00 (1)    2023-09-24T02:05 (1)
2023-09-24T02:10 (1)    2023-09-24T02:15 (1)    2023-09-24T02:20 (1)
2023-09-24T02:25 (1)    2023-09-24T02:30 (1)    2023-09-24T02:35 (1)
2023-09-24T02:40 (1)    2023-09-24T02:45 (1)    2023-09-24T02:50 (1)
2023-09-24T02:55 (1)    2023-09-24T03:00 (1)    2023-09-24T03:05 (1)
2023-09-24T03:10 (1)    2023-09-24T03:15 (1)    2023-09-24T03:20 (1)
2023-09-24T03:25 (1)    2023-09-24T03:30 (1)

Requests per hour:
2023-09-23T03 (4)       2023-09-23T04 (12)      2023-09-23T05 (12)
2023-09-23T06 (12)      2023-09-23T07 (12)      2023-09-23T08 (12)
2023-09-23T09 (12)      2023-09-23T10 (12)      2023-09-23T11 (12)
2023-09-23T12 (12)      2023-09-23T13 (12)      2023-09-23T14 (12)
2023-09-23T15 (12)      2023-09-23T16 (12)      2023-09-23T17 (12)
2023-09-23T18 (12)      2023-09-23T19 (12)      2023-09-23T20 (12)
2023-09-23T21 (12)      2023-09-23T22 (12)      2023-09-23T23 (12)
2023-09-24T00 (12)      2023-09-24T01 (12)      2023-09-24T02 (12)
2023-09-24T03 (7)

Requests per day:
2023-09-23 (244)        2023-09-24 (43)
```

# Centmin Mod Nginx JSON Logs

To setup Nginx JSON access logging, you will need to manually edit your main `/usr/local/nginx/conf/nginx.conf` config file and add a 4th `log_format` to existing listing which is listed directly below where log_format named = `main_json`:

```
log_format main_json escape=json '{'
  '"msec": "$msec", ' # request unixtime in seconds with a milliseconds resolution
  '"connection": "$connection", ' # connection serial number
  '"connection_requests": "$connection_requests", ' # number of requests made in connection
  '"pid": "$pid", ' # process pid
  '"request_id": "$request_id", ' # the unique request id
  '"request_length": "$request_length", ' # request length (including headers and body)
  '"remote_addr": "$remote_addr", ' # client IP
  '"remote_user": "$remote_user", ' # client HTTP username
  '"remote_port": "$remote_port", ' # client port
  '"time_local": "$time_local", '
  '"time_iso8601": "$time_iso8601", ' # local time in the ISO 8601 standard format
  '"request": "$request", ' # full path no arguments if the request
  '"request_uri": "$request_uri", ' # full path and arguments if the request
  '"args": "$args", ' # args
  '"status": "$status", ' # response status code
  '"body_bytes_sent": "$body_bytes_sent", ' # the number of body bytes exclude headers sent to a client
  '"bytes_sent": "$bytes_sent", ' # the number of bytes sent to a client
  '"http_referer": "$http_referer", ' # HTTP referer
  '"http_user_agent": "$http_user_agent", ' # user agent
  '"http_x_forwarded_for": "$http_x_forwarded_for", ' # http_x_forwarded_for
  '"http_host": "$http_host", ' # the request Host: header
  '"server_name": "$server_name", ' # the name of the vhost serving the request
  '"request_time": "$request_time", ' # request processing time in seconds with msec resolution
  '"upstream": "$upstream_addr", ' # upstream backend server for proxied requests
  '"upstream_connect_time": "$upstream_connect_time", ' # upstream handshake time incl. TLS
  '"upstream_header_time": "$upstream_header_time", ' # time spent receiving upstream headers
  '"upstream_response_time": "$upstream_response_time", ' # time spend receiving upstream body
  '"upstream_response_length": "$upstream_response_length", ' # upstream response length
  '"upstream_cache_status": "$upstream_cache_status", ' # cache HIT/MISS where applicable
  '"ssl_session_reused": "$ssl_session_reused", ' # TLS session reused
  '"ssl_cipher": "$ssl_cipher", ' # TLS cipher only OpenSSL 3.0 supported
  '"ssl_curve": "$ssl_curve", ' # TLS curve OpenSSL 1.0.2+ supported
  '"ssl_curves": "$ssl_curves", ' # TLS curves
  '"scheme": "$scheme", ' # http or https
  '"request_method": "$request_method", ' # request method
  '"server_protocol": "$server_protocol", ' # request protocol, like HTTP/1.1 or HTTP/2.0
  '"pipe": "$pipe", ' # “p” if request was pipelined, “.” otherwise
  '"gzip_ratio": "$gzip_ratio", '
  '"http_cf_ray": "$http_cf_ray"'
'}';
```

Next in your Nginx site vhost config file i.e. HTTPS vhost would be at `/usr/local/nginx/conf/conf.d/domain.com.ssl.conf`, you will need to add a new access_log line referencing the `log_format named = main_json`. The buffer and flush directives tell Nginx to use a memory buffer to write to access log every 256KB size or after 5 minutes for better performance. So you will need to do Nginx reload/restart to flush any memory buffered access logs to disk if you want to inspect latest log info.

```
access_log /home/nginx/domains/domain.com/log/access_log.json main_json buffer=256k flush=5m;
```

Normally, you would want to place it grouped with your existing access_log in your Nginx site vhost config file like.

```
access_log /home/nginx/domains/domain.com/log/access.log combined buffer=256k flush=5m;
access_log /home/nginx/domains/domain.com/log/access_log.json main_json buffer=256k flush=5m;
error_log /home/nginx/domains/domain.com/log/error.log;
```

Then restart Nginx server for changes to take affect
```
service nginx restart
```
or cmd shortcut
```
ngxrestart
```

You can use jq to filter just the Nginx metrics you want. Example
```
cat access_log.json | tail -1 | jq -r '"\(.time_local) \(.remote_addr) \(.http_x_forwarded_for) \(.request_uri) \(.status) \(.request_method) \(.http_host) \(.scheme) \(.server_protocol) \(.ssl_protocol) \(.ssl_cipher) \(.http_cf_ray) \(.http_user_agent)"'
03/May/2020:08:59:16 +0000 66.249.73.203 66.249.73.203 /threads/ovh-new-infrastructure-line-severs-intel-xeon-e-22xx-xeon-silver-amd-epyc-7371.18392/ 200 GET community.centminmod.com https HTTP/1.1 TLSv1.3 TLS_AES_256_GCM_SHA384 58d8c8f393bbe049-DFW Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```
Or find out the proportion of HTTPS SSL ciphers served to visitors
```
cat access_log.json | jq -r '.ssl_cipher' | sort | uniq -c | sort -rn
   3099 TLS_AES_256_GCM_SHA384
    171 ECDHE-ECDSA-AES256-GCM-SHA384
     22 ECDHE-ECDSA-CHACHA20-POLY1305
      2 ECDHE-ECDSA-AES128-SHA
```
HTTPS SSL protocols and ciphers served to visitors
```
cat access_log.json | jq -r '"\(.ssl_protocol) \(.ssl_cipher)"' | sort | uniq -c | sort -rn
   3099 TLSv1.3 TLS_AES_256_GCM_SHA384
    171 TLSv1.2 ECDHE-ECDSA-AES256-GCM-SHA384
     22 TLSv1.2 ECDHE-ECDSA-CHACHA20-POLY1305
      1 TLSv1 ECDHE-ECDSA-AES128-SHA
      1 TLSv1.1 ECDHE-ECDSA-AES128-SHA
```
HTTPS SSL protocols and HTTP status codes served to visitors
```
cat access_log.json | jq -r '"\(.ssl_protocol) \(.status)"' | sort | uniq -c | sort -rn
   2115 TLSv1.3 200
    478 TLSv1.3 301
    226 TLSv1.3 307
    150 TLSv1.2 200
    135 TLSv1.3 304
     76 TLSv1.3 303
     62 TLSv1.3 403
     25 TLSv1.2 304
      6 TLSv1.2 301
      5 TLSv1.3 404
      4 TLSv1.2 307
      3 TLSv1.2 403
      3 TLSv1.2 303
      2 TLSv1.2 400
      1 TLSv1 400
      1 TLSv1.3 405
      1 TLSv1.3 400
      1 TLSv1.1 400
```
HTTPS protocol and HTTP status codes for only urls = /login/login
```
cat access_log.json | jq -r 'select(.request_uri == "/login/login")| "\(.ssl_protocol) \(.status)"' | sort | uniq -c | sort -rn                             
     25 TLSv1.3 200
```

# Nginx JSON Format Logs with Cloudflare Proxy

If you have Cloudflare proxy in front of Nginx, you can alter the Nginx json log format added to /usr/local/nginx/conf/nginx.conf to below version for additional logged fields

`log_format named = cf_json`
```
log_format cf_json escape=json '{'
  '"msec": "$msec", ' # request unixtime in seconds with a milliseconds resolution
  '"connection": "$connection", ' # connection serial number
  '"connection_requests": "$connection_requests", ' # number of requests made in connection
  '"pid": "$pid", ' # process pid
  '"request_id": "$request_id", ' # the unique request id
  '"request_length": "$request_length", ' # request length (including headers and body)
  '"remote_addr": "$remote_addr", ' # client IP
  '"remote_user": "$remote_user", ' # client HTTP username
  '"remote_port": "$remote_port", ' # client port
  '"time_local": "$time_local", '
  '"time_iso8601": "$time_iso8601", ' # local time in the ISO 8601 standard format
  '"request": "$request", ' # full path no arguments if the request
  '"request_uri": "$request_uri", ' # full path and arguments if the request
  '"args": "$args", ' # args
  '"status": "$status", ' # response status code
  '"body_bytes_sent": "$body_bytes_sent", ' # the number of body bytes exclude headers sent to a client
  '"bytes_sent": "$bytes_sent", ' # the number of bytes sent to a client
  '"http_referer": "$http_referer", ' # HTTP referer
  '"http_user_agent": "$http_user_agent", ' # user agent
  '"http_x_forwarded_for": "$http_x_forwarded_for", ' # http_x_forwarded_for
  '"http_host": "$http_host", ' # the request Host: header
  '"server_name": "$server_name", ' # the name of the vhost serving the request
  '"request_time": "$request_time", ' # request processing time in seconds with msec resolution
  '"upstream": "$upstream_addr", ' # upstream backend server for proxied requests
  '"upstream_connect_time": "$upstream_connect_time", ' # upstream handshake time incl. TLS
  '"upstream_header_time": "$upstream_header_time", ' # time spent receiving upstream headers
  '"upstream_response_time": "$upstream_response_time", ' # time spend receiving upstream body
  '"upstream_response_length": "$upstream_response_length", ' # upstream response length
  '"upstream_cache_status": "$upstream_cache_status", ' # cache HIT/MISS where applicable
  '"ssl_protocol": "$ssl_protocol", ' # TLS protocol
  '"ssl_cipher": "$ssl_cipher", ' # TLS cipher
  '"scheme": "$scheme", ' # http or https
  '"request_method": "$request_method", ' # request method
  '"server_protocol": "$server_protocol", ' # request protocol, like HTTP/1.1 or HTTP/2.0
  '"pipe": "$pipe", ' # “p” if request was pipelined, “.” otherwise
  '"gzip_ratio": "$gzip_ratio", '
  '"http_cf_ray": "$http_cf_ray", '
  '"http_cf_worker": "$http_cf_worker", '
  '"http_cf_request_id": "$http_cf_request_id", '
  '"http_cf_railgun": "$http_cf_railgun", '
  '"http_accept": "$http_accept"'
'}';
```
and use this in nginx vhost adding a 2nd log for
`/home/nginx/domains/domain.com/log/access_log.json` using nginx `log format = cf_json`
```
access_log /home/nginx/domains/domain.com/log/access.log combined buffer=256k flush=5m;
access_log /home/nginx/domains/domain.com/log/access_log.json cf_json buffer=256k flush=5m;
error_log /home/nginx/domains/domain.com/log/error.log;
```