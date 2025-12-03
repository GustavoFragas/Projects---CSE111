def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    print(f"reversed: {reverse_list(fruit_list)}")

    print(f"appended: {append_orange(fruit_list)}")

    print(f"replaced: {insert_cherry_before_apple(fruit_list)}")

    print(f"removed: {remove_banana(fruit_list)}")

    print(f"popped: {pop_and_print_last_element(fruit_list)}")

    print(f"sorted: {sort_list(fruit_list)}")

    print(f"cleared: {clear_list(fruit_list)}")


def clear_list(lst):
    lst.clear()
    return lst


def sort_list(lst):
    lst.sort()
    return lst

def pop_and_print_last_element(lst):
    last_element = lst.pop()
    print(f"popped element: {last_element}")
    return lst

def remove_banana(lst):
    lst.remove("banana")
    return lst

def insert_cherry_before_apple(lst):
    index = lst.index("apple")
    lst.insert(index, "cherry")
    return lst
        
def append_orange(lst):
   lst.append("orange")
   return lst

def reverse_list(lst):
   
   lst.reverse()
   return lst

if __name__ == "__main__":
    main()