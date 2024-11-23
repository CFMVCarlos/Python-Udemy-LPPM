import json
import urllib.request

json_data_source: str = "Section8/temperature_anomaly.json"

with open(json_data_source, "r", encoding="utf-8") as jsonfile:
    anomalies: dict[str, dict[str, str | float]] = json.load(jsonfile)
print(anomalies["description"])
for year, value in anomalies["data"].items():
    print(f"{year}: {float(value):6.2f}")
print(anomalies["citation"])

#############################################################################################################################
print("*" * 80)
#############################################################################################################################

json_data_source: str = (
    "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"
)
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalies = json.loads(data)

for year, value in anomalies["data"].items():
    print(f"{year}: {float(value):6.2f}")
