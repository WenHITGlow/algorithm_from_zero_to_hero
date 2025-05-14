import random

def calculate_gini(wealth):
    """Calculate the Gini coefficient of wealth distribution."""
    sum_of_absolute_differences = 0
    sum_of_wealth = sum(wealth)
    n = len(wealth)
    for i in range(n):
        for j in range(n):
            sum_of_absolute_differences += abs(wealth[i] - wealth[j])
    return sum_of_absolute_differences / (2 * n * sum_of_wealth)

def experiment(n, t):
    """Run the wealth distribution experiment."""
    wealth = [100.0] * n  # Everyone starts with 100 units of money
    
    for _ in range(t):
        has_money = [w > 0 for w in wealth]
        
        for j in range(n):
            if has_money[j]:
                # Give 1 unit to random person other than self
                while True:
                    other = random.randint(0, n-1)
                    if other != j:
                        break
                wealth[j] -= 1
                wealth[other] += 1
    
    # Sort wealth for display
    wealth.sort()
    print("列出每个人的财富(贫穷到富有) : ")
    for i in range(n):
        print(f"{int(wealth[i])} ", end="")
        if i % 10 == 9:
            print()
    print()
    print(f"这个社会的基尼系数为 : {calculate_gini(wealth)}")

def main():
    print("一个社会的基尼系数是一个在0~1之间的小数")
    print("基尼系数为0代表所有人的财富完全一样")
    print("基尼系数为1代表有1个人掌握了全社会的财富")
    print("基尼系数越小，代表社会财富分布越均衡；越大则代表财富分布越不均衡")
    print("在2022年，世界各国的平均基尼系数为0.44")
    print("目前普遍认为，当基尼系数到达 0.5 时")
    print("就意味着社会贫富差距非常大，分布非常不均匀")
    print("社会可能会因此陷入危机，比如大量的犯罪或者经历社会动荡")
    print("测试开始")
    
    n = 100  # number of people
    t = 100000  # number of rounds
    print(f"人数 : {n}")
    print(f"轮数 : {t}")
    experiment(n, t)
    print("测试结束")

if __name__ == "__main__":
    main() 