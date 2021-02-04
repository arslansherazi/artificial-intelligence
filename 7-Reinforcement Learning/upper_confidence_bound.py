# Upper Confidence Bound (UCB)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing Dataset
dataset = pd.read_csv('../Datasets/ads_ctr_optimisation.csv')

# Implementing UCB
no_of_users_records = 10000
no_of_ads_in_one_round = 10
ads_selected = []
num_of_selections = [0] * 10  # N
sum_of_rewards = [0] * 10  # R
dataset = dataset.values
for n in range(0, no_of_users_records):
    selected_ad = "no ad selected"
    max_upper_bound = 0
    for i in range(0, no_of_ads_in_one_round):
        if dataset[n, i] > 0:
            if num_of_selections[i] > 0:
                average_reward = sum_of_rewards[i] / num_of_selections[i]  # ri(n) = Ni(n) / Ri(n)
                delta_i = math.sqrt(3 / 2 * math.log(n + 1)) / num_of_selections[i]  # delta_i(n)
                upper_bound = average_reward + delta_i
            else:
                upper_bound = 1e400
            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                selected_ad = i
        else:
            continue
    if selected_ad != 'no ad selected':
        ads_selected.append(selected_ad)
        sum_of_rewards[selected_ad] += 1
        num_of_selections[selected_ad] += 1

# visualizing the UCB
plt.hist(ads_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
