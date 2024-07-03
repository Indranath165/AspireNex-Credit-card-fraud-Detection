<h1>Credit Card Fraud Detection</h1>
This project involves building a machine learning model to identify fraudulent credit card transactions. It includes preprocessing and normalizing the transaction data, handling class imbalance issues, and splitting the dataset into training and testing sets. The project demonstrates the use of classification algorithms, such as Logistic Regression and Decision Tree Classifier, to classify transactions as fraudulent or genuine.
<br> <br>
<b>Check out the live demo of this application</b> <a href="https://aspirenex-credit-card-fraud-detection.streamlit.app/" target="_blank">here</a>.

<h2>Project Overview</h2>
Credit card fraud is a significant issue in the financial industry, leading to substantial financial losses each year. Detecting fraudulent transactions accurately is crucial for preventing these losses and protecting customers. This project aims to build a reliable model to identify fraudulent credit card transactions.

<h2>Objectives</h2>
<ol>
    <li><b>Data Preprocessing</b>: Clean and normalize the transaction data.</li>
    <li><b>Class Imbalance Handling</b>: Address the imbalance between fraudulent and genuine transactions.</li>
    <li><b>Model Building</b>: Train classification algorithms (Logistic Regression and Decision Tree Classifier) to detect fraudulent transactions.</li>
    <li><b>Model Evaluation</b>: Evaluate the models' performance using metrics like precision, recall, F1-score, and accuracy.</li>
    <li><b>Improvement Techniques</b>: Apply oversampling or undersampling techniques to improve model performance.</li>
</ol>
<h2>Dataset</h2>
The dataset used in this project is taken from Kaggle and consists of 29 key features used to determine whether a transaction is normal or fraudulent. It includes the following columns:
<ul>
    <li><b>Time</b>: Number of seconds elapsed between this transaction and the first transaction in the dataset.</li>
    <li><b>V1, V2, ..., V28</b>: Principal components obtained from PCA.</li>
    <li><b>Amount</b>: Transaction amount.</li>
    <li><b>Class</b>: Class label (1 = Fraudulent, 0 = Genuine).</li>
</ul>
You can find the dataset <a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud" target="_blank">here</a>.
<h2>Getting Started</h2>
To get a local copy up and running, follow these steps:
<ol>
    <li>Download or clone this repository in your local machine.</li>
    <li>Navigate to the project directory: <code>cd AspireNex-Credit-card-fraud-Detection</code>.</li>
    <li>Run the following command to install the required libraries: <code>pip install -r requirements.txt</code>.</li>
    <li>Run the Streamlit app:<code>streamlit run app.py</code>.</li>
</ol>
<h2>Model Evaluation</h2>
The models are evaluated using the following metrics:
<ul>
    <li><b>Accuracy</b>: The ratio of correctly predicted observations to the total observations.</li>
    <li><b>Precision</b>: The ratio of correctly predicted positive observations to the total predicted positives.</li>
    <li><b>Recall</b>: The ratio of correctly predicted positive observations to all the observations in the actual class.</li>
    <li><b>F1-Score</b>: The weighted average of Precision and Recall.</li>
</ul>
<h2>Contributions</h2>
Contributions are welcome! We value your input and encourage you to actively participate in the project. If you have any ideas, suggestions, bug reports, or feature requests, please don't hesitate to open an issue on GitHub. Additionally, we appreciate any code contributions you may have. If you'd like to contribute code, please submit a pull request, and we will review it as soon as possible. Thank you for your support!
