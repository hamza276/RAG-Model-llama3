FROM python: 3.10.0

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit run main.py"]
