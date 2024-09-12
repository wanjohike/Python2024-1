# to save to a csv file, we use the CSV module
import csv

with open('C:/Users/user/Desktop/files/results.csv', 'w', newline="") as results:
    writer = csv.writer(results) 
    # using the writerows() function fuction to write new rows/data into our csv file
    # writer.writerow(['Names', 'English', 'Mathematics', 'Programming', 'Science'])
    # writer.writerow(['Ahmed', '80', '77', '89', '47'])
    # writer.writerow(['Bronson', '98', '78', '86', '39'])
    # writer.writerow(['Erick', '74', '98', '87', '49'])
    # writer.writerow(['Hayan', '98', '87', '88', '46'])
    # writer.writerow([['Aria', '100', '90', '90', '100']])
    
    # 
    student_results = [
        ['Names', 'English', 'Mathematics', 'Programming', 'Science'],
        ['Ahmed', '80', '77', '89', '47'],
        ['Bronson', '98', '78', '86', '39'],
        ['Erick', '74', '98', '87', '49'],
        ['Hayan', '98', '87', '88', '46'],
        ['Aria', '100', '90', '90', '100']
    ]
    
    writer.writerows(student_results)
    
    # using the csv.Dict
    
    student_dict = [
        {
            'Name' : 'Broson',
            'English' : '40',
            'Mathematics' : '50'
        },
        {
            'Name' : 'Hayan',
            'English' : '60',
            'Mathematics' : '70'
        }
    ]
    
    # Extract the columns
    table_columns = ['Name', 'English', 'Mathematics']
    
    # Open the file
    with open('C:/Users/user/Desktop/files/results1.csv', 'w', newline="") as results1:
        writer = csv.DictWriter(results1, fieldnames=table_columns)
        writer.writeheader()
        writer.writerows(student_dict)
    
    