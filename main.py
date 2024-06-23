import pandas as pd
import statistics
import random
import matplotlib.pyplot as plt

# Specify the new path to the CSV file
file_path = r'G:\tree\medium_data.csv'

# Try to read the data and handle potential errors
try:
    # Read the data from the CSV file
    data = pd.read_csv(file_path, header=None)
    data = data[0]  # Assuming the data is in the first column

    # Convert data to numeric, forcing non-numeric values to NaN, then drop NaN values
    data = pd.to_numeric(data, errors='coerce')
    data = data.dropna()

    # Calculate the population mean
    population_mean = statistics.mean(data)

    def sample_mean(data, sample_size=30):
        """Take a random sample of the specified size from the data and return the mean."""
        sample = random.sample(list(data), sample_size)
        return statistics.mean(sample)

    def setup(data, iterations=100, sample_size=30):
        """Repeat the sampling process a specified number of times and store the means."""
        sample_means = []
        for _ in range(iterations):
            mean = sample_mean(data, sample_size)
            sample_means.append(mean)
        return sample_means

    def plot_graph(sample_means):
        """Plot a histogram of the sample means."""
        plt.hist(sample_means, bins=20, edgecolor='black')
        plt.xlabel('Sample Mean')
        plt.ylabel('Frequency')
        plt.title('Distribution of Sample Means')
        plt.axvline(statistics.mean(sample_means), color='r', linestyle='dashed', linewidth=1)
        plt.show()

    # Get the sample means
    sample_means = setup(data)

    # Plot the graph of sample means
    plot_graph(sample_means)

    # Calculate the mean of the sample means
    mean_of_sample_means = statistics.mean(sample_means)

    # Compare the mean of the sample means with the population mean
    print(f"Population Mean: {population_mean}")
    print(f"Mean of Sample Means: {mean_of_sample_means}")

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except PermissionError:
    print(f"Permission denied: {file_path}. Please check the file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
