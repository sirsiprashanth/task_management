FROM python:3.10.7

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --trusted-host pypi.python.org --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./api /api/app

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80",  "--reload"]