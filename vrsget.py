import requests
def getEventsOfMonior(monitorID):
    url = "https://www.vrs.de/index.php"
    params = {
        "eID": "tx_vrsinfo_departuremonitor",
        "i": monitorID #id of monitor
    }

    headers = {
        "Host": "www.vrs.de",
        "Cookie": "_pk_ref.1.bcd9=%5B%22%22%2C%22%22%2C1684601748%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.bcd9=b647ea25766b70fb.1684601748.; _pk_ses.1.bcd9=1; _fbp=fb.1.1684601748495.983568733",
        "Sec-Ch-Ua": "\"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.vrs.de/am/s/59a2db3e420a2a5064823955e7bf5138",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.get(url, params=params, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        events = data["events"]
        return(events)
    else:
        return("Request failed with status code:", response.status_code)

def getLinesOfMonitor(monitorID):
    events = getEventsOfMonior(monitorID)
    lines = [item['line'] for item in events]
    return(lines)

def getStopPointsOfMonitor(monitorID):
    events = getEventsOfMonior(monitorID)
    stopPoint = [item['stopPoint'] for item in events]
    return(stopPoint)

def getDeparturesOfMonitor(monitorID):
    events = getEventsOfMonior(monitorID)
    departure = [item['departure'] for item in events]
    return(departure)

def getLinesOfInput(event):
    lines = [item['line'] for item in event]
    return(lines)

def getStopPointsOfInput(event):
    StopPoints = [item['StopPoint'] for item in event]
    return(StopPoints)

def getStopPointsOfInput(event):
    StopPoints = [item['line'] for item in event]
    return(StopPoints)

def getDeparturesOfInput(event):
    Departures = [item['departure'] for item in event]
    return(Departures)
