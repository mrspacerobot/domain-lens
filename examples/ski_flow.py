"""Fictional example of a ski resort weather request."""
from dataclasses import dataclass

@dataclass
class WeatherReport:
    resort: str
    snowfall_cm: int

class RequestHandler:
    def __init__(self, service):
        self.service = service

    def handle(self, resort: str) -> str:
        report = self.service.report(resort)
        return f"{report.resort}: {report.snowfall_cm} cm fresh snow"

class SnowService:
    def __init__(self, gateway):
        self.gateway = gateway

    def report(self, resort: str) -> WeatherReport:
        snowfall = self.gateway.fetch(resort)
        return WeatherReport(resort, snowfall)

class WeatherGateway:
    def __init__(self, api):
        self.api = api

    def fetch(self, resort: str) -> int:
        return self.api.snowfall(resort)

class MockWeatherAPI:
    def snowfall(self, resort: str) -> int:
        return {"Snow Peak": 18, "Pine Ridge": 7}.get(resort, 0)
