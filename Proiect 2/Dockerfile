FROM python:3.13-slim

WORKDIR /api

COPY ./ /api

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]