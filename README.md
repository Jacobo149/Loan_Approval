# Loan_Approval
Running an ML algorithm on the backend on Loan Approval dataset, will tell you if you are eligble for a loan.

# Loan_Approval Application
Trains a random forest algorithm from Scikit-learn Library (93% accuracy)  
Leveraging the Next.js framework, the application asks the user for independent variables and predicts whether a user is eligible for a loan  

## Issues Being Addressed
- Need to implement Fetch request to display on frontend
- Change sys calls instead to __init__ calls for reproducibility
- Refine UX
- Clean up code

## How To Run

### Prerequisites
Download necessary packages (Python, Javascript, numpy, pandas, scipy, sklearn, npm)  
Change sys() calls in server.py to proper the directory on deployer's machine
Change pd.read_csv() call in preprocess.py to the proper directory on deployer's machine

### Server Console Commands (Windows)
- Navigate to "server" directory  
- Activate Server VM
```
venv\Scripts\activate
```
- Run server.py
```
python .\server.py
```

### Client Console Commands (Windows)
- Navigate to "client" directory
- Run the frontend framework
```
npm run dev
```
