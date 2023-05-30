from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from dotenv import dotenv_values

def make_client(mcc_id="") -> GoogleAdsClient:
    """
    :param mcc_id: this is the ID of the MCC the user is attached to. If the User has direct access to an account,
    don't pass a value here. If the user only has access to an account via an MCC. Pass through the MCC ID here.
    :return: GoogleAdsClient
    """
    config = dotenv_values("C:\Dev GoogleAdsAPI\google-ads-api-samples\.env.example")
    print(config)  # Add this line to check the config dictionary
    credentials = {
        "developer_token": config["developer_token"],
        "refresh_token": config["refresh_token"],
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "use_proto_plus": True
    }
    google_ads_client = GoogleAdsClient.load_from_dict(credentials, version="v10")
    if mcc_id != "":
        google_ads_client.login_customer_id = mcc_id
    return google_ads_client


if __name__ == "__main__":
    try:
        make_client()
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
