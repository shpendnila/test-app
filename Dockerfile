FROM python:3.8
WORKDIR /app/
COPY app ./app/
RUN pip3 install --no-cache-dir -r ./app/requirements.txt
ENV FLASK_APP=app.main
EXPOSE 6000
CMD ["python", "-m", "app.main"]

