import os
from nanonets import OCR

API_KEY = os.environ.get('NANONETS_API_KEY')
CATEGORIES = ['name', 'sex', 'date_of_birth', 'address', 'dl_number', 'issue_date', 'exp_date', 'class', 'height', 'restrictions', 'eyes']
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')

IMAGE_DIR = './images/'
ANNOTATION_DIR = './annotations/json/'

model = OCR(API_KEY, CATEGORIES, model_id=MODEL_ID)

images = [IMAGE_DIR + x for x in os.listdir(IMAGE_DIR)]
annotations = [ANNOTATION_DIR + x for x in os.listdir(ANNOTATION_DIR)]

images.sort()
annotations.sort()

training_dict = dict(zip(images, annotations))

response = model.train(training_dict)

print("NEXT RUN: export NANONETS_MODEL_ID=" + model.model_id)
print("NEXT RUN: python ./code/model-state.py")

