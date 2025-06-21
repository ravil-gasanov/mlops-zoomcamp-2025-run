# Monitoring

## Types
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

## Approach to implementing monitoring
- make use of what the company already has in place and build on top of that
- maybe build a simple dashboard using e.g. a BI tool, before trying to fully automate monitoring

- monitor in batch, even if you have an online prediction service
- i.e. log inputs, outputs, and then run monitoring batch jobs

## Evidently
- column mapper
- report(metrics...)
- some important metrics: drift in prediction column, drift in dataset, number of missing values
- or just use DataDriftPreset to use pre-defined metrics
- report.run(reference_data = train data, current_data = incoming (or val data for dev purposes))