
# Lung Cancer Detector

"Lung Cancer Detector" is a web-based application, that is used 
for detection of lung cancer in a patient. The dataset has been trained using Random Forest Classifier, giving an accuracy (F1 score) of 81%


## Acknowledgements

 - [Random Forest Regressor Docs](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Dataset Link](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer)



## Tech Stack

**Client:** HTML, CSS, JS

**Server:** Flask, Python, PythonAnywhere


## Run Locally

Clone the project

```bash
  git clone https://github.com/ashutosh1808/Lung-Cancer-Prediction-Flask
```

Go to the project directory

```bash
  cd Lung-Cancer-Prediction-Flask
```

Install dependencies

```bash
  pip install flask
```
```bash
  pip install flask_mail
```


Start the server

```bash
  python app.py
```


## Features


- Authenticated
- Interactive
- Password is sent through mail
- Accurate Results (upto 81%)


## Optimizations

To improve the performance, the authentication feature has been added, and the user password is sent through mail. It can further be encrypted. 

After plotting the feature importance, there were some redundant features which were dropped in the final model. A few parameters would be added soon.


