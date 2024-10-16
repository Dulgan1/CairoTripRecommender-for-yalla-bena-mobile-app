# 🗺️ CairoTripRecommender-for-yalla-bena-mobile-app

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview: Key Functionalities


## 1. Project Overview
- **Objective**: Build a machine learning recommendation system for personalized travel planning in Cairo.
1. **Data Collection**: 
  - Scrape data on places, restaurants, hotels, and transportation in Cairo.
  - Clean and organize data on stay duration, location, price, reviews, and type (family, friends, solo).
2. **Filtering Preferences**: 
  - Filter data based on user preferences (type, interests, price).
  - Rank options by reviews and proximity.
3. **Model Development**: 
  - Develop collaborative filtering or content-based recommendation models.
  - Incorporate budget constraints for recommendations.
4. **Model Evaluation**: 
  - Use precision and recall to evaluate model performance.
  - Optimize for better personalized recommendations.
5. **API Development**: 
  - Create API endpoints for real-time integration with the Yalla Bena app.
  - Support dynamic itinerary suggestions and budget-aware planning.
This project aims to create a tailored travel experience for users exploring Cairo.

# Tools & Libraries Used

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Data Manipulation**: [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
3. **Numerical Computing**: [![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
4. **Data Visualization**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=plotly&logoColor=white)](https://matplotlib.org/) [![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white)](https://seaborn.pydata.org/)
5. **Logging**: [![Logger](https://img.shields.io/badge/Logging-4B8BBE?style=flat&logo=python&logoColor=yellow)](https://docs.python.org/3/howto/logging.html)
6. **Data Scraping**: [![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-FFD700?style=flat&logo=python&logoColor=black)](https://www.crummy.com/software/BeautifulSoup/)| [![Requests](https://img.shields.io/badge/Requests-005571?style=flat&logo=python&logoColor=white)](https://requests.readthedocs.io/en/latest/)
7. **Database**: [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
8. **Machine Learning Frameworks**:[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)|[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
9. **Recommendation Algorithms**: [![Collaborative Filtering](https://img.shields.io/badge/Collaborative%20Filtering-4B0082?style=flat&logo=cloudsmith&logoColor=white)](https://en.wikipedia.org/wiki/Collaborative_filtering)| [![Content-Based Filtering](https://img.shields.io/badge/Content--Based%20Filtering-008080?style=flat&logo=cloudsmith&logoColor=white)](https://en.wikipedia.org/wiki/Content-based_filtering)
10. **Model Evaluation**: [![Precision](https://img.shields.io/badge/Precision-FF6347?style=flat&logo=chart-line&logoColor=white)](https://en.wikipedia.org/wiki/Precision_and_recall)|[![Recall](https://img.shields.io/badge/Recall-4682B4?style=flat&logo=chart-line&logoColor=white)](https://en.wikipedia.org/wiki/Precision_and_recall)
11. **Web Framework**: [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
12. **Statistical Analysis**: [![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
13. **Version Control**: [![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)| [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/)
14. **Code Formatting & Linting**: [![Black](https://img.shields.io/badge/Black-000000?style=flat&logo=python&logoColor=white)](https://github.com/psf/black)
15. **Continuous Integration (CI)**: [![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)
16. **Environment Management**: [![Pip](https://img.shields.io/badge/Pip-005A8B?style=flat&logo=pypi&logoColor=white)](https://pip.pypa.io/en/stable/)
## Folder Organization

```

📁.github
└──
    └── 📁workflows
         └── 📃unittests.yml
└── 📁data
         └── 📃fun-things-to-do-in-cairo.csv
         └── 📃things-to-do-cairo-with-kids.csv
└── 📁notebooks
         └── 📃__init__.py
         └── 📓scrap.ipynb
└── 📁scripts
         └── 📃__init__.py
         └── 📃scarap_data.py
└── 💻src
    └── 📁dashboard-div
                    └── 📝app.py
                    └── 📝setup.py
└── ⌛tests
         └── 📃__init__.py

└── 📜.gitignore
└── 📰README.md
└── 🔋requirements.txt
└── 📇templates.py

```


### **Usage**

These modules are designed to be used in conjunction with each other to streamline the data analysis process, from data preparation and cleaning to in-depth analysis and model creation.

- **💻src**: The main source code of the project, including the Streamlit dashboard and other related files.

  - **📁dashboard-div**: Holds the code for the dashboard.
    - **📝app.py**: Main application file for the dashboard.
    - **📝README.md**: Documentation specific to the dashboard component.

- **⌛tests**: Contains test files, including unit and integration tests.

  - \***\*init**.py\*\*: Initialization file for the test module.

- **📜.gitignore**: Specifies files and directories to be ignored by Git.

- **📰README.md**: The main documentation for the entire project.

- **🔋requirements.txt**: Lists the Python dependencies required to run the project.

- **📇templates.py**: Contains templates used within the project, possibly for generating or processing data.

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/CairoTripRecommender-for-yalla-bena-mobile-app.git
```

2. Change directory

```bash
cd CairoTripRecommender-for-yalla-bena-mobile-app
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```

4. change directory to run the Flask app locally.

```bash
cd src
```

5. Start the Flask app

```bash
uvicorn dashboard-div.app:app --reload                           
```
6. go to the front end then run the html

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
