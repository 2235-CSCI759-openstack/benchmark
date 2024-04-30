import requests
import statistics
import time

def make_api_calls(endpoint, num_calls, payload_size):
    responses = []
    for _ in range(num_calls):
        response = requests.post(endpoint, json={"payload_size": payload_size})
        if response.status_code == 200:
            responses.append(response.json())
            time.sleep(0.1)
    return responses

def process_data(data):
    # Extract the values you want to analyze from the JSON data
    values = [entry['commTime'] for entry in data]
    # Calculate mean, min, max, and standard deviation
    mean_value = statistics.mean(values)
    min_value = min(values)
    max_value = max(values)
    std_deviation = statistics.stdev(values)
    return mean_value, min_value, max_value, std_deviation

if __name__ == "__main__":
    endpoint = "http://192.168.1.210:32774"
    num_calls = 100
    payload_size = 200
    
    responses = make_api_calls(endpoint, num_calls, payload_size)
    print(responses)
    if responses:
        mean, minimum, maximum, std_dev = process_data(responses)
        print("Mean:", mean)
        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Standard Deviation:", std_dev)
    else:
        print("No valid responses received.")
