from src.utils import read_file, filter_operations, sort_by_date, mask_card, mask_account

def main():
    read = read_file("operations.json")
    filtered = filter_operations(read)
    last = sort_by_date(filtered)
    #print(last)



if __name__ == '__main__':
    main()
