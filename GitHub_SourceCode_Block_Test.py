import json
import logging
from datetime import datetime

class CustomerService:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.records = []

    def add_customer(self, customer_id: int, name: str) -> None:
        self.records.append({
            "customer_id": customer_id,
            "name": name,
            "created_at": datetime.utcnow().isoformat(),
        })

    def export_data(self, output_file: str) -> None:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(self.records, file, indent=2)