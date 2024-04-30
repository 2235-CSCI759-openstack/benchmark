import requests
import statistics

def make_api_calls(endpoint, num_calls):
    responses = []
    for _ in range(num_calls):
        response = requests.get(endpoint)
        if response.status_code == 200:
            responses.append(response.json())
    return responses

def process_data(data):
    # Extract the values you want to analyze from the JSON data
    values = [entry['value'] for entry in data]
    # Calculate mean, min, max, and standard deviation
    mean_value = statistics.mean(values)
    min_value = min(values)
    max_value = max(values)
    std_deviation = statistics.stdev(values)
    return mean_value, min_value, max_value, std_deviation

if __name__ == "__main__":
    endpoint = "YOUR_ENDPOINT_URL_HERE"
    num_calls = int(input("Enter the number of API calls: "))
    
    responses = make_api_calls(endpoint, num_calls)
    if responses:
        mean, minimum, maximum, std_dev = process_data(responses)
        print("Mean:", mean)
        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Standard Deviation:", std_dev)
    else:
        print("No valid responses received.")
