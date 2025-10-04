# SISE-Projet-Enedis
Master’s Year 2 Python – ML Project on Classifying Housing Energy Performance Certificate (DPE) Ratings in France.

To be implemented:
- [ ] Data extraction from APIs.
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
│   ├── api
│   │   ├── api_requesters.py
│   │   ├── api_routes.py
│   │   └── helper.py
│   ├── models.py/        
│
├── models/                    # trained ml models.
│   ├── model1.pkl
│   └── ...
├── assets/                    # assets for streamlit app.
```