class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        indiv_wait_time_sum = 0
        chef_free_time = 0
        for customer in customers:
            arrival, order = customer

            start_time = max(chef_free_time, arrival)
            finish_time = start_time + order

            indiv_wait_time_sum += finish_time - arrival
            
            chef_free_time = finish_time

        avg = indiv_wait_time_sum / len(customers)
        return avg