FROM python:3.9

WORKDIR /streamlit
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . /streamlit

# Intentionally do not expose port 8501 or else people can circumvent login

RUN pip install -r requirements.txt

CMD streamlit run app.py