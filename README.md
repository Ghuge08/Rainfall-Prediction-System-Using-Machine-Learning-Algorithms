# Rainfall-Prediction-System-Using-Machine-Learning-Algorithms

To get the access of the full code and dataset just click on the my-new-branch branch. The detailed desscription of the project is given below.
The main intution behind this project is to learn about the various machine learning algorithms and practically implement them. The Dataset is fetched from the kaggle , you can directly download from here or this is the [link](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)

#### Folder structure
Go to my-new-branch, there are two folders, dataset which contains dataset and another is model, which contain all the code.

The project consist of the following steps:

#### Preprocessing
In this phase, null values were removed to ensure data integrity. Outlier detection was performed; however, as it eliminated significant variations in the data, we decided not to proceed with it. Since this is a classification problem, identifying the most relevant features for the target variable was crucial. To achieve this, a correlation matrix was plotted for feature selection.

#### Model Building and Training
Six models were trained on the dataset: Random Forest Classifier, Decision Tree Classifier, Support Vector Machine, Gaussian Naive Bayes, and an ensemble learning technique (Adaboost). Among these, Adaboost demonstrated the best performance. Consequently, a `.pkl` file was generated using the Adaboost model, and a user interface (UI) was developed based on it. The image below showcases the performance evaluation of the models.


![Screenshot 2024-12-25 212736](https://github.com/user-attachments/assets/01e766fb-cc46-47e7-9782-691c1efd7922)

The UI is made with streamlit library with the integration of the best selected model. The UI will look like
![image](https://github.com/user-attachments/assets/5aea19c1-ef19-4818-9e1d-ce9e14ca5933)
Just enter the detailes and hit that predict button , it will show the output.

