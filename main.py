from utils import get_data, filter_data, sort_data, format_data


def main():
    data = get_data()
    data = filter_data(data)
    data = sort_data(data)
    data = format_data(data)

    for operation in data:
        print(operation)

    #print(data)


if __name__ == "__main__":
    main()
