import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# logo configuration
MONITOR_DPI = 96
PIXEL_SIZE = 500
BACKGROUND_COLOR = None  # black, white, or None


data = pd.read_csv("rose_diagram_data.csv")

cr = (
    data["annual_rate_of_mortality_per_1000_zymotic_diseases"][:12]
    + data["annual_rate_of_mortality_per_1000_wounds_and_injuries"][:12]
    + data["annual_rate_of_mortality_per_1000_all_other_causes"][:12]
)

number_of_months = 12
bottom = 2
start = -np.pi / 4 - np.pi / 6
stop = start + 2 * np.pi
theta = np.linspace(start, stop, number_of_months, endpoint=False)
width = (2 * np.pi) / number_of_months

fig = plt.figure(figsize=(PIXEL_SIZE/MONITOR_DPI, PIXEL_SIZE/MONITOR_DPI), dpi=MONITOR_DPI)

if BACKGROUND_COLOR is not None:
    fig.patch.set_facecolor(BACKGROUND_COLOR)

ax = fig.add_subplot(111, polar=True)
bars = ax.bar(
    theta,
    cr,
    width=width,
    bottom=bottom,
    color="#6a103c",
    edgecolor="#FFFFFF",
    linewidth=5,
)
ax.set_theta_zero_location("N")  # north
ax.set_theta_direction(-1)  # increasing clockwise

plt.axis("off")
plt.tight_layout()
plt.gca().set_position([-0.1, 0, 1.4, 1.55])  # ensures the diagram is centered and not the origin

# plt.savefig("logo.svg", transparent=True, dpi=MONITOR_DPI)
plt.savefig("logo.png", transparent=True, dpi=MONITOR_DPI)
# plt.show()
