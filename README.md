# IP Location Lookup

This is a Python script that uses the [iplocate.io API](https://iplocate.io/) to retrieve the location details (such as country, city, and coordinates) of a given IP address.

## How to Use

1. Install the required Python package:
    ```bash
    pip install requests
    ```

2. Download the script and add your API key and IP address.

3. Run the script:
    ```bash
    python ip_location_lookup.py
    ```

The script will output a nicely formatted JSON object containing the location details of the provided IP address.

## API Limits

Please note that the **iplocate.io API** allows **up to 1000 requests per day** for all users combined. This means if the limit is reached, the API will not return any data until the next day.

## Disclaimer

This tool is provided **as-is**. The author is **not responsible for any misuse or issues** that arise from using this script or the IP data retrieved. Please make sure you comply with all relevant laws and regulations when using this tool.

## 💡 Got suggestions or improvements? Open a pull request or issue on GitHub!
