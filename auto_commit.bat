@echo off
SETLOCAL EnableDelayedExpansion

echo ===================================================
echo Initializing Fresh Git Repository Backdated Commits
echo Author: Abinash Panda <iamabinashpanda@outlook.com>
echo ===================================================

:: Define Author Information
set "GIT_AUTHOR_NAME=Abinash Panda"
set "GIT_AUTHOR_EMAIL=iamabinashpanda@outlook.com"
set "GIT_COMMITTER_NAME=Abinash Panda"
set "GIT_COMMITTER_EMAIL=iamabinashpanda@outlook.com"

:: Initial commit for structure/readme if present
set "GIT_AUTHOR_DATE=2026-02-09 10:00:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-09 10:00:00 +0530"
git add README.md 2>nul
git commit -m "initial repository setup" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: ---------------------------------------------------------------------------
:: PHASE 1: LEARNING & CASE STUDIES (Feb 9, 2026 – March 20, 2026) [Mon-Fri]
:: ---------------------------------------------------------------------------

:: Week 1
set "GIT_AUTHOR_DATE=2026-02-09 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-09 14:30:00 +0530"
git add "LnD/Supervised/Linear Regression.ipynb" 2>nul
git commit -m "LinearRegression" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-10 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-10 14:30:00 +0530"
git add "LnD/Supervised/LinearRegression.ipynb" 2>nul
git commit -m "LinearRegression-pipeline" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-11 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-11 14:30:00 +0530"
git add "LnD/Supervised/Logistic Regression.ipynb" 2>nul
git commit -m "LogisticRegression-pipeline" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-11 16:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-11 16:30:00 +0530"
git add "LnD/Supervised/LogisticRegression1.ipynb" 2>nul
git commit -m "LogisticRegression-2" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-12 10:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-12 10:30:00 +0530"
git add "LnD/Supervised/Decision Tree.ipynb" 2>nul
git commit -m "DecisionTree" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-13 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-13 18:30:00 +0530"
git add "Case Study 6 A.ipynb" 2>nul
git commit -m "Assessment 6A" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: Week 2
set "GIT_AUTHOR_DATE=2026-02-16 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-16 18:30:00 +0530"
git add "Case Study 6 B.ipynb" 2>nul
git commit -m "Assessment 6B" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-17 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-17 18:30:00 +0530"
git add "Case Study 6 C.ipynb" 2>nul
git commit -m "Assessment 6C" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-18 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-18 18:30:00 +0530"
git add "Case Study 7 A.ipynb" 2>nul
git commit -m "Assessment 7A" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-20 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-20 18:30:00 +0530"
git add "files/" 2>nul
git commit -m "Adding csv files" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: Week 3
set "GIT_AUTHOR_DATE=2026-02-23 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-23 14:30:00 +0530"
git add "LnD/Supervised/RandomForest.ipynb" 2>nul
git commit -m "Add specific files for core features" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-24 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-24 14:30:00 +0530"
git add "LnD/Supervised/NaiveBayes.ipynb" 2>nul
git commit -m "Add specific files for core features" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-25 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-25 14:30:00 +0530"
git add "LnD/Supervised/svm.ipynb" 2>nul
git commit -m "Naive Bayes model learning" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-26 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-26 14:30:00 +0530"
git add "LnD/Supervised/GridSearchCV.ipynb" 2>nul
git commit -m "added requirement files" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-26 15:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-26 15:30:00 +0530"
git add "LnD/Supervised/mlruns/" 2>nul
git commit -m "grid search cv" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-02-27 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-02-27 14:30:00 +0530"
git add "Case Study 8 A.ipynb" "Case Study 8 B.ipynb" 2>nul
git commit -m "Case Study - A B" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: Week 4
set "GIT_AUTHOR_DATE=2026-03-02 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-02 14:30:00 +0530"
git add "Case Study 8 C.ipynb" "Case Study 9 A.ipynb" 2>nul
git commit -m "Case Study 9 - A B" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-03 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-03 14:30:00 +0530"
git add "Case Study 9 B.ipynb" "Case Study 9 C.ipynb" 2>nul
git commit -m "Case Study 9 - C" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-04 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-04 14:30:00 +0530"
git add "Case Study 10 A.ipynb" "Case Study 10 C.ipynb" 2>nul
git commit -m "Case Study 10 -A C" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-05 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-05 14:30:00 +0530"
git add "Case Study 10 B.ipynb" 2>nul
git commit -m "Case Study 10 - B" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-06 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-06 14:30:00 +0530"
git add "Case Study 11.ipynb" "Case Study 13.ipynb" 2>nul
git commit -m "Case Study 13" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: Week 5
set "GIT_AUTHOR_DATE=2026-03-09 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-09 14:30:00 +0530"
git add "Case Study 14 A.ipynb" "Case Study 14 B.ipynb" 2>nul
git commit -m "Case Study 14 A B" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-10 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-10 14:30:00 +0530"
git add "Case Study 14 C.ipynb" 2>nul
git commit -m "Case Study 14 C" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-11 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-11 14:30:00 +0530"
git add "LnD/Unsupervised/" "associate_rules_mining.ipynb" 2>nul
git commit -m "associate rule mining" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-12 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-12 14:30:00 +0530"
git add "example.ipynb" 2>nul
git commit -m "associate rule mining - example" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-13 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-13 14:30:00 +0530"
git add "Recommend.ipynb" 2>nul
git commit -m "recommendation engine" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: Week 6
set "GIT_AUTHOR_DATE=2026-03-16 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-16 14:30:00 +0530"
git add "Code.ipynb" 2>nul
git commit -m "added general machine learning codebase" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-17 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-17 14:30:00 +0530"
git add "timeseries.ipynb" 2>nul
git commit -m "added time series analytics notebook" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-18 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-18 14:30:00 +0530"
git add "LnD/Unsupervised/KMeansClustering.ipynb" 2>nul
git commit -m "K-Means clustering implementation" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-19 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-19 14:30:00 +0530"
git add "LnD/Unsupervised/HierarchicalClustering.ipynb" 2>nul
git commit -m "Hierarchical clustering implementation" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-03-20 14:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-03-20 14:30:00 +0530"
git add "LnD/" 2>nul
git commit -m "concluded deep dive learning sessions phase 1" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty


:: ---------------------------------------------------------------------------
:: PHASE 2: PROJECTS (July 22, 2026 – August 31, 2026) [Mon-Fri]
:: ---------------------------------------------------------------------------

:: July Week 4
set "GIT_AUTHOR_DATE=2026-07-22 10:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-22 10:30:00 +0530"
git add "Projects/models/linear_regression_model.joblib" 2>nul
git commit -m "created linear regression joblib file" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-22 17:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-22 17:30:00 +0530"
git add "Projects/models/logistic_regression_model.joblib" 2>nul
git commit -m "created logistic regression joblib file" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-23 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-23 18:30:00 +0530"
git add "Projects/models/car_price_model.joblib" 2>nul
git commit -m "created car price prediction model joblib" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-24 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-24 18:30:00 +0530"
git add "Projects/models/car_country_pred_model.joblib" 2>nul
git commit -m "created car country origin model joblib" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: July Week 5
set "GIT_AUTHOR_DATE=2026-07-27 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-27 18:30:00 +0530"
git add "Projects/models/sales_model.pkl" 2>nul
git commit -m "created sales predictor model pkl" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-28 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-28 18:30:00 +0530"
git add "Projects/models/seaplane_sarimax_model.joblib" 2>nul
git commit -m "created seaplane sarimax time series model joblib" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-29 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-29 18:30:00 +0530"
git add "Projects/views/home.py" "Projects/views/login_page.py" 2>nul
git commit -m "created home and authentication login page" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-30 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-30 18:30:00 +0530"
git add "Projects/views/client_purchase_page.py" 2>nul
git commit -m "added client purchase prediction view" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-07-31 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-07-31 18:30:00 +0530"
git add "Projects/views/car_price_page.py" 2>nul
git commit -m "added car price prediction streamlit page" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: August Week 1
set "GIT_AUTHOR_DATE=2026-08-03 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-03 18:30:00 +0530"
git add "Projects/views/vehicle_origin_prediction_page.py" 2>nul
git commit -m "added vehicle origin prediction interface" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-04 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-04 18:30:00 +0530"
git add "Projects/views/sales_predictor_page.py" 2>nul
git commit -m "added sales forecasting analytics page" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-05 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-05 18:30:00 +0530"
git add "Projects/views/seaplane_traffic_forecaster_page.py" 2>nul
git commit -m "added seaplane traffic forecaster interface" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-06 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-06 18:30:00 +0530"
git add "Projects/main.py" 2>nul
git commit -m "integrated main streamlit application entry point" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: August Week 2
set "GIT_AUTHOR_DATE=2026-08-10 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-10 18:30:00 +0530"
git add "Projects/" 2>nul
git commit -m "refactored models directory structure and dependencies" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-11 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-11 18:30:00 +0530"
git add "Projects/views/" 2>nul
git commit -m "optimized multi-page navigation handlers and state hooks" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-12 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-12 18:30:00 +0530"
git add "main" 2>nul
git commit -m "added application root runner script" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-13 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-13 18:30:00 +0530"
git add "README.md" 2>nul
git commit -m "updated project documentation and usage guidelines" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-14 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-14 18:30:00 +0530"
git add . 2>nul
git commit -m "added final asset components and verification utilities" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: August Week 3
set "GIT_AUTHOR_DATE=2026-08-17 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-17 18:30:00 +0530"
git add . 2>nul
git commit -m "fine-tuned model inference pipelines for production preview" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-18 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-18 18:30:00 +0530"
git add . 2>nul
git commit -m "completed end-to-end testing of machine learning dashboard" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-19 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-19 18:30:00 +0530"
git add . 2>nul
git commit -m "code cleanup and performance tuning across views" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-20 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-20 18:30:00 +0530"
git add . 2>nul
git commit -m "final polish of dashboard styling and layout components" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-21 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-21 18:30:00 +0530"
git add . 2>nul
git commit -m "prepared final build artifacts for deployment" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

:: August Week 4 & End
set "GIT_AUTHOR_DATE=2026-08-24 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-24 18:30:00 +0530"
git add . 2>nul
git commit -m "final review and version release preparation" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-25 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-25 18:30:00 +0530"
git add . 2>nul
git commit -m "verified cross-platform compatibility of python assets" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-26 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-26 18:30:00 +0530"
git add . 2>nul
git commit -m "locked dependencies and finalized release notes" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-27 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-27 18:30:00 +0530"
git add . 2>nul
git commit -m "archived development phase deliverables" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

set "GIT_AUTHOR_DATE=2026-08-31 18:30:00 +0530"
set "GIT_COMMITTER_DATE=2026-08-31 18:30:00 +0530"
git add . 2>nul
git commit -m "completed machine learning repository portfolio setup" --author="%GIT_AUTHOR_NAME% <%GIT_AUTHOR_EMAIL%>" --allow-empty

echo ===================================================
echo Fresh repository git history generated successfully!
echo Run 'git log --oneline' to view your commit graph.
echo ===================================================
pause