"""
Recall service module.

Provides recall lookup functionality for vehicles based on VIN.
"""

import logging


class RecallService:
    """
    Service responsible for checking vehicle recalls.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Simulated recall database (mock data)
        self.recall_database = {
            "Honda": [
                {
                    "campaign_id": "HND-2023-001",
                    "issue": "Airbag inflator may rupture",
                    "severity": "High"
                }
            ],
            "Ford": [
                {
                    "campaign_id": "FRD-2022-014",
                    "issue": "Brake fluid leakage",
                    "severity": "Medium"
                }
            ]
        }

    def check_recalls(self, manufacturer: str) -> list:
        """
        Return recall information for a given manufacturer.
        """

        recalls = self.recall_database.get(manufacturer, [])

        if recalls:
            self.logger.info(f"Recalls found for manufacturer: {manufacturer}")
        else:
            self.logger.info(f"No recalls found for manufacturer: {manufacturer}")

        return recalls
