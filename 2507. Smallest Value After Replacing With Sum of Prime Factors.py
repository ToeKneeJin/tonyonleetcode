class Solution:
    def get_total_prime_factor(self, n):
        new = 0
        i = 2
        while i <= n:
            while n % i == 0:
                n = n / i
                new += i
            i += 1
        return new
        
    def smallestValue(self, n: int) -> int:
        smallest = n
        while smallest > self.get_total_prime_factor(smallest):
            smallest = self.get_total_prime_factor(smallest)
        return smallest
