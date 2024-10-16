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
The CairoTripRecommender repository is dedicated to building a machine learning-based recommendation system for personalized travel planning in Cairo. This project includes various stages, from data collection to model deployment, aimed at delivering real-time, tailored trip suggestions within the Yalla Bena app. Below is a detailed breakdown of the planned technical approach and tasks:

1. **Data Collection & Preparation** 
- **Data Sources**: Scrape and aggregate data from websites listing places, restaurants, and hotels in Cairo, ensuring only Cairo-specific information is retained. 
**Data Processing**: 
- - - Extract and clean data fields such as staying time, location, price, reviews, type (family, friends, solo), and keywords that reflect the interests of each location. 
- - - Gather transportation data (public and private) to include price, distance, and stop times between places.  
- **Output**: Cleaned and structured datasets ready for use in machine learning, encompassing both location details and transportation information.

2. **Preference-Based Data Filtering** 
- **Filtering Logic**: 
- - - Apply user-defined preferences such as place type, interests, and price range to the data. 
- - - Implement a ranking mechanism to prioritize locations with the highest reviews and closest proximity when multiple options share similar attributes (e.g., price). 
- **Output**: A filtered, personalized dataset that prioritizes places most aligned with the user’s preferences.

3. **Recommendation Model Development** 
- **Model Selection**: Build a collaborative filtering or content-based model to generate personalized recommendations for places, activities, and dining options based on user preferences and behavior. 
**Budget Constraints**: Incorporate budget allocation rules (e.g., 20% transportation, 40% activities, 20% restaurants, 20% hotels) to refine the recommendation process based on user-defined budgets. 
- **Output**: A trained recommendation model capable of suggesting a cohesive itinerary, tailored to user interests and budgetary constraints.

4. **Model Evaluation & Optimization** 
- **Evaluation Metrics**: Utilize precision and recall to assess the relevancy and accuracy of recommendations. 
- **Optimization**: Fine-tune the model based on evaluation results, making adjustments to improve personalized recommendations. 
- **Output**: An optimized recommendation system that aligns closely with user preferences, providing relevant travel suggestions.

5. **API Development for Front-End Integration** 
- **API Design**: Create endpoints for real-time interaction between the recommendation engine and the Yalla Bena app, allowing users to receive dynamic itinerary suggestions. 
- **Data Delivery**: Ensure the API supports features like activity and transportation recommendations, as well as budget-aware itinerary planning. 
- **Output**: An API interface that seamlessly connects the recommendation engine to the app, providing users with a smooth, interactive travel planning experience.

This project focuses on building a reliable, responsive, and adaptable recommendation engine, from data preparation to API integration, specifically tailored for the Cairo travel experience.




# Tools & Libraries Used

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Data Manipulation**: [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
3. **Numerical Computing**: [![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
4. **Data Visualization**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=plotly&logoColor=white)](https://matplotlib.org/) [![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white)](https://seaborn.pydata.org/)
5. **Logging**: [![Logger](https://img.shields.io/badge/Logging-4B8BBE?style=flat&logo=python&logoColor=yellow)](https://docs.python.org/3/howto/logging.html)
6. **Data Scraping**: 
- - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- - [Requests](https://requests.readthedocs.io/en/latest/)
7. **Database**: [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

8. **Machine Learning Frameworks**:
- - [Scikit-learn](https://scikit-learn.org/stable/)
- - [TensorFlow](https://www.tensorflow.org/) (if using deep learning models)

9. - **Recommendation Algorithms**: 
  - -  Collaborative Filtering
  - -  Content-Based Filtering

10.  **Model Evaluation**: 
  - Precision, Recall, and other metrics for model assessment

11. **Web Framework**: [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

12. **Statistical Analysis**: [![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)

13. **Version Control**: 
- -  [Git](https://git-scm.com/) 
- -  [GitHub](https://github.com/)
14. **Code Formatting & Linting**: [![Black](https://img.shields.io/badge/Black-000000?style=flat&logo=python&logoColor=white)](https://github.com/psf/black)
15. **Continuous Integration (CI)**: [![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)
16. **Environment Management**: 
- - [pip](https://pip.pypa.io/en/stable/)
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
