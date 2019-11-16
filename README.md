# Docker Creditability prediction API
Run flask app in docker conatainer

# Run in Docker
```
docker pull ramottamado/creditapp
docker run -d -p 5000:5000 ramottamado/creditapp
```
Go to localhost:5000

# Run from folder (Not Docker)
```
python run.py
```
Go to localhost:5000

# Usage

Send `POST` request to localhost:5000 with data like this:
`{
    "CustServ Calls":1,"Eve Mins":197.4,"Intl Mins":10.0,"VMail Message":25,
    "Intl Calls":3,"Night Mins":244.7,"Day Mins":265.1,
    "Int'l Plan":0
}`

output should be like this:
`{'results': {'creditability': 'Bad'}}`
