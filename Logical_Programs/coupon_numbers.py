import random
class CouponNumber:
    """
    Coupon Numbers
    a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
    need to generate distinct coupon number? This program simulates this random
    process.
    b. I/P -> N Distinct Coupon Number
    c. Logic -> repeatedly choose a random number and check whether it's a new one.
    d. O/P -> total random number needed to have all distinct numbers.
    e. Functions => Write Class Static Functions to generate random number and to
    process distinct coupons.

    """
    @staticmethod
    def generate_random_number(n):
        return random.randint(0,n-1)
    
    @staticmethod
    def collect_coupons(n):
        collected = set()
        count = 0

        while len(collected) < n:
            coupon = CouponNumber.generate_random_number(n)
            count += 1
            collected.add(coupon)

        return count

n = int(input("Enter Distinct Coupon Number"))

total_distinct_coupons = CouponNumber.collect_coupons(n)
print(f"Total Random Numbers : {total_distinct_coupons}")

