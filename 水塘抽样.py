# random取1
# random取k
# 带权重的水塘抽样

import numpy as np
import random


def watershed_sampling(population, sample_size, seed=None):
    if seed is not None:
        np.random.seed(seed)

    # 确保样本大小不超过总体大小
    sample_size = min(sample_size, len(population))

    # 从总体中随机选择初始样本
    sample = np.random.choice(population, sample_size, replace=False)

    for i in range(sample_size, len(population), sample_size):
        # 从总体中随机选择一个未被选中的元素加入样本
        new_member = np.random.choice(list(set(population) - set(sample)))
        sample = np.append(sample, new_member)

        # 从样本中随机移除一个元素
        removed_member = np.random.choice(sample)
        sample = np.delete(sample, np.where(sample == removed_member))

    return sample


# 示例使用
population = list(range(100))  # 假设总体是从0到99的整数
sample_size = 10  # 我们需要的样本大小
seed = 42  # 随机种子，用于结果可复现

sample = watershed_sampling(population, sample_size, seed)
print("Watershed Sample:", sample)