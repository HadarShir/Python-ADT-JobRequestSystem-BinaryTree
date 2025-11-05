from ADTs import *


class CPUNodes:
    # responsible for resource management using a linked list

    def __init__(self, capacity, nodes_number):
        # Defining the constructor according to the task and raising exceptions accordingly
        self.requested_capacity = 0  # Used to set a counter to get_available_cpu_capacity
        if not isinstance(nodes_number, int):
            raise TypeError
        if nodes_number <= 0:
            raise ValueError
        if not isinstance(capacity, int):
            raise TypeError
        if capacity < nodes_number:
            raise ValueError
        self.__nodes_number = nodes_number
        self.__capacity = capacity
        self.__cpu_nodes = LinkedList()

        # Adding nodes to the list according to the instructions in the question
        if self.__capacity % self.__nodes_number == 0:
            i = self.__nodes_number
            while i > 0:
                node_to_add = [int(self.__capacity / self.__nodes_number), int(self.__capacity / self.__nodes_number)]
                self.__cpu_nodes.add_at_start(node_to_add)
                i = i - 1
        else:
            i = self.__nodes_number - 1
            while i > 0:
                node_to_add = [int(self.__capacity // self.__nodes_number), int(self.__capacity // self.__nodes_number)]
                self.__cpu_nodes.add_at_start(node_to_add)
                i = i - 1
            last_node = [int(self.__capacity // self.__nodes_number + self.__capacity % self.__nodes_number),
                         int(self.__capacity // self.__nodes_number + self.__capacity % self.__nodes_number)]
            self.__cpu_nodes.add_at_end(last_node)

    def get_cpu_capacity(self):
        return self.__capacity

    def get_available_cpu_capacity(self):
        available_cpu_capacity = self.__capacity - self.requested_capacity
        return available_cpu_capacity

    def get_cpu_nodes(self):
        return self.__cpu_nodes.head

    def occupy_available_cpu_capacity(self, requested_capacity):
        # A function whose purpose is to update the linked list according to the resources
        curr_node = self.__cpu_nodes.head
        self.requested_capacity += requested_capacity  # counter for get_available_cpu_capacity
        while requested_capacity > 0:
            if curr_node.value[1] == requested_capacity:
                curr_node.value[1] = 0
                requested_capacity = 0
            elif curr_node.value[1] > requested_capacity:
                curr_node.value[1] = curr_node.value[1] - requested_capacity
                requested_capacity = 0
            elif curr_node.value[1] < requested_capacity:
                requested_capacity = requested_capacity - curr_node.value[1]
                curr_node.value[1] = 0

            curr_node = curr_node.next

    def free_occupied_cpu_capacity(self, freed_capacity):
        # A function whose purpose is to update the linked list according to the resources
        self.requested_capacity -= freed_capacity  # counter for get_available_cpu_capacity
        curr_node = self.__cpu_nodes.head
        while freed_capacity > 0 and curr_node is not None:
            if curr_node.value[1] < curr_node.value[0]:
                to_free = min(curr_node.value[0] - curr_node.value[1], freed_capacity)
                curr_node.value[1] += to_free
                freed_capacity -= to_free
            curr_node = curr_node.next

    def __repr__(self):
        return repr(self.__cpu_nodes)
