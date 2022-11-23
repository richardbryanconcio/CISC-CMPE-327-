FROM python:3.8.15-slim
RUN mkdir /qbay
WORKDIR /qbay
ADD . /qbay
RUN pip3 install -r requirements.txt
RUN chmod +x /qbay/wait-for-it.sh
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
