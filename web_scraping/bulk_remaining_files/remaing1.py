import os

def main():
    i = 0
    path = 'C:/Users/ARSHI/Documents/Acadmics/python_practice_dsa_daa/web_scraping/bulk_remaining_files/remaing_folder'
    for file_name in os.listdir(path):
        my_dest = "word" + str(i) + ".doc"
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source,my_dest)
        i += 1

if __name__ == '__main__':
    main()
