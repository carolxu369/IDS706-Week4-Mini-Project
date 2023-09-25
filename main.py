import statistics

def calculate(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)
    
    return mean, median, std_dev

if __name__ == "__main__":
    data = [15, 23, 43, 11, 5, 30, 8, 19, 7, 50, 28, 37, 14, 21, 9, 63, 31, 2, 45, 12]

    mean, median, std_dev = calculate(data)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
