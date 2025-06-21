# Module 2. Experiment Tracking with MLFlow

## Basics
Experiment: a collection of attempts to find the best model

Run: a single attempt to find the best model, involves evaluating a single or a set of models, and recording the results, the models, parameters, etc.

## MLFLow
Scope:
- experiment tracking
- model registry
- basic deployment

Out of scope:
- data versioning
- model monitoring

### Experiment tracking
Features:
- UI to visualize results, compare runs, etc. 
- autologging or manual logging of metrics, parameters, models, commit hashes, etc.
- tracking server (local or server-side)
- backend storage (SQL database)

Limitations:
- no authentication, use VPN to restrict access to servers if they are not deployed locally

### Model Registry
Features:
- model lineage: see the run the model is associated with and all relevant details
- versioning: a model with the same name can have multiple versions
- stage: staging, production, archive
- easily pull and deploy a model from the registry by specifying the model name, version, and stage
- for each model, also contains (automatically inferred, but editable) env requirements info

Limitations:
- does not deploy models automatically, build a CI/CD process on top of the model registry to achieve this