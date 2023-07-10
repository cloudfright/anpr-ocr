import cv2
import logging
import time
import datetime
from paddleocr import PaddleOCR

class PlateReader(object):

    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)
        self.reader = PaddleOCR(use_angle_cls=True, show_log=False, lang='en') # need to run only once to download and load model into memory
     

    def read_plate(self,filenames):

      logging.debug(f"Plate READER - numfiles to read {len(filenames)}")
      
      results = []
      for filename in filenames:

        logging.debug(f"reading - {filename}")
        result = self.reader.ocr(filename, cls=True)
        logging.debug(f"result: {result}")

        if len(result) > 0 and len(result[0]) > 0:
          for idx in range(len(result)):
            res = result[idx]
            # print (res)
            results.append((datetime.datetime.now(), "filename", res[1][0], res[1][1]))

      results.sort(key=lambda tup: tup[3], reverse=True)
      for result in results:
        # print(result)
        logging.debug(f"Plate READER - OCR results: {results}")   
      

print("Plate READER - testing")
# plate_reader = PlateReader()
# plate_reader.read_plate(["./images/ir-image1.jpg"])