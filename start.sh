#!/bin/bash
echo "Starting ITUS Semantic Portal..."
echo "PORT is set to: $PORT"

# Ensure PORT is set and not a reserved port
if [ -z "$PORT" ]; then
    echo "PORT not set, using default 8000"
    PORT=8000
fi

# Check if port is in reserved range and use alternative
if [ "$PORT" -eq 18012 ] || [ "$PORT" -eq 18013 ] || [ "$PORT" -eq 19099 ]; then
    echo "Detected reserved port $PORT, using 8000 instead"
    PORT=8000
fi

echo "Using port: $PORT"
exec python -m uvicorn app:app --host 0.0.0.0 --port $PORT