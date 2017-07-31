# -*- coding: utf-8 -*-
#现在有100辆车
cars = 100
#每辆车可以容纳4.0个人
space_in_a_car = 4.0
#有30个司机
drivers = 30
#有90个乘客
passengers = 90
#不开的车=总车辆-司机人数
cars_not_driven = cars - drivers
#开的车=司机人数
cars_driven = drivers
#总载客数=开的车*每辆车可容纳的人数
carpool_capacity = cars_driven * space_in_a_car
#平均一辆车载多少乘客=乘客数量/开的车的数量
average_passengers_per_car = passengers / cars_driven
#显示 这里有100辆可用的车？
print "There are", cars,"cars available."
#显示 这里仅有30个司机
print "There are only", drivers,"drivers available."
#显示 这里将有70辆空车
print "There will be",cars_not_driven,"empty cars today."
#显示 我们可以运输120.0个乘客
print "We can transport", carpool_capacity,"people today."
#显示 我们有90个乘客需要载
print "We have",passengers,"to carpool today."
#显示 每辆车放3个乘客
print "We need to put about",average_passengers_per_car,"in each car."

# 附加题
#错误信息：错误地将carpool_capacity写成car_pool_capacity,这个之前没有定义过
