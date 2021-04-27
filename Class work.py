import matplotlib.pyplot as plt
fig,ax=plt.subplots()

x=[1,2,3,4,5]
y=[2,4,6,8,10]
y2=[1,2,3,4,5]
ax.plot(x,y, marker="v", color="gold", linestyle="dashdot")
ax.plot(x,y2)

plt.show()

