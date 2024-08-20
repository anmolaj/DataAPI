# 
FROM python:3.10.11

# 
WORKDIR /work

# 
COPY ./app /work/app
COPY ./requirements.txt /work/requirements.txt

# Install Requirements
RUN pip install --no-cache-dir --upgrade -r /work/requirements.txt


# 
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8081"]