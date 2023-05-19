from scipy.stats import binom

# 1. Probability of 5 successes in 10 trials
print(binom.rvs(100, 0.35, size =1000))

cien = binom.rsv(100, 0.35, size =100)
#mil = binom.rvs(100, 0.35, size =1000)
#diezmil = binom.rvs(100, 0.35, size =10000)
#cienmil = binom.rvs(100, 0.35, size =100000)