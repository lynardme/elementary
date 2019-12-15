def main():
    cur = [1,2,3,4]
    print(update_list('hello',cur))

def update_list(*args,current_list=[]):
    for value in args:
        current_list.append(value)
    return current_list

if __name__ == '__main__':
    main()
