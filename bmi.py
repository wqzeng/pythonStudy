# @author :xpzhuang
# @date : 2020/10/25
height: float = float(input('请输入你的身高：'))
weight = float(input('请输入你的体重：'))
bmi = weight / (height * height)

if bmi < 18.5:
    print('你的BMI指数为：' + str(bmi))
    print('体重过轻')
elif 18.5 <= bmi < 24.9:
    print('你的BMI指数为：' + str(bmi))
    print('正常范围，注意保持')
elif 24.9 <= bmi < 29.9:
    print('你的BMI指数为：' + str(bmi))
    print('你的体重过重')
else:
    print('你太过肥胖')
