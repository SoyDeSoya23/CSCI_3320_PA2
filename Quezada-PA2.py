"""
Program Title: Revised Heapsort
Author: Jonny Quezada
Class: CSCI 3320-850, Fall 2022
Assignment #2
Objective: To revise the original heapsort algorithm to heapsort ONLY the
elements within a user-specified range of values. All other elements are to
remain in their original positions.
"""


class HeapPriorityQueue:
    """
    CLASS: HeapPriorityQueue
    This class and the majority of its methods were obtained from the textbook.

    Some slight modifications were made:
    First, some unnecessary methods were omitted in this program for brevity.
    Second, anything that referenced the PriorityQueue class from the textbook was omitted and
    the adjusted HeapPriorityQueue class instead focuses only on the user-given array.
    Third, the _downheap() method was slightly modified as shown below; I did not rename it
    so that the clarity as to where it came from remained.
    Fourth, the _heapify() method was renamed to maxheap() for clarity.
    Fifth, the get_data() method was created to help access the _data attribute.
    Lastly, the heapsort() method was created to handle the heap sorting.
    """
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:  # changed from "<" to ">"
                    small_child = right
            if self._data[small_child] > self._data[j]:  # changed from "<" to ">"
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self, contents=[]):
        """
        Create a new priority queue.
        """
        self._data = contents
        self._sorted = []

    def get_data(self):
        return self._data

    def maxheap(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def heapsort(self):
        """
        METHOD heapsort:
        Modifies the _sorted attribute to contain the sorted _data array.
        After each iteration of maxheap() and remove_max(), the element
        gathered from remove_max() is moved to the _sorted array.

        OUTPUT:
        :return: the sorted array.
        """
        self._sorted = []
        length = len(self._data)
        for i in range(length):  # modify the empty _sorted array such that len(_sorted) == len(_data)
            self._sorted.append(i)
        for i in range(0, len(self._data)):  # perform maxheap until the last element
            if len(self._data) > 0:
                self.maxheap()  # perform maxheap on _data
                x = self.remove_max()  # assign the maximum to variable "x"; array _data is one element smaller
                self._sorted[length - 1 - i] = x  # move "x" to its respective position in the _sorted array
        return self._sorted

    def __len__(self):
        return len(self._data)

    def remove_max(self):
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item


def preservedIndices(array, low, high):
    """
    FUNCTION preservedIndices:
    Creates an array containing all the indices of elements which fall out of the
    specified range between parameters "low" and "high".

    INPUT PARAMETERS:
    :param array: The array in which to traverse; the original unmodified array from the user.
    :param low: An integer given by the user specifying the lower bound of the range.
    :param high: An integer given by the user specifying the upper bound of the range.

    OUTPUT:
    :return: the array of indices.
    """
    indices = []
    for i in range(len(array)):  # this logic captures all indices which should be preserved
        if array[i] <= low:
            indices.append(i)
        elif array[i] >= high:
            indices.append(i)
    return indices


def getActualArray(original, excluding):
    """
    FUNCTION getActualArray:
    Creates an array containing all the elements of which indices
    are not in the array of indices created by the function preservedIndices.

    INPUT PARAMETERS:
    :param original: The array in which to traverse; the original unmodified array from the user.
    :param excluding: An array created from calling the preservedIndices function; contains indices.

    OUTPUT:
    :return: An array containing only those elements which should be sorted.
    """
    new = []
    for i in range(len(original)):
        if i not in excluding:  # if the index "i" is not one that should be preserved, append to the new array
            new.append(original[i])
    return new


def strToList(string):
    """
    FUNCTION strToList:
    Converts a string of comma-separated integers into an array.

    INPUT PARAMETERS:
    :param string: The string in which to convert to an array; given from user input.

    OUTPUT:
    :return: An array containing all the desired integers.
    """
    string = string.split(',')  # use the comma as the delimiter, the split method creates the array
    for i in range(len(string)):
        string[i] = string[i].strip()  # strips any accidental space between numbers
        string[i] = int(string[i])  # since the array elements are strings, convert to integer
    return string


def getFinalSorted(original, excluding, sorted_temp):
    """
    FUNCTION getFinalSorted:
    Creates an array containing all the user inputted integers;
    all integers that needed to be sorted were sorted and all integers
    whose position needed to be preserved is maintained.

    INPUT PARAMETERS:
    :param original: The original unmodified array from the user.
    :param excluding: An array created from calling the preservedIndices function; contains indices.
    :param sorted_temp: An array containing the sorted elements within the user-specified range.

    OUTPUT:
    :return: The final sorted array.
    """
    p = 0  # counter to increment the index of the sorted_temp arra
    for i in range(len(original)):
        if i in excluding:  # preserves the positions for those elements out of the specified range
            pass
        else:
            original[i] = sorted_temp[p]
            p += 1
    return original


if __name__ == "__main__":
    """
    Prompt for general input.
    Continuously asks the user if they would like to enter another array to heapsort
    within a specified range.
    
    Sample Run:
    -----------------------------------------------
    Enter the array elements comma separated (ex: 1,2,3): 21, 57, 35, 44, 51, 14, 6, 28, 39, 15
    Low: 20
    High: 51
    The original array is:  [21, 57, 35, 44, 51, 14, 6, 28, 39, 15]
    The Maxheap of those elements within the specified range is:  [44, 39, 21, 28, 35]
    The final sorted array is:  [21, 57, 28, 35, 51, 14, 6, 39, 44, 15]
    Would you like to enter another array of values to sort? (enter y/n): n
    -----------------------------------------------
    Program done!
    """
    while True:
        print("-----------------------------------------------")

        prompt = input("Enter the array elements comma separated (ex: 1,2,3): ")
        low = int(input("Low: ").strip())
        high = int(input("High: ").strip())

        # Convert the string input into an array:
        prompt = strToList(prompt)

        print("The original array is: ", prompt)

        # Create an array that contains the indices of those elements to not change:
        preserve = preservedIndices(prompt, low, high)

        # Create a temporary array that only contains those elements within the specified range:
        actual_list = getActualArray(prompt, preserve)

        # Create a heap object and print the Maxheap before the sorting:
        heap = HeapPriorityQueue(contents=actual_list)
        heap.maxheap()
        print("The Maxheap of those elements within the specified range is: ", heap.get_data())

        # Perform the sorting and print out the final sorted list:
        new_list = heap.heapsort()
        last = getFinalSorted(prompt, preserve, new_list)
        print("The final sorted array is: ", last)

        # Ask the user if they would like to repeat this process for another array:
        question = input("Would you like to enter another array of values to sort? (enter y/n): ").strip().lower()
        while question != 'y' and question != 'n':
            question = input('Enter (y/n): ')
        if question == 'n':
            break
    print("-----------------------------------------------")
    print("Program done!")
