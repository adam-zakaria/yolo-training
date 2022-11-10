# On remote machine
import fiftyone as fo

# A name for the dataset
name = "nightowls"

# The type of the dataset being imported
dataset_type = fo.types.COCODetectionDataset  # for example

# The directory containing the source images
#data_path = "/usr/src/datasets/n100t/base/images"

data_path = "/usr/src/raw_datasets/nightowls/nightowls_training"
# The path to the COCO labels JSON file
labels_path = "/usr/src/raw_datasets/nightowls/nightowls_training.json"

# Import the dataset
dataset = fo.Dataset.from_dir(
            dataset_type=fo.types.COCODetectionDataset,
                data_path=data_path,
                    labels_path=labels_path,
                    max_samples=10,
                        name=name)

session = fo.launch_app(dataset,remote=True)


