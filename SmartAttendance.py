# This is a basic code to read the image imagePath_ls and mark the attendance in a
# spreadsheet.

from pathlib import Path
import cv2 as cv
import datetime
import pandas as pd
import re
import pytesseract as tess
path = 'Tesseract-OCR/tesseract.exe'
tess.pytesseract.tesseract_cmd = path

# Reading the excel sheet containing the attendance
attendancePath = 'Attendance_list.csv'
attendance_df = pd.read_csv(attendancePath)

# Obtaining the list of student names
name_ls = list(attendance_df['Student names'])

# Reading the images
folder = Path('Attendance Screenshots').glob('*')
# Storing the paths of all the images in the folder
imgPath_ls = [imgPath for imgPath in folder]

# Getting the current date
currentDate = datetime.datetime.now()
date = currentDate.strftime('%d-%m-%Y')
# Adding a new column for the current date
attendance_df[date] = 0
#print(attendance_df)
for imgPath in imgPath_ls:
    # print(imgPath)
    img = cv.imread(str(imgPath),1)

    # Extracting the text from the image
    text = tess.image_to_string(img,lang='eng')

    for i,name in enumerate(name_ls):
        if re.search(name,text):
            attendance_df.loc[i,date] = 1

# Updating the excel sheet
attendance_df.to_csv('Attendance_list.csv',index=False)
#print(attendance_df)
    # cv.imshow('Attendance list',img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()