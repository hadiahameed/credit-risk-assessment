# credit-risk-assessment
Predict whether a person will pay their credit loan or not

1. Download data from https://www.kaggle.com/datasets/laotse/credit-risk-dataset
2. Docker command:
```
docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=mypassword' -p 1401:1433 --name sqlserver -d mcr.microsoft.com/azure-sql-edge
```
3. 
