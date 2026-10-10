class ListNode:

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):

        return self.data


class LinkedList:

    def __init__(self):

        self.header = ListNode(None)
        self.count = 0

    def __repr__(self):

        curr = self.header.next
        output = []
        while curr is not None:
            output.append(curr.data)
            curr = curr.next
        output.append("None")
        return " -> ".join(output)


def destroy_list(lst):

    lst.header.next = None
    del lst


def insert_at_position(lst, position: int, node):

    if (position < 0) or (position > lst.count):
        return None
    prev = lst.header
    for _ in range(position):
        prev = prev.next
    node.next = prev.next
    prev.next = node
    lst.count += 1
    return 1


def remove_element(lst, value):

    if lst.count == 0:
        return None
    curr = lst.header.next
    prev = lst.header
    while True:
        if curr.data == value:
            prev.next = curr.next
            del curr
            lst.count -= 1
            return 1
        prev = curr
        curr = curr.next
        if curr is None:
            return 0


def search(lst, value):

    if lst.count == 0:
        return None
    index = 0
    curr = lst.header.next
    while index < lst.count:
        if curr.data != value:
            curr = curr.next
            index += 1
        else:
            return curr.data
    return 0


linked_list = None
list_created = False

def new_list():
    global list_created
    if list_created:
        print("You have already created a list.")
        return 0
    list_created = True
    global linked_list
    if linked_list is not None:
        delete_list()
    linked_list = LinkedList()
    print("List created successfully.")


def add_element(): # Inserts a new node at the given position; the nodes from that position onwards are shifted by one

    print("Enter the element value:\n")
    value = input()
    element = ListNode(data=value)
    while True:
        print("Choose the position to insert the element at:\n")
        try:
            position = int(input().strip())
            result = insert_at_position(linked_list, position, element)
            if result is None:
                print("Invalid position.")
            else:
                print(f"Element {value} inserted at position {position}.")
            break
        except ValueError:
            print("The position must be an integer.\n")
            continue


def delete_element(): # Deletes the first occurrence of the given value


    print("Enter the value of the element you want to delete:\n")
    value = input().strip()
    result = remove_element(linked_list, value)
    if result == 1:
        print("Element deleted successfully.\n")
    elif result is None:
        print("Your list is empty.\n")
    else:
        print("The value you entered does not exist in your list.")


def print_list():
    print(linked_list)


def search_list(): # Prints the given value if it is found in the list

    print("Enter the value of the element you are looking for:\n")
    value = input().strip()
    found = search(linked_list, value)
    if found is None:
        print("Your list is empty.\n")
    elif found == 0:
        print("The value is not in the list.")
    else:
        print(f"The value is in the list: {found}")


def delete_list():
    global linked_list
    global list_created
    if linked_list is None and not list_created:
        print("You do not have a list, there is nothing to delete.")
    else:
        destroy_list(linked_list)
        linked_list = None
        list_created = False
        print("List deleted successfully.")


while True:
    print("-----MENU-----\n"
          "Choose an option:\n"
          "1. Create a new list\n"
          "2. Delete the list\n"
          "3. Print the list\n"
          "4. Insert an element at a given position\n"
          "5. Delete an element with a given value\n"
          "6. Search the list for a given value\n"
          "7. Exit the program\n")

    try:
        choice = int(input().strip())
        if choice < 1 or choice > 7:
            print("Enter a valid option.\n")
            continue
    except ValueError:
        print("Enter a number as the option.\n")
        continue

    if choice == 7:
        print("Exiting the program...")
        break
    elif choice == 1:
        new_list()
    elif not list_created:
        print("Create a list first.")
        continue
    elif choice == 2:
        delete_list()
    elif choice == 3:
        print_list()
    elif choice == 4:
        add_element()
    elif choice == 5:
        delete_element()
    elif choice == 6:
        search_list()
