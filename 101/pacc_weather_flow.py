import httpx
from prefect import flow, task

@task()
def fetch_weather(lat: float, lon: float):
    """get weather data from open-meteo"""
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    return most_recent_temp

@task()
def save_weather(temp: float):
    """save temperature to csv"""
    with open("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Successfully wrote temp"

@flow()
def pipeline(coord: list):
    """iterate over list of dictionaries containing latitude and longitude, append weather result to csv. """
    results = []
    for i in coord:
        lat = i['lat']
        lon = i['lon']
        temp = fetch_weather(lat, lon)
        results.append(temp)
    save_weather(results)
    return results


if __name__ == "__main__":
    """create list of dictionaries for 3 locations"""
    coordinates = [{'lat': 40.1, 'lon':-60.0}, {'lat':42.4, 'lon':-65.0}, {'lat':36.3, 'lon':-51.2}]
    pipeline(coordinates)
