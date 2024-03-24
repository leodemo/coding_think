import random

def weighted_reservoir_sampling(weights, values, k):
    # 初始化蓄水池
    reservoir = []
    total_weight = 0

    # 首先将前k个元素加入蓄水池
    for i in range(k):
        reservoir.append((values[i], weights[i]))
        total_weight += weights[i]

    # 遍历剩余的数值
    for i in range(k, len(values)):
        # 计算当前元素的权重
        current_weight = weights[i]
        # 累积权重加上当前元素的权重
        new_total_weight = total_weight + current_weight

        # 生成一个[0, 1]的随机数
        random_choice = random.random()

        # 计算随机数是否小于当前元素权重与总权重的比例
        if random_choice <= (current_weight / new_total_weight):
            # 随机选择一个蓄水池中的元素进行替换
            reservoir_index = int(random_choice * (k - 1))
            reservoir[reservoir_index] = (values[i], current_weight)
            total_weight += current_weight - reservoir[reservoir_index][1]

    # 返回蓄水池中的数值
    return [item[0] for item in reservoir]

# 示例使用
weights = [10, 20, 30, 4000, 50]  # 权重数组
values = ['a', 'b', 'c', 'd', 'e']  # 数值数组
k = 3  # 要采样的数量

sampled_values = weighted_reservoir_sampling(weights, values, k)
print(sampled_values)