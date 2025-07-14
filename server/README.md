## Checklist

1. localhost pem key is generted inside `./server/.certs`

## How to run

```bash
# (Optional) Enable python
source ./server/.venv/bin/activate

# From root
PYTHONPATH=./server uvicorn main:app \
  --host 0.0.0.0 \
  --port 51000 \
  --ssl-keyfile=server/.certs/localhost-key.pem \
  --ssl-certfile=server/.certs/localhost.pem
```