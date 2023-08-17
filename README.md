4th July 2023
Raj Simpi

SpaCy model and NLTK model have been commited as separete files
OS library is required to be imported and chages related to that need to be made.  

26th June 2023
Aditya Sinha

The dataset from kaggle (https://www.kaggle.com/datasets/rhtsingh/general-table-recognition-dataset) has been cleaned and separated as test and train images. All the images have 512x512 dimension and are padded from all 4 sides.

The annotations denote the presence of tables in the images. The images look pure black but they are made up of 2 different pixel values, 0 and 1 (on a scale of 0-255. As a result both 0 valued and 1 valued pixels look similar to naked eyes but machines can distinguish them). The place where tables are present are filled with 1 while non-table spaces are filled with 0.

Train the images on Table Transformer. 
