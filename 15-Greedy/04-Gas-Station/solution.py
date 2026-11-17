from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determines the starting gas station index to complete a circular route.
        Uses a Greedy approach by tracking the total gas deficit/surplus and 
        resetting the starting position whenever the current tank drops below zero.
        """
        # If the total gas available is strictly less than the total cost, 
        # it is mathematically impossible to complete the circuit from ANY station.
        if sum(gas) < sum(cost):
            return -1
            
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            # If our tank drops below zero, it means we cannot reach station i + 1 
            # from our current start_index (or from any station in between).
            if current_gas < 0:
                # The earliest possible start must be the next station
                start_index = i + 1
                # Reset our current tank for this new potential start
                current_gas = 0
                
        return start_index