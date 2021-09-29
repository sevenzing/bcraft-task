# Run

```bash
docker build . -t bcraft_stats
docker run -it -p 8000:8000 bcraft_stats
```

service will start at localhost:8000

# Communicate

## Create statistic
```bash
curl -X POST \
  http://localhost:8000/api/statistic/ \
  -H 'content-type: application/json' \
  -d '{
	"date": "2021-09-29", 
	"views": 40, 
	"clicks": 1, 
	"cost": 1
}'
```

## Show statistics

```bash
curl -X GET \
  'http://localhost:8000/api/statistic/?from=2021-09-29&to=2021-10-09'
```

## Delete everything


```bash
curl -X DELETE \
  http://localhost:8000/api/statistic/
```