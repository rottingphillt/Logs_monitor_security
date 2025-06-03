FROM python:3.10-slim

WORKDIR /app

COPY log_monitor.py .
COPY fake_syslog.log .

RUN mkdir -p /log_output

CMD ["python", "log_monitor.py"]
