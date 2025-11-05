from ADTs import *
from CPUNodes import CPUNodes
from Job import Job


class JobRequestSystem:
    # A class representing a request
    def __init__(self, nodes_number=5, system_capacity=30):
        # Defining the constructor according to the task and raising exceptions accordingly
        self.__nodes_system_capacity = CPUNodes(system_capacity, nodes_number)
        self.__initialized_job_container = Queue()
        self.__waiting_job_container = Stack()
        self.__storage_stack = Stack()

    def get_nodes_system_capacity(self):
        return self.__nodes_system_capacity

    def get_initialized_jobs(self):
        return self.__initialized_job_container

    def get_waiting_jobs(self):
        return self.__waiting_job_container

    def request_new_job(self, job_description="", job_rank=1, job_request_resources=1):
        # A function representing a new request
        # The function checks the value, and creates a type from the class Job or raise an error
        try:
            self.job_description = job_description
            self.job_rank = job_rank
            self.job_request_resources = job_request_resources
            if job_request_resources > self.__nodes_system_capacity.get_cpu_capacity():
                raise RuntimeError(f"Job's requested resources exceeds the maximal number of cpu")

            else:
                request_new_job = Job(job_description, job_rank, job_request_resources)
                return request_new_job
        except RuntimeError as error:
            print(error)

    def request_job_resources(self, job_request):
        # A function that handles a new request.
        # If the request is from Job type, it checks the number of resources and handles according to the waiting list.
        # If it is not a work type, raise an error accordingly.
        try:
            if not isinstance(job_request, Job):
                raise ValueError(f"'NoneType' object has no attribute 'get_job_requested_resources'")

            if self.__waiting_job_container.is_empty():
                if job_request.get_job_requested_resources() <= self.__nodes_system_capacity.get_available_cpu_capacity():
                    self.__nodes_system_capacity.occupy_available_cpu_capacity(job_request.get_job_requested_resources())
                    self.__initialized_job_container.enqueue(job_request)
                    print(f"Requested resources for Job {job_request.get_id()} have been initialized.")
                else:
                    self.__waiting_job_container.push(job_request)
                    print(f"Requested resources for Job {job_request.get_id()} must wait for available resources.\n"
                          f"Consider terminating the current request and trying lower resources\n"
                          f"Meanwhile you will be waiting for available resources")
            else:
                for i in range(self.__waiting_job_container.size()):
                    if self.__waiting_job_container.peek().get_rank() >= job_request.get_rank():
                        curr_v = self.__waiting_job_container.pop()
                        self.__storage_stack.push(curr_v)
                    else:
                        break
                self.__waiting_job_container.push(job_request)
                for i in range(self.__storage_stack.size()):
                    curr_v = self.__storage_stack.pop()
                    self.__waiting_job_container.push(curr_v)
                if self.__waiting_job_container.peek().get_job_requested_resources() <= self.__nodes_system_capacity.get_available_cpu_capacity():
                    self.__nodes_system_capacity.occupy_available_cpu_capacity(job_request.get_job_requested_resources())
                    self.__initialized_job_container.enqueue(job_request)
                    self.__waiting_job_container.pop()
                    print(f"Requested resources for Job {job_request.get_id()} have been initialized.")
                else:
                    print(f"Requested resources for Job {job_request.get_id()} must wait for available resources.\n" 
                          f"Consider terminating the current request and trying lower resources\n" 
                          f"Meanwhile you will be waiting for available resources")
        except ValueError as error:
            print(error)

    def terminate_job(self, job_request_id):
        while not self.__waiting_job_container.is_empty():
            curr_v = self.__waiting_job_container.pop()
            self.__storage_stack.push(curr_v)
            if curr_v.get_id() == job_request_id:
                result = self.__storage_stack.pop()
                break
        while not self.__storage_stack.is_empty():
            curr_v = self.__storage_stack.pop()
            self.__waiting_job_container.push(curr_v)
        return result

    def execute_job(self):
        if self.__initialized_job_container.len != 0:
            first_rec = self.__initialized_job_container.dequeue()
            self.__nodes_system_capacity.free_occupied_cpu_capacity(first_rec.get_job_requested_resources())
            print(f"The current job with the id: {first_rec.get_id()} is being executed....\n"
                  f"The Job with the id {first_rec.get_id()} has finished executing successfully.")
        while not self.__waiting_job_container.is_empty() and self.__nodes_system_capacity.get_available_cpu_capacity() >= self.__waiting_job_container.peek().get_job_requested_resources():
            self.request_job_resources(self.__waiting_job_container.pop())

    def total_waiting_requested_job_resources(self):

        total_waiting_requested_job_resources = 0

        # Transferring the values in the original stack to the temporary stack and sum the values
        while not self.__waiting_job_container.is_empty():
            job = self.__waiting_job_container.pop()
            total_waiting_requested_job_resources += job.get_job_requested_resources()  # sum the values
            self.__storage_stack.push(job)

        # Returning the values to the original stack
        while not self.__storage_stack.is_empty():
            self.__waiting_job_container.push(self.__storage_stack.pop())

        return total_waiting_requested_job_resources

