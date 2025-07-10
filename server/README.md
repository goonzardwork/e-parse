## How to run

```bash
# From root
uvicorn server.main:app \
  --host 0.0.0.0 \
  --port 51000 \
  --ssl-keyfile=server/.certs/localhost-key.pem \
  --ssl-certfile=server/.certs/localhost.pem
```