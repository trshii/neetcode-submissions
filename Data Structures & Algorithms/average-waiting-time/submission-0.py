class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        indiv_wait_time = []
        chef_free_time = 0
        for customer in customers:
            arrival, order = customer

            start_time = max(chef_free_time, arrival)
            finish_time = start_time + order

            indiv_wait_time.append(finish_time - arrival)
            
            chef_free_time = finish_time

        avg = sum(indiv_wait_time) / len(customers)
        return avg