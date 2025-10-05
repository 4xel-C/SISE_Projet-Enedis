# SISE-Projet-Enedis
Master’s Year 2 Python – ML Project on Classifying Housing Energy Performance Certificate (DPE) Ratings in France.

To do:
- [ ] Data extraction from APIs.
- [ ] Data preparation.
- [ ] Machine learning models training.
- [ ] Vizualisation.
- [ ] Frontend.
- [ ] API Routes.

## Project structure
```
mon_projet/
│
├── app.py                     # Main streamlit app launcher.
├── requirements.txt
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
│
├── pages/                     # Pages from streamlit.
│   ├── 1_Visualisation.py
│   ├── 2_Modele_ML.py
│   └── 3_Analyse_API.py
│
├── src/                       # Main code.
│   ├── data_requesters        # Requesters for data on external APIs.
│   │   ├── api_requesters.py
│   │   └── helper.py
│   └── api.py/                # FastAPI routes for the application.
│       └── main.py            # main FastAPI file to run the back-end API routes.
│
├── MLmodels/                    # trained ml models.
│   ├── model1.pkl
│   └── ...
├── assets/                    # assets for streamlit app.
├── data/                      # data storage (will contains a sample for test).
└── notebooks/                 # ipython noteboks for exploration.                     
```