FROM python:3.12.3

RUN mkdir app
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["index.py" ]