import time
from typing import Any

import requests


class Ademe_API_requester:
    """
    A class to interact with the ADEME API.
    """

    # Class attributes: base URLs for different datasets
    base_url_existant = (
        "https://data.ademe.fr/data-fair/api/v1/datasets/dpe03existant/lines"
    )
    base_url_neuf = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe02neuf/lines"

    def __init__(
        self,
        size: int = 2500,
        max_retries: int = 3,
        backoff_factor: int = 2,
    ) -> None:
        """Initializes the Ademe_API_requester class.

        Args:
            size (int, optional): The number of results to return per page. Defaults to 2500.
            max_retries (int, optional): The maximum number of retry attempts for API requests. Defaults to 3.
            backoff_factor (int, optional): The backoff factor for retry delays. Defaults to 2.
        """
        self.params = {"size": size}
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def __get_data(self, url: str, params: dict[str, Any] | None = None) -> dict | None:
        """Private method to get the crude data from the API passing the base URL and parameters.

        Returns:
            dict: The JSON response from the API or an error message.
        """
        for attempt in range(self.max_retries):
            if attempt > 0:
                print(f"Retrying... ({attempt}/{self.max_retries})")

            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Raise an error for bad responses.
                return response.json()

            except Exception as e:
                print(f"Error fetching data: {e}")
                if attempt == self.max_retries - 1:
                    raise  # Re-raise the exception if max retries reached.
                else:
                    # Exponential backoff before the next retry.
                    wait_time = self.backoff_factor**attempt
                    print(f"Waiting for {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
        # endfor

    def get_existant_bydepartement(self, departement: int) -> list[dict[str, Any]]:
        """Retrieve existing building data by department.

        Args:
            departement (int): The department code to filter by.

        Returns:
            list[dict[str, Any]]: A list of dictionaries containing the building data.
        """
        # Build the parameter dictionary from the new department argument.
        params = self.params | {"qs": f"code_departement_ban:{departement}"}

        # Initialize the all_data list to get all the data from the pagination loop.
        all_data: list[dict[str, Any]] = []

        url = self.base_url_existant

        # Pagination loop.
        while url:
            data = self.__get_data(url, params=params)
            all_data.extend(data["results"])
            url = data.get("next")  # Get the next page URL.
            params = None  # Clear params for subsequent requests.
        # endwhile

        return all_data
