FROM registry.uid.ir/uid/python:3
WORKDIR /app
ADD exporter.py .
RUN pip3 install prometheus_client
RUN pip3 install requests
CMD [ "python3", "-u","./exporter.py" ]
