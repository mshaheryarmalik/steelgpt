class EnergyConsumptionEstimator:
    def __init__(self):
        # Arbitrary constants for energy consumption
        self.GOOGLE_SEARCH_ENERGY = 1  # Arbitrary energy units for one Google search
        self.WEB_SCRAPING_ENERGY = 2  # Arbitrary energy units for one web scraping operation
        self.SMALL_GPT_MODEL_ENERGY = 5  # Arbitrary energy units for one inference with a small GPT model
        self.LARGE_GPT_MODEL_ENERGY = 15  # Arbitrary energy units for one inference with a large GPT model
        self.LARGE_GPT_MODEL_ATTEMPTS_ACCURATE_INFO = 2 # Even if we take two searches for Large model to get same information


    def estimate_energy_consumption_small(self, num_google_searches):
        total_energy_consumed = (
            num_google_searches * self.GOOGLE_SEARCH_ENERGY +
            num_google_searches * self.WEB_SCRAPING_ENERGY +
            self.SMALL_GPT_MODEL_ENERGY
        )
        return total_energy_consumed
    
    def estimate_energy_consumption_large(self):
        total_energy_consumed = (
            self.LARGE_GPT_MODEL_ENERGY * self.LARGE_GPT_MODEL_ATTEMPTS_ACCURATE_INFO
        )
        return total_energy_consumed