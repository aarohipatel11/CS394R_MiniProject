import time
#credit to chatgpt for coding assistance

def main() -> None:
    start_time = time.time()
    # Dataset: scores and their frequencies
    scores = [60, 70, 80, 90]
    frequencies = [2, 3, 4, 1]

    # Total number of data points
    n = sum(frequencies)

    # Step 1: Calculate the mean
    total_score = sum(score * freq for score, freq in zip(scores, frequencies))
    mean = total_score / n

    # Step 2: Calculate the squared deviations and weighted sum
    squared_deviations = [(score - mean) ** 2 for score in scores]
    weighted_squared_deviations = [sd * freq for sd, freq in zip(squared_deviations, frequencies)]

    # Step 3: Calculate the variance
    variance = sum(weighted_squared_deviations) / n

    # Output results
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.6f} seconds")

if __name__ == '__main__':
    main()