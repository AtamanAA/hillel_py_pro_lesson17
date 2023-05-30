import csv
from datetime import datetime

from django.utils import timezone

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_file_path = "log/log_file.csv"

        execution_time = datetime.now(tz=timezone.utc)
        request_path = request.path
        request_method = request.method

        log = Log(
            execution_time=execution_time,
            request_path=request_path,
            request_method=request_method,
        )
        log.save()

        def file_is_empty(file_path):
            with open(file_path, "r") as file:
                csv_dict = [row for row in csv.DictReader(file)]
                if len(csv_dict) == 0:
                    return True
                return False

        with open(log_file_path, mode="a") as csvfile:
            fieldnames = ["execution_time", "request_path", "request_method"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if file_is_empty(log_file_path):
                writer.writeheader()
            writer.writerow(
                {
                    "execution_time": execution_time,
                    "request_path": request_path,
                    "request_method": request_method,
                }
            )

        response = self.get_response(request)
        return response
