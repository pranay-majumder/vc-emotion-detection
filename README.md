# ml-pipelines-using-dvc
Code of how to build a ml-pipeline using DVC

Instead of Wrting whole ML workflow in single file (emotion_detection.ipynb), we can write each part of workflow (data_ingestion, data_preprocessing, feature_engineering, model_building, model_evaluation etc.) in separate .py file, and later we can run whole workflow in form of pipeline (DVC Pipeline).

1. Install git
2. git init (git start tracking your folder)
3. python -m pip install dvc
4. dvc init (dvc start tracking your folder)
5. dvc repro (for run pipeline)
6. dvc dag (for getting pipeline graph)
7. dvc metrics show (dvc must track metrics.json then only we can use this command)

# git push

1. git status
2. git add .
3. git commit -m "<commit_message>"
4. create one public git repo (vc-emotion-detection)
4. git remote add origin "<https_link_of_repo>"
5. git branch
6. git push -u origin main

# Installl Dependency

1. python -m pip freeze > requirements.txt