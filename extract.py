import kaggle
import os

# Set kaggle API credentials directory
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/niran/.kaggle'

# Specify the dataset(s) identifier
dataset = 'piterfm/paris-2024-olympic-summer-games'

# Set the download path
download_path = "./src"

# Remove existing files in the folder to prevent duplicates or outdated files
for file in os.listdir(download_path):
    file_path = os.path.join(download_path,file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(f"Deleted {file_path}")

    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# Download the dataset using the Kaggle API and unzip the files
kaggle.api.dataset_download_files(dataset=dataset,path=download_path,unzip=True)

# List of CSV files imported
csv_files = [file for file in os.listdir(download_path) if file.endswith(".csv")]
print(csv_files)