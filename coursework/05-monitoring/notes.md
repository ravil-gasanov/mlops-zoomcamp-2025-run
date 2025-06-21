# Monitoring

## Monitoring types
Core:
- Service health
    - uptime
    - memory
    - latency
- Model performance
    - depends on the setting, e.g. it can be precision/recall for classification problems, etc.
- Data quality and integrity
    - e.g. number/percentage of missing values, value ranges, etc.
- Data and concept drift
    - monitor distribution changes in input, output, and P(y|X)

Additional:
- Performance by segment
- Fairness
- Outliers
- Explainability

## Strategies to implement monitoring
- make use of what the company already has in place and build on top of that
- maybe build a simple dashboard using e.g. a BI tool, before trying to fully automate monitoring

- monitor in batch, even if you have an online prediction service
- i.e. log inputs, outputs, and then run monitoring batch jobs

## Implement a monitoring job
1. Build an evidently report (map columns, define metrics)
2. Build a test suite
3. Build a flow (e.g. with Prefect) that:
    a. Loads new data and predictions to your database
    b. Calculates and logs defined metrics
    c. Run the test suite
4. Build a dashboard (e.g. with Grafana)
5. Set up alerts (not covered in the module)