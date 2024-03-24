import random

def reservoir_sample_streaming(data_iterable, k):
    """
    从数据流中使用Reservoir Sampling算法随机抽取k个数。
    :param data_iterable: 一个可迭代的数据流（例如文件对象的__iter__方法）
    :param k: 要抽取的样本数量
    :return: 一个包含k个样本的列表
    """
    samples = []
    for i, item in enumerate(data_iterable):
        # 如果样本列表还为空或者小于要抽取的样本数量k
        if len(samples) < k:
            samples.append(item)
        else:
            # 计算随机数，如果小于当前索引i，则替换样本列表中的一个元素
            # 包含0和i
            a = random.randint(0, i)
            if a < k:
                samples[a] = item
            # if random.randint(0, i) < k:
            #     # 随机选择一个索引来替换样本列表中的元素
            #     samples[random.randint(0, k - 1)] = item

    return samples

# # 示例使用
# # 假设我们有一个大型数据文件，每行包含一个数字
# file_path = 'large_dataset.txt'
# k = 1000  # 要抽取的样本数量
#
# # 打开文件并逐行读取，抽取样本
# with open(file_path, 'r') as file:
#     samples = reservoir_sample_streaming(file.__iter__(), k)
#     print("Sampled Data Points:", samples)

# a=[100,20,2,4,6,8,9,2,5,7,9,5,3,1,6,8,212,45]
a=[3,2,2,4,6,6,9,2,5,7,9,5,3,1,6,8,212,45]
k=5
samples = reservoir_sample_streaming(a, k)
print(samples)