## Server 용 인증키 생성

* 이유: Excel TaskPane 은 보안정책상 인증된 HTTPS로의 요청만 수용.
  - openssl의 키는 위험한 것으로 판단하여 수용하지 않음
  - 해결책: `mkcert` 사용. 로컬호스트만 사용가능한 키를 새로 생성해줌
  - 참고: [mkcert](https://github.com/FiloSottile/mkcert)

### Mac

1. mkcert 설치

```bash
brew install mkcert
mkcert -install

# Created a new local CA 💥
# The local CA is now installed in the system trust store! ⚡️
```


2. `키체인 접근` 에서 `mkcert` 검색. 존재여부 확인

3. 다음 경로에 인증서 생성

```bash
mkdir server/.certs
mkcert localhost
```

4. Python 서버 실행

```bash
uvicorn server.main:app \
  --host 0.0.0.0 \
  --port 51000 \
  --ssl-keyfile=server/.certs/localhost-key.pem \
  --ssl-certfile=server/.certs/localhost.pem

# INFO:     Uvicorn running on https://0.0.0.0:51000 (Press CTRL+C to quit)
# INFO:     127.0.0.1:54007 - "POST /upload_csv/ HTTP/1.1" 200 OK
```

https로 서버가 실행된 것을 확인. 
