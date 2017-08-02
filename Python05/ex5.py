# -- coding: utf-8 --
my_name='Zed A. Shaw'
my_age= 35
my_height= 74
my_weight = 180
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight)

# 附加题1
name='Zed A. Shaw'
age= 35
height= 74
cm = height * 2.54
weight = 180
kg = 0.4535924 * weight
eyes='Blue'
teeth='White'
hair='Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % cm
print "He's %d pounds heavy." % kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d,%d,and %d I get %d." %(age,height,weight,age + height + weight)
