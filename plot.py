import matplotlib
matplotlib.use('cairo')
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
import pandas
import pdb



# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(5, 5))

data =pandas.read_csv("data.csv")
# Load the example car crash dataset

# Plot the total crashes
#sns.set_color_codes("pastel")
#pal = sns.color_palette([(0.9,0.1,0.1),(0.1,0.1,0.9)])
#sns.set_palette(pal)
data["Value"]*=100


sns.barplot(x="Value", y="Concept", data=data, hue=data["Hue"])

# Add a legend and informative axis label
plt.title("Beliefs of Presidential Twitter Followers")
ax.legend(ncol=1, loc="upper center", bbox_to_anchor=(0.8, 0.85), frameon=True)
ax.set(xlim=(-200, 200), ylabel="",
       xlabel="Relative Rate of Following Proxy Accounts")
#sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.savefig("plot.png")
