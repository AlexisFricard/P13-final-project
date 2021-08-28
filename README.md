## Project - Association of the Master II Contracts in French and European law of Poitiers

---
**Note:** You will not find all files in *"/static/assets/img/"* folder who's in charge to distribute the images localy

**Solution:** Put your School's backgrounds photos inside folder *"/static/assets/img/"*

---
* ## For Development:
Prerequisites:  
>pip  
>python3  
>git  
>PostgreSQL + local database  
>Docker (only for chat)

### Step 1 - Basique settings:
***After clone repo..*** 
  
**Inside *<word dir>/***
```bash
>> pip install virtualenv

>> python3 -m venv <ENV_NAME>
>> <ENV_NAME>\scripts\activate

>> pip install -r requirements.txt
```
### Step 2- Environments variables:
#### For Django
>* SECRET_KEY = <DJANGO_SECRET_KEY>
>```
>TIPS ! :
>You can generate secrets with secrets module  
>``` 

#### For Database (PostgreSQL)

>* DB_NAME = <POSTGRE_DB_NAME>  
>* DB_USER = <POSTGRE_DB_USER>  
>* DB_PASSWORD = <POSTGRE_DB_USER_PASSWORD>

#### For Bucket storage (Scaleway)

>* ACCESS_KEY_ID = <SCALEWAY_ACCESS_API_KEY>
>* SECRET_ACCESS_KEY = <SCALEWAY_SECRET_API_KEY>
>* BUCKET_NAME = <SCALEWAY_BUCKET_NAME>
>* S3_REGION_NAME = <SCALEWAY_BUCKET_REGION_NAME>

### Step 3 - How enable chat

***Setting up local Docker container on port 6379*** 
```bash
(env)../P13-final-project/>> pip install redis

(env)../P13-final-project/>> docker run -p 6379:6379 -d redis:5
```
### Set 4 - Install database models
```bash
(env)../P13-final-project/>> python3 manage.py migrate
(env)../P13-final-project/>> python3 manage.py makemigrations frontpage
(env)../P13-final-project/>> python3 manage.py migrate frontpage
```
### Set 5 - Create your superuser
```bash
(env)../P13-final-project/>> python3 manage.py createsuperuser
```
### Set 6 - Launch app localy
```bash
(env)../P13-final-project/>> python3 manage.py runserver --settings=mastercontrat.dev_settings
```
---
* ## For Production - *with* Heroku
*To come up*
```python
# TODO: Setting up EMAIL BACKENDS
```