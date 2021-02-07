# Thompson Sampling
"""
1. It is better than Upper Confidence Bound
2. It can compute accurate results even using less rounds(user records).
3. We are using only 1000 record and it will give accurate results which is not possible in UCB
"""

import matplotlib.pyplot as plt
import pandas as pd
import random

# Importing Dataset
dataset = pd.read_csv('../Datasets/ads_ctr_optimisation.csv')

# Implementing UCB
no_of_users_records = 1000
no_of_ads_in_one_round = 10
ads_selected = []
no_of_rewards_0 = [0] * 10  # R
no_of_rewards_1 = [0] * 10
total_reward = 0
dataset = dataset.values
for n in range(0, no_of_users_records):
    selected_ad = 0
    max_random = 0
    for i in range(0, no_of_ads_in_one_round):
        random_beta = random.betavariate(no_of_rewards_0[i] + 1, no_of_rewards_1[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            selected_ad = i
    ads_selected.append(selected_ad)
    reward = dataset[n, selected_ad]
    if reward == 1:
         no_of_rewards_1[selected_ad] += 1
    else:
        no_of_rewards_0[selected_ad] += 1
    total_reward += reward

# visualizing the UCB
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
