from ingestion.image_preprocessor import ImagePreprocessor

processor = ImagePreprocessor()

output = processor.preprocess("data/raw/image.jpg")

print(output)