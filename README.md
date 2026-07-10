# ml-pipelines-using-dvc
Code of how to build a ml-pipeline using DVC

Instead of Wrting whole ML workflow in single file (emotion_detection.ipynb), we can write each part of workflow (data_ingestion, data_preprocessing, feature_engineering, model_building, model_evaluation etc.) in separate .py file, and later we can run whole workflow in form of pipeline (DVC Pipeline).

1. Install git
2. git init (git start tracking your folder)
3. python -m pip install dvc
4. dvc init (dvc start tracking your folder)
5. dvc repro (for run pipeline)
6. dvc dag (for getting pipeline graph)
7. dvc metrics show