#!/usr/bin/env bash
# Bold Guide — static site server (local dev)
APP_PORT=${APP_PORT:-3001}
cd "$(dirname "$0")"
python3 -m http.server "$APP_PORT"
