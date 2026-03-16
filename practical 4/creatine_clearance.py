#1.define variables:age=__
#weight=__
#gender=male/female
#cr=__μmol/l
#2.ensure variables are reasonable:
#if weight <=0 or >=80, wrong
#if gender is not male or female, wrong
#3. calculate:
#if gender is female:
#  crcl=((140-age)*weight)/(72*cr)*0.85
# else: 
# crcl=(140-age)*weight)/(72*cr)
#4.output:
#if the result is reasonable, print the resule
# else:
#print:the result is wrong
age=18
weight=65
gender="male"
cr=80
reasonable=True
if age>=100:
   reasonable=False
if weight<=20 or weight>=80:
   reasonable=False
if cr<=0 or cr >=100:
   reasonable=False
if reasonable:
    if gender=='male':
       crcl=crcl=((140-age)*weight)/(72*cr)
    else:crcl=((140-age)*weight)/(72*cr)*0.85
    print("crcl:"+str(round(crcl,2))+"ml/min")
else:
    print("ERROR")

