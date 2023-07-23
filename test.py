import random
import chart

def main():
	datas = []
	for i in range(999):
		datas.append(random.randint(0,8999))
		pass

	_chart = chart.chart()
	_chart.DrawLine(datas)
	_chart.show()


if __name__ == "__main__":
	main()
