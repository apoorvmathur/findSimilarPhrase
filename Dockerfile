FROM python:3.12
COPY . /opt/similar_phrases
WORKDIR /opt/similar_phrases
RUN python -m pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]