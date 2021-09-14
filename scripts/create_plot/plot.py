# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

xs = np.arange(len(df))
xlabels = ["1\n(Beginner)", "2", "3", "4", "5\n(Expert)"]
before = df.before.to_numpy()
after = df.after.to_numpy()
before_percent = 100*(before / before.sum())
after_percent = 100*(after / after.sum())
width=0.35
hsf_red = "#C02F2C"
im = plt.imread("hsf_logo_angled.png")

# +
fig, ax = plt.subplots()
bar_before = ax.bar(xs-width/2, before_percent, width=width, label="Before training", color="k")
bar_after = ax.bar(xs+width/2, after_percent, width=width, label="After training", color=hsf_red)
for n, rect in zip(before, bar_before):
    height = rect.get_height()
    if n > 0:
        plt.text(
            rect.get_x() + rect.get_width() / 2.0,
            1+height,
            f'{n:.0f}', ha='center', va='bottom', color="k"
        )
for n, rect in zip(after, bar_after):
    height = rect.get_height()
    if n > 0:
        ax.text(
            rect.get_x() + rect.get_width() / 2.0, 1+height,
            f'{n:.0f}',
            ha='center', va='bottom', color=hsf_red
        )
plt.legend()
ax.set_xticks(xs)
ax.set_xticklabels(xlabels)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.legend(frameon=False)
ax.set_ylabel("Percent of participants")
ax.set_title("How do you rate your knowledge and abilities when using Docker?\n")

newax = fig.add_axes([0.65, 0.55, 0.18, 0.18], anchor='NE')
newax.imshow(im)
newax.axis('off')

fig.savefig("dockerfeedback_new.pdf")
fig.savefig("dockerfeedback_new.png", dpi=200)
# -
