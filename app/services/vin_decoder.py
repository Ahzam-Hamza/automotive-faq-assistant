"""
VIN validation and decoding service.
"""

import logging
from app.core.cache import SimpleCache


class VINDecoder:
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cache = SimpleCache()  # ✅ Proper cache initialization

    def validate_vin(self, vin: str) -> bool:
        """
        Validate VIN structure.
        """

        if not vin:
            self.logger.warning("VIN validation failed: Empty VIN.")
            return False

        vin = vin.strip()

        if len(vin) != 17:
            self.logger.warning(f"VIN validation failed: Invalid length ({len(vin)}).")
            return False

        if not vin.isalnum():
            self.logger.warning("VIN validation failed: Non-alphanumeric characters found.")
            return False

        if any(char in vin for char in ["I", "O", "Q"]):
            self.logger.warning("VIN validation failed: Contains invalid characters (I, O, Q).")
            return False

        if vin != vin.upper():
            self.logger.warning("VIN validation failed: VIN must be uppercase.")
            return False
        
        self.logger.info(f"VIN validation successful for VIN: {vin}")
        return True


    def _extract_model_year(self, vin: str):
        """
        Extract model year from VIN (10th character).
        """

        year_map = {
            "1": 2001, "2": 2002, "3": 2003,
            "4": 2004, "5": 2005, "6": 2006,
            "7": 2007, "8": 2008, "9": 2009,
            "A": 2010, "B": 2011, "C": 2012, "D": 2013,
            "E": 2014, "F": 2015, "G": 2016, "H": 2017,
            "J": 2018, "K": 2019, "L": 2020, "M": 2021,
            "N": 2022, "P": 2023, "R": 2024, "S": 2025
        }

        year_code = vin[9]
        return year_map.get(year_code, "Unknown")


    def _extract_manufacturer(self, vin: str):
        """
        Extract manufacturer from VIN (first 3 characters).
        """

        wmi_map = {
            "1HG": "Honda (USA)",
            "1FA": "Ford (USA)",
            "1G1": "Chevrolet (USA)",
            "JHM": "Honda (Japan)",
            "WDB": "Mercedes-Benz (Germany)"
        }

        wmi_code = vin[0:3]
        return wmi_map.get(wmi_code, "Unknown Manufacturer")


    def decode(self, vin: str) -> dict:
        """
        Decode VIN to extract vehicle information.
        """

        # Validate first
        if not self.validate_vin(vin):
            return {
                "vin": vin,
                "error": "Invalid VIN"
            }

        # ✅ Check cache
        cached_result = self.cache.get(vin)
        if cached_result:
            self.logger.info(f"Cache hit for VIN: {vin}")
            return cached_result

        # Decode if not cached
        manufacturer = self._extract_manufacturer(vin)
        model_year = self._extract_model_year(vin)

        decoded_data = {
            "vin": vin,
            "manufacturer": manufacturer,
            "model_year": model_year
        }

        # ✅ Store in cache
        self.cache.set(vin, decoded_data)

        self.logger.info(f"VIN decoded and cached successfully for VIN: {vin}")

        return decoded_data
