FROM python:3.7-slim

RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'
RUN apt-get update && apt-get install
ADD requirements.txt .

EXPOSE 8501
RUN pip install -r requirements.txt
CMD streamlit run Alfaaz.py