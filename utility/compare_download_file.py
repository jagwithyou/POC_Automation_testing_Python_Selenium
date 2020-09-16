import csv, xlrd, os, zipfile, shutil
from itertools import zip_longest

#defining Global Logger
logger = ''

def unzip_file(zip_file_path, Extract_folder_path):
    ''' Unzip a zip file to a giver path '''
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(Extract_folder_path)
    os.remove(zip_file_path)

def find_file_path(folder_path, extention):
    ''' Returns the complete file path having the giver extention '''
    for fname in os.listdir(folder_path):
        if fname.endswith(extention):
            return os.path.join(folder_path, fname)

def compare_csv_files(first_file_path, second_file_path):
    ''' Compare both the csv file '''
    #open both the file
    first_file = open(first_file_path, 'r')
    second_file = open(second_file_path, 'r')
    #read both the file with csv reader
    first_csv = list(csv.reader(first_file))
    second_csv = list(csv.reader(second_file))
    #check if both the files have same number of lines
    if len(first_csv) != len(second_csv):
        logger.exception("Total number of lines are not equal")
        return False
    #loop through all the lines and compare
    for row_first_csv,row_second_csv in zip(first_csv, second_csv):
        row_first_csv = list(filter(None, row_first_csv)) 
        row_second_csv = list(filter(None, row_second_csv)) 
        if "Date & Time" in row_first_csv:
            logger.info(f"Date Time Skip {row_first_csv}")
            continue
        if row_first_csv != row_second_csv:
            logger.exception(f"{row_first_csv} is not equal with {row_second_csv}")
            return False
    logger.info("CSV are equal")
    return True

def compare_excel_files(first_file_path, second_file_path):
    #Open both the file
    first_xlsx = xlrd.open_workbook(first_file_path)
    second_xlsx = xlrd.open_workbook(second_file_path)
    #Check if both the files have same number of sheets
    if len(first_xlsx.sheet_names()) != len(second_xlsx.sheet_names()):
        logger.exception(f"Sheet Number is not equal. File1 : {len(first_xlsx.sheet_names())}, File2 :  {len(second_xlsx.sheet_names())}")
    #Loop through all the sheets except first
    for i in range(1,len(first_xlsx.sheet_names())):
        sheet_first_xlsx = first_xlsx.sheet_by_index(i)
        sheet_second_xlsx = second_xlsx.sheet_by_index(i)
        #Check if both the sheets have same number of rows
        if sheet_first_xlsx.nrows != sheet_second_xlsx.nrows:
            logger.exception(f"Total number of rows of both the sheets are not similar. Sheet no : {i+1}")
        #Loop through the rows of the sheet and compare
        for rownum in range(max(sheet_first_xlsx.nrows, sheet_second_xlsx.nrows)):
            rows_first_xlsx = sheet_first_xlsx.row_values(rownum)
            rows_second_xlsx = sheet_second_xlsx.row_values(rownum)
            for colnum, (row_first_xlsx, row_second_xlsx) in enumerate(zip_longest(rows_first_xlsx, rows_second_xlsx)):
                if row_first_xlsx != row_second_xlsx:
                    logger.exception("Row {} Col {} - {} != {}".format(rownum+1, colnum+1, row_first_xlsx, row_second_xlsx))
                    return False
    #Log and return
    logger.info("XLSX are equal")
    return True

def compare_file(download_folder_path, expected_folder_path, log):
    global logger
    logger = log
    logger.info("File comparison started")
    #get the path of complete zip file
    zip_file_path = find_file_path(download_folder_path, '.zip')
    #cleaning the output folder
    output_folder_path = os.path.join(download_folder_path, 'output_files')
    if os.path.isdir(output_folder_path):
        shutil.rmtree(output_folder_path)
    #unzip files to output folder
    unzip_file(zip_file_path, output_folder_path)
    logger.info(f"Zip file extracted to {output_folder_path}")
    #compare csv
    expected_csv_output_file_path = find_file_path(expected_folder_path, '.csv')
    actual_csv_file_path = find_file_path(output_folder_path, '.csv')
    logger.info(f"Comparing CSV {expected_csv_output_file_path} vs {actual_csv_file_path}")
    csv_compare =  compare_csv_files(expected_csv_output_file_path, actual_csv_file_path)
    #Comparing Excel Files
    expected_xlsx_output_file_path = find_file_path(expected_folder_path, '.xlsx')
    actual_xlsx_file_path = find_file_path(output_folder_path, '.xlsx')
    logger.info(f"Comparing XLSX {expected_xlsx_output_file_path} vs {actual_xlsx_file_path}")
    xlsx_compare = compare_excel_files(expected_xlsx_output_file_path, actual_xlsx_file_path)
    if csv_compare and xlsx_compare:
        return True



# if __name__ == "__main__":
#     #get the path of complete zip file
#     folder_path = os.getcwd() + "/downloads"
#     zip_file_path = find_file_path(folder_path, '.zip')
#     #unzip the file to the output folder
#     output_folder_path = 'files/output_files'
#     unzip_file(zip_file_path, output_folder_path)
#     #compare csv
#     expected_output_path = 'files\expected_output_files\BOC-client-master-reconciliation-2020-07-00-26905.csv'
#     actual_file_path = find_file_path(output_folder_path, '.csv')
#     # output = compare_csv_files('D:/sulopa/Learning/python_selenium_automation_testing/code/project_folder/files/output_files/client-master-reconciliation-2020-07-49-46203.csv', 'D:/sulopa/Learning/python_selenium_automation_testing/code/project_folder/files/output_files/client-master-reconciliation-2020-07-49-46203.csv')
#     print(compare_csv_files(expected_output_path, actual_file_path))
#     res = compare_excel_files('D:\sulopa/automation_testing\cmr_automation\media\download\output_files\client-master-reconciliation-2020-07-13-8188.xlsx', 'D:\sulopa/automation_testing\cmr_automation\media\download\output_files\client-master-reconciliation-2020-07-13-8188.xlsx')
#     print(res)