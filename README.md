# ml-pipelines-using-dvc
Code of how to build a ml-pipeline using DVC

Instead of Wrting whole ML workflow in single file (emotion_detection.ipynb), we can write each part of workflow (data_ingestion, data_preprocessing, feature_engineering, model_building, model_evaluation etc.) in separate .py file, and later we can run whole workflow in form of pipeline (DVC Pipeline).

1. Install git
2. git init (git start tracking your folder) -----> check using "ls -a" from git CMD
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

# git tag V2.0

git add .
git commit -m "Add TF-IDF model"

git tag -a v2.0 -m "Release V2 with TF-IDF"  ## create tag localy

git push origin main
git push origin v2.0                         ## push tag into github

# git tag V3.0

git add .
git commit -m "Add TF-IDF model"

git tag -a v3.0 -m "Release V3 with BOW"   ## create tag localy

git push origin main
git push origin v3.0                       ## push tag into github

# show all commit, tag, brach in form of graph

git log --oneline --graph --all

* 0182015 (HEAD -> main, origin/main) update README.md second time
* a0f3f9f update README.md file
* 55f2fc0 (tag: v3.0) add BOW feature engineering steps
* eab9c1a (tag: v2.0) add TF-IDF in feature engineering step
* 4effc4c adding requirements.txt and update README.md file
* bc90a50 Initial Commit

# Checkout a Specific Git Tag

Suppose you are currently on the latest `main` branch.

```text
HEAD --> main (latest commit)
```

## Move to Tag `v2.0`

```bash
git checkout v2.0
```

After running this command:

- `HEAD` points to the commit tagged as `v2.0` (**Detached HEAD** state).
- All **Git-tracked files** (source code, README, configuration files, etc.) are restored to their `v2.0` version.
- You are no longer on the `main` branch.

Example:

```text
main
  |
A ---- B ---- C ---- D
       ^
     tag:v2.0
       ^
     HEAD
```

## What Happens to Data and Models?

Git only restores files that it **tracks**.

For example:

```text
project/
│
├── src/
├── README.md
├── data/
└── models/
```

- `src/` and `README.md` are restored to their `v2.0` version (if tracked by Git).
- `data/` and `models/` **do not change** if they are ignored using `.gitignore`.

This is because Git is designed for **source code versioning**, not for large datasets or trained machine learning models.

If your datasets and models are versioned using **DVC**, run:

```bash
dvc checkout
```

This restores the correct versions of the data and models for the checked-out Git commit.

## Move to Another Tag

```bash
git checkout v3.0
```

This restores all Git-tracked files to the `v3.0` version.

## Return to the Latest `main` Branch

```bash
git checkout main
```

This switches back to the latest commit on the `main` branch.

---

## Summary

```bash
# Move to tag v2.0
git checkout v2.0

# Restore DVC-tracked data/models (if using DVC)
dvc checkout

# Move to tag v3.0
git checkout v3.0
dvc checkout

# Return to the latest main branch
git checkout main
dvc checkout
```

> **Note:** Checking out a tag puts you in a **Detached HEAD** state because a tag is a fixed pointer to a specific commit, not a branch.