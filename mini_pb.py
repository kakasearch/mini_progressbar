import time
def progressbar(total,desc = "Progress:"):
	maxval = min([50,total])#控制最大值小于数字
	maxval = max([20,maxval])#最小值大于给的数字
	for i in range(total):
		percent = i/total
		yield i
		print('%s|'%desc + ('#' * int(percent*maxval)).ljust(maxval) + '| [{:0>4.1f}%] {}/{}'.format(percent*100,i+1,total),end="\r")
	print('%s|'%desc + ('#' * int(maxval)).ljust(maxval) + '| [100%] '+ "%s/%s  "%(total,total))

if  __name__ == "__main__":
	for i in progressbar(100,desc="进度："):
		#your code
		time.sleep(0.1)