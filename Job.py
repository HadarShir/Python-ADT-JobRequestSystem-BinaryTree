
from functools import total_ordering

@total_ordering
class Job:
    # In the class definition we will create private fields and raise errors according to the task.
    last_job_id = 0

    def __init__(self, job_description, job_rank, job_request_resources):
        # Defining the constructor according to the task and raising exceptions accordingly
        self.__job_id = Job.last_job_id
        self.__description = job_description
        self.__rank = job_rank
        self.__job_request_resources = job_request_resources
        Job.last_job_id += 1

        if not isinstance(self.__job_id, int):
            raise TypeError("Invalid job_id value, must be int")
        if self.__job_id < 0:
            raise ValueError("Invalid job_id value, must be positive int.")

        if not isinstance(self.__description, str):
            raise TypeError("Invalid description value, must be str")

        if not isinstance(self.__rank, int) :
            raise TypeError("Invalid rank value, must be int")
        if self.__rank <= 0:
            raise ValueError("Invalid rank value, must be positive int.")

        if not isinstance(self.__job_request_resources, int) :
            raise TypeError("Invalid job_request_resources value, must be int")
        if self.__job_request_resources <= 0:
            raise ValueError("Invalid job_request_resources value, must be positive int.")



    def __repr__(self):
        return f"ID: {self.__job_id}, Rank: {self.__rank}, Resources: {self.__job_request_resources}"

    def get_description(self):
        return self.__description

    def get_id(self):
        return self.__job_id

    def get_job_requested_resources(self):
        return self.__job_request_resources

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        if not isinstance(new_rank, int):
            raise TypeError("Invalid rank value, must be int")
        if new_rank <= 0:
            raise ValueError("Invalid rank value, must be positive int.")
        self.__rank = new_rank

    def set_description(self, new_description):
        if not isinstance(new_description, str):
            raise TypeError("Invalid description value, must be str")
        self.__description = new_description

    def set_job_requested_resources(self, new_job_requested_resources):
        if not isinstance(new_job_requested_resources, int):
            raise TypeError("Invalid request resources value, must be int")
        if new_job_requested_resources <= 0:
            raise ValueError("Invalid request resources value, must be positive int.")
        self.__job_request_resources = new_job_requested_resources

    def __eq__(self, other):
        return self.__rank == other.__rank

    def __ne__(self, other):
        return self.__rank != other.__rank

    def __lt__(self, other):
        return self.__rank < other.__rank

    def __le__(self, other):
        return self.__rank <= other.__rank

    def __gt__(self, other):
        return self.__rank > other.__rank

    def __ge__(self, other):
        return self.__rank >= other.__rank
