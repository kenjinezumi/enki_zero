import requests
import time
import logging


def requests_data(url_api_call):
    """Function to request data.

    :params url_api_call: URL for the API call.
    """
    try:
        r = requests.get(url_api_call)
        r.raise_for_status()
        return r
    except requests.exceptions.Timeout:
        logging.info(f"{requests.exceptions.Timeout} has been thrown. "
                     f"We'll wait for one minute")
        time.sleep(60)
        self.get_real_estate_prices()

    except requests.exceptions.TooManyRedirects:
        raise Exception(
            f"{requests.exceptions.TooManyRedirects} exception has been raised. "
            f"You might want to try a different URL"
        )

    except request.exceptions.RequestException as e:
        logging.critical(
            f"Critical error has happened."
            f"System exiting."
            f"Error message: {e}"
        )
        raise SystemExit(e)
    except Exception as e:
        raise Exception(
            f"{e} exception has been raised."
        )






