import random


def weighted_sampling_k_elements(population, weights, k, seed=None):
    if seed is not None:
        random.seed(seed)

    # 检查权重是否在0到1之间
    if not all(0 <= w <= 1 for w in weights):
        raise ValueError("Weights must be in the range [0, 1].")

    # 检查权重数组和总体数组长度是否一致
    if len(weights) != len(population):
        raise ValueError("The length of the population and weights must be the same.")

    # 计算权重的累积和
    cumulative_weights = []
    current_sum = 0
    for w in weights:
        current_sum += w
        cumulative_weights.append(current_sum)

    # 初始化样本列表
    samples = []

    # 重复K次采样过程
    for _ in range(k):
        # 生成一个[0, sum(weights))范围内的随机数
        random_value = random.uniform(0, sum(weights))

        # 根据随机数找到对应的元素
        for i, cum_weight in enumerate(cumulative_weights):
            if random_value <= cum_weight:
                samples.append(population[i])
                break  # 找到元素后跳出循环

    return samples


# 示例使用
population = ['apple', 'banana', 'cherry', 'date', 'fig']
weights = [0.2, 0.3, 0.5, 0.05, 0.6]  # 权重总和不为1
k = 3  # 要采样的元素数量
seed = 42  # 随机种子，用于结果可复现

samples = weighted_sampling_k_elements(population, weights, k, seed)
print("Weighted Samples (K=3):", samples)