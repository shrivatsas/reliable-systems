# reliable-systems

### To run the services

```
docker-compose up
```

### Endpoints can be found at

```
curl localhost:8080/docs
```

### To load test using ApacheBench

```
ab -n 1000 -c 5 localhost:8080/
```
