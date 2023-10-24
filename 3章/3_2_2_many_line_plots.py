import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14

# データ生成
np.random.seed(0)  # 同じ乱数が生成されるようにシードを設定
n_days = 30
n_individuals = 30
half_n = int(n_individuals / 2)

# 期待値を生成
expected_values_group1 = np.random.normal(loc=50, scale=5, size=half_n)
expected_values_group2 = np.random.normal(loc=70, scale=5, size=half_n)
expected_values = np.concatenate([expected_values_group1, expected_values_group2])

# 各個体の30日間の活動量を生成
activity_data = [np.random.normal(loc=ev, scale=10, size=n_days) for ev in expected_values]

# グラフ描画
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# 全個体をそれぞれ違う色で描画
# colors = plt.cm.viridis(np.linspace(0, 1, n_individuals))  # 色のリストを生成
colors = plt.cm.jet(np.linspace(0, 1, n_individuals))  # 色のリストを生成

for i in range(n_individuals):
    axs[0, 0].plot(range(n_days), activity_data[i], color=colors[i], alpha=0.8)

# 一番活動量の期待値が大きい個体をゴールド、それ以外は灰色で描画
max_ev_individual = np.argmax(expected_values)  # 最大期待値の個体のインデックス
for i in range(n_individuals):
    if i == max_ev_individual:
        pass
    color = 'gray'
    axs[0, 1].plot(range(n_days), activity_data[i], color=color, alpha=0.5)

color = 'gold'
axs[0, 1].plot(range(n_days), activity_data[max_ev_individual], color=color, lw=2)


# 15個体のグループごとに、ゴールド、青で描画
for i in range(half_n):
    axs[1, 0].plot(range(n_days), activity_data[i], color='gold', alpha=0.5)
for i in range(half_n, n_individuals):
    axs[1, 0].plot(range(n_days), activity_data[i], color='blue', alpha=0.5)

# 各グループの各日の平均値と標準偏差を計算し、平均値を折れ線グラフで、標準偏差をその周りの影付きの領域で描画
for i, color in zip([0, half_n], ['gold', 'blue']):
    group_activity_data = activity_data[i:i + half_n]
    group_mean = np.mean(group_activity_data, axis=0)
    group_std = np.std(group_activity_data, axis=0)
    axs[1, 1].plot(range(n_days), group_mean, color=color)
    axs[1, 1].fill_between(range(n_days), group_mean - group_std, group_mean + group_std, color=color, alpha=0.3)

# グラフの調整
for ax in axs.ravel():
    ax.set_ylim(15, 105)
    # ax.set_ylabel('Activity level')

axs[0, 0].set_ylabel("活動量スコア")
axs[1, 0].set_ylabel("活動量スコア")
axs[1, 0].set_xlabel("経過日数")
axs[1, 1].set_xlabel("経過日数")
# axs[0, 0].set_title('All individuals')
# axs[0, 1].set_title('Max expectation individual in gold')
# axs[1, 0].set_title('Grouped by initial expectation')
# axs[1, 1].set_title('Mean and standard deviation for each group')

plt.tight_layout()
# more space between subplots
plt.subplots_adjust(hspace=0.3, wspace=0.2)
plt.savefig('3_2_2_many_line_plots.png', dpi=300)
plt.savefig('3_2_2_many_line_plots.svg', dpi=300)

plt.show()
