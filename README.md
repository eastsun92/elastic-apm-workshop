# Elastic APM workshop
- https://events.elastic.co/o11yseminar1

- https://docs.google.com/presentation/d/1lT6EWobXV34UgFGND7s9qUFHaLFHVlqQTmCfn4nOzgU

- https://cloud.elastic.co/registration


## 1. Scatter Plot (scatter.hjson)
- Vega
  * https://www.elastic.co/guide/en/kibana/current/vega.html
  * https://vega.github.io/vega/examples/
  * https://vega.github.io/vega-lite/examples/
- Discover
  * apm/link-to/transaction/{{value}}
- APM Index: traces-apm*, logs-apm.error*
- Distributed Tracing
  * Latency Correlation

- Track deployments with annotations
https://www.elastic.co/guide/en/kibana/current/transactions-annotations.html 

```
$ curl -X POST \
  ${KIBANA_URL:9243}/apm/services/${SERVICE_NAME}/annotation \ 
-H 'Content-Type: application/json' \
-H 'kbn-xsrf: true' \
-H 'Authorization: ApiKey ${API_KEY}' \ 
-d '{
      "@timestamp": "2024-02-27T00:00:00.000Z", 
      "service": {
        "version": "0.1" 
      },
      "message": "My first deployment" 
    }'
```
${API_KEY}: Kibana > Stack Management > API keys > Create..


## 2. RUM
https://www.elastic.co/blog/performing-real-user-monitoring-rum-with-elastic-apm


## 3. Anomaly Detection
- Import .csv file
- Ingest pipeline
- Create ML Job


## 4. ES|QL
https://www.elastic.co/guide/en/elasticsearch/reference/current/esql-getting-started.html 
