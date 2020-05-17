# import time //if you wish to check how long this program runs, kindly uncommentize line 1, 139, 324, 330, 342, 349, 397
def hcf(x,y):
    if (y!=0):
        return hcf(y, x%y)
    else:
        return x

def getFraction(x):
    isNegative=False
    string_x= str(x)
    if '.' in string_x:
        list_x=[]
        list_x=string_x.split('.')

        signedindicator=float(x)
        if signedindicator<0:
            isNegative=True

        integer=int(list_x[0])
       
        decimalplace=int(float(list_x[1]))
        numberoften=1
        for i in range(len(list_x[1])):
            integer*=10
            numberoften*=10

        if integer>0:
            integer=integer+decimalplace
        elif integer<0:
            integer=integer-decimalplace
        else:
            if isNegative==True:
                integer=integer-decimalplace
            else:
                integer=integer+decimalplace

        nom=int(integer)
        denom=int(numberoften)
        common_divisor=hcf(nom,denom)
        if common_divisor!=-1:
            nom/=common_divisor
            denom/=common_divisor 
    else:
        nom=x
        denom=1

    return int(nom),int(denom)


def xgety(x_input_nominator,x_input_denominator, xlist_nominator,  xlist_denominator, ylist_nominator,  ylist_denominator, c_nominator, c_denominator,n_points):
    # result_nominator=1
    # result_denominator=1
    # result_nominator=result_nominator*ylist_nominator[0]
    # result_denominator=result_denominator*ylist_denominator[0]
    result_double=ylist_nominator[0]/ylist_denominator[0]
    x_input=x_input_nominator/x_input_denominator
    # semi_result_nominator=1
    # semi_result_denominator=1

    for i in range(1,n_points):
        # semi_result_nominator=1
        # semi_result_denominator=1
        semi_result_double=1
        for j in range(i):
            # semi_result_nominator = semi_result_nominator * (x_input_nominator * xlist_denominator[j] - xlist_nominator[j] * x_input_denominator)
            # semi_result_denominator = semi_result_denominator * x_input_denominator * xlist_denominator[j]
            semi_result_double = semi_result_double * (x_input -  (xlist_nominator[j] / xlist_denominator[j]))

        # result_nominator = (result_nominator * c_denominator[i-1] * semi_result_denominator) + (c_nominator[i-1] * semi_result_nominator * result_denominator)
        # result_denominator = result_denominator * c_denominator[i-1] *semi_result_denominator
        result_double=result_double+(semi_result_double*c_nominator[i-1]/c_denominator[i-1])
    # common_divisor=hcf(result_nominator,result_denominator)
    # if common_divisor!=-1:
    #     result_nominator/=common_divisor
    #     result_denominator/=common_divisor
    
    # if result_nominator>0 and result_denominator<0:
    #     result_nominator=0-result_nominator
    #     result_denominator=0-result_denominator
    # elif result_nominator<0 and result_denominator<0:
    #     result_nominator=0-result_nominator
    #     result_denominator=0-result_denominator


    nom,denom=getFraction(result_double)
    if denom==0:
        print("\nDivision by Zero Error")
    elif denom!=1:
        print("\nAnswer: ",nom,"/",denom)
    else:
        print("\nAnswer: ",nom)

    print("Answer_Double: ",result_double,"\n")

   
# Data Points //

# xlistA=["1","2","5","6","9","12","14","15","16","18","19","21","22","23","25","26","27","29"]
# ylistA=["2","4","6","8","11","13","15","10","17","19","25","22","10","31","61","14","19","33"]
# xlistA=['7.2','55/26','20/31','18','44/37','44.1','59.2','91.3','95.1','67.2','74.3','41/88','70.2','99/56','23/52','52','89','21/5','34/41','4/5']
# ylistA=['1.1','3/4','57/35','89','29','82.1','67.1','24.1','0.2','55.3','17.2','59/55','83.1','45/47','69/56','29','75','17/15','7/65','5/3']
# xlistA=[3241.327,2898.271,4479.23037,6599.6586,127176134/168940443,69324089/17295954,652705791/163906639,40043.0,27660.0,921758.709,98302603/285838978,5474.973,73734815/942591443,60757.193,9605.9256,191077214/361754335,68091.732,9119.000000001,17520027/373063436,82496.77]
# ylistA=[49102.600,2499.646,4156.399,283.8457,92015816/130744339,219411144/65991127,869218004/278833051,93059.0,2165.0,3271.27,388354315/803595284,5727.804,615544042/684528757,3570.998,97733.3482,364486804/167117415,9494.897,1658.00000003,57108281/52795128,1237.88]
# xlistA=["481203241.3279759","443542898.2715899","147544479.23037577","843756599.6586645","127176134/168940443","69324089/17295954","652705791/163906639","875640043.0","728427660.0","262921758.70967478","98302603/285838978","658275474.9736588","73734815/942591443","242360757.19323093","693229605.9256951","191077214/361754335","255568091.7324281","930369119.3078916","17520027/373063436","492882496.7704442","143901476.0"]
# ylistA=["573049102.6004064","798082499.646927","876904156.3990815","50500283.84574724","92015816/130744339","219411144/65991127","869218004/278833051","554793059.0","661312165.0","41663271.27070969","388354315/803595284","335265727.80449873","615544042/684528757","330513570.99817264","464097733.34829545","364486804/167117415","103599494.89758292","809791658.7343193","57108281/52795128","310961237.8886008","572469665.0"]
xlistA=[0.983,0.293,-0.678,14.9,456.16,-192.22,102.876,-90.273,12.08,0.162,-86.383,14.765,82.465,354.677,75.2,23.475,54.57,-0.7504,11.11,162.485]
ylistA=[-10.384,0.456,9855.721,-1046.364,4364.86,-0.984,15.7685,0.924,-19.753,8647.99,-901.746,1673.873,-90.172,765.987,142.66773,-0.000173,90.3222,-18.937,-0.4732,-178.8761]
# xlistA=[964639935.5,375766042.9,168156070.9,51939105.86,656779524.5,639724492.4,52209610.52,960138538.1,712691753.4,69,973392384.1,863009670.3,691007501,950776234.3,622095113.9,486550911.1,310059043.6,313580254.8,421808699.8,760984000.9]
# ylistA=[234031906.1,577436990.2,548475438.9,970630817.8,907165157.9,920895353,514094323,402003019.6,649544500.5,420,380040187.6,355705835.3,546574433.3,236446699.4,690760312.9,896103805.6,572086271.3,133432672.5,809171341.7,420482966.2]
# xlistA=[0.0,1.0,2.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.2,12.3,13.0,14.0,15.5,16.0,17.0,18.0]
# ylistA=[4.0,5.0,6.0,6.0,5.0,3.0,1.0,1.0,1.0,3.0,4.0,4.0,3.0,3.0,4.4,4.0,3.0,0.0]

for i in range(len(xlistA)):
    xlistA[i]=str(xlistA[i])
    ylistA[i]=str(ylistA[i])

xlist=[]
ylist=[]
xlist_nominator=[]
xlist_denominator=[]
ylist_nominator=[]
ylist_denominator=[]
c_nominator=[]
c_denominator=[]
stringg=""
tominus_x_nom=1
tominus_x_denom=1

#Manually input points if you wish to //
# n_points=int(input("Enter number of points: "))
# for i in range (n_points):
#     print("Enter Point",i+1,":")
#     points=input("")
#     x , y=points.split()
#     xlistA.append(x)
#     ylistA.append(y)

n_points=len(xlistA)
# start_time=time.time()

#To print points here //
# print("Points")
# for i in range(n_points):
#     print(xlistA[i] , end=" ")
#     print(ylistA[i])

for i in range (n_points):

    for i in xlistA:
        if '/' in i:
            nom,denom= i.split('/')
            xlist_nominator.append(nom)
            xlist_denominator.append(denom)
        else:
             nom,denom= getFraction(i)
             xlist_nominator.append(nom)
             xlist_denominator.append(denom)
    for i in ylistA:
        if '/' in i:
            nom,denom=i.split('/')
            ylist_nominator.append(nom)
            ylist_denominator.append(denom)
        else:
            nom,denom= getFraction(i)
            ylist_nominator.append(nom)
            ylist_denominator.append(denom)

#You can display inputs if you wish to//            
# print("Fraction Form Inputs")
# for i in range(n_points):
#     print(xlist_nominator[i] , end="/")
#     print(xlist_denominator[i], end="\t")
#     print(ylist_nominator[i],end="/")
#     print(ylist_denominator[i])

for i in range(0,len(xlist_nominator)):
    xlist_nominator[i]=int(xlist_nominator[i])
    xlist_denominator[i]=int(xlist_denominator[i])
    ylist_nominator[i]=int(ylist_nominator[i])
    ylist_denominator[i]=int(ylist_denominator[i])


# You can display Polynomial Order 0 if you wish to//
# Polynomial Order 0
stringg=stringg+str(ylist_nominator[0])
# print(ylist_nominator[0], end="")
if ylist_denominator[0] != 1:
    stringg=stringg+'/'+str(ylist_denominator[0])
    # print('/' +str(ylist_denominator[0]),end="")
print()
for i in range (1,n_points):
    divider_nominator=1
    divider_denominator=1
    tominusA_nominator=0
    tominusA_denominator=1
    tominusA_double=0
    divider_double=1

    temp_nominator = int(ylist_nominator[i] * ylist_denominator[0] - ylist_nominator[0] * ylist_denominator[i])
    temp_denominator = int(ylist_denominator[i] * ylist_denominator[0])

    for a in range (i-1):
        for j in range(a+1):
                tominus_x_nom = int(tominus_x_nom * int(int(xlist_nominator[i] * xlist_denominator[j]) - int(xlist_nominator[j] * xlist_denominator[i])))
                tominus_x_denom = int(tominus_x_denom * int(xlist_denominator[i] * xlist_denominator[j]))

                common_divisor=hcf(tominus_x_nom,tominus_x_denom)
                if common_divisor != -1 :
                    tominus_x_nom /= common_divisor
                    tominus_x_denom /= common_divisor

        tominusA_nominator = int(tominusA_nominator * c_denominator[a] * tominus_x_denom) + int(tominusA_denominator * c_nominator[a] * tominus_x_nom)
        tominusA_denominator = int(tominusA_denominator * tominus_x_denom * c_denominator[a])  
                    
        common_divisor=hcf(tominusA_nominator,tominusA_denominator)
        if common_divisor != -1 :
            tominusA_nominator /= common_divisor
            tominusA_denominator/= common_divisor
        
        tominus_x_nom=1
        tominus_x_denom=1
        tominus_x_double=1

    temp_nominator = int(temp_nominator * tominusA_denominator) - int(tominusA_nominator * temp_denominator)
    temp_denominator = int(temp_denominator * tominusA_denominator)

    common_divisor=hcf(temp_nominator,temp_denominator)
    if common_divisor != -1 :
        temp_nominator /= common_divisor
        temp_denominator/= common_divisor

    for j in range (i):
        divider_nominator = int(divider_nominator * (int(xlist_nominator[i] * xlist_denominator[j]) - int(xlist_nominator[j] * xlist_denominator[i])))
        divider_denominator = int(divider_denominator * int(xlist_denominator[i] * xlist_denominator[j]))

        common_divisor=hcf(divider_nominator,divider_denominator)
        if common_divisor != -1 :
            divider_nominator /= common_divisor
            divider_denominator/= common_divisor

    if divider_denominator==0:
        print("Division by Zero Error")
        exit()

    value=int(temp_nominator * divider_denominator)
    c_nominator.append(value)
    value=int(divider_nominator *temp_denominator)
    c_denominator.append(value)
    

    common_divisor = hcf(c_nominator[i - 1], c_denominator[i - 1])
    if common_divisor != -1 :
        c_nominator[i - 1] /= common_divisor
        c_denominator[i - 1] /= common_divisor
    
    smallest_K_nominator = int(temp_nominator*divider_denominator)
    smallest_K_denominator = int(temp_denominator*divider_nominator)

    common_divisor = hcf(smallest_K_nominator, smallest_K_denominator)
    if common_divisor != -1 :
        smallest_K_nominator /= common_divisor
        smallest_K_denominator /= common_divisor

    if smallest_K_nominator < 0 and smallest_K_denominator < 0 or smallest_K_nominator > 0 and smallest_K_denominator < 0:
        smallest_K_nominator = 0 - smallest_K_nominator
        smallest_K_denominator = 0 - smallest_K_denominator
        
    if smallest_K_nominator>=0:
        stringg=stringg+"+"

    stringg=stringg+str(int(smallest_K_nominator))

    if smallest_K_nominator!=0 and smallest_K_denominator!=1:
        stringg=stringg+'/'+str(int(smallest_K_denominator))

    for b in range (i-1,-1,-1):
        denominatorisChange=False
        nominatorisChange=False

        if xlist_nominator[b] < 0 and xlist_denominator[b] < 0:
            xlist_nominator[b] = 0 - xlist_nominator[b]
            xlist_denominator[b] = 0 - xlist_denominator[b]
            stringg= stringg+"(x - "
            
        elif xlist_nominator[b] >= 0 and xlist_denominator[b] < 0:
            xlist_denominator[b] = 0 - xlist_denominator[b]
            denominatorisChange = True
            stringg=stringg+"(x + "

        elif xlist_nominator[b] <= 0 and xlist_denominator[b] > 0:
            xlist_nominator[b] = 0 - xlist_nominator[b]
            nominatorisChange = True
            stringg=stringg+"(x + "
        else:
            stringg=stringg+"(x - "

        if xlist_denominator[b]==1:
            stringg=stringg + str(int(xlist_nominator[b]))
        else:
            common_divisor=hcf(xlist_nominator[b],xlist_denominator[b])
            if common_divisor !=-1:
                x_nominator=xlist_nominator[b]/common_divisor
                x_denominator=xlist_denominator[b]/common_divisor
            
            stringg=stringg+ str(int(x_nominator)) +'/'+str(int(x_denominator))
        
        stringg=stringg+")"

        if nominatorisChange==True:
            xlist_nominator[b]=0-xlist_nominator[b]
        elif denominatorisChange==True:
            xlist_denominator[b]=0-xlist_denominator[b]

    # print("Polynomial Order",i,":")   uncommentize this line and next line to show every single polynomial order //
    # print(stringg)
print("Polynomial Order",n_points-1,":")
print(stringg)

print("Constant Values: ")
for i in range(len(c_nominator)):
    print(i)
    print(c_nominator[i]/c_denominator[i])

# print("Time: ",time.time()-start_time)
option=int(input("To test our polynomial: [1|value] [2|index] : "))

while option ==1 or option ==2:
    if option==1:
        x_value=input("Enter x value: ")
        # start_time=time.time()
        if '/' in x_value:
            nom,denom= x_value.split('/')
            nom,denom=int(nom),int(denom)
        else:
            nom,denom=getFraction(float(x_value))
            nom,denom=int(nom),int(denom)
        print(nom)
        print(denom)
        print("X value: ",nom,"/",denom)
        print("X value in floating point: ",nom/denom)
        xgety(nom,denom, xlist_nominator,  xlist_denominator, ylist_nominator,  ylist_denominator, c_nominator, c_denominator,n_points) 
        # print("Time: ",time.time()-start_time)

        option=int(input("To test our polynomial: [1|value] [2|index] : "))

    elif option==2:
        print("Available index 0-",(n_points-1))
        index_input=input("Enter index (location): ")
        # start_time=time.time()

        if '/' in index_input:
            nom,denom=index_input.split('/')
            nom,denom=int(nom),int(denom)
        else:
            nom,denom=getFraction(float(index_input))
            nom,denom=int(nom),int(denom)

        common_divisor=hcf(nom,denom)
        if common_divisor!=-1:
            nom/=common_divisor
            denom/=common_divisor

        front_index= int(nom/denom)
        back_index=int(front_index+1)

        if front_index==(n_points-1):
            if ylist_denominator[front_index]!=1:
                print("\nAnswer: ",ylist_nominator[front_index],"/",ylist_denominator[front_index],"\n")
            else:
                print("\nAnswer: ",ylist_nominator[front_index])

        elif nom==0:
            xgety(xlist_nominator[front_index],xlist_denominator[front_index], xlist_nominator,  xlist_denominator, ylist_nominator,  ylist_denominator, c_nominator, c_denominator,n_points) 
        elif nom==front_index and denom==1:
            if ylist_denominator[front_index]!=1:
                print("\nAnswer: ",ylist_nominator[front_index],"/",ylist_denominator[front_index],"\n")
            else:
                print("\nAnswer: ",ylist_nominator[front_index])
        else:
            difference_nominator = int(xlist_nominator[back_index] * xlist_denominator[front_index]) - int(xlist_nominator[front_index] * xlist_denominator[back_index])
            difference_denominator = int(xlist_denominator[back_index] * xlist_denominator[front_index])

            while nom >denom:
                nom=nom-denom
            if nom==denom:
                xgety(xlist_nominator[front_index],xlist_denominator[front_index], xlist_nominator,  xlist_denominator, ylist_nominator,  ylist_denominator, c_nominator, c_denominator,n_points) 
            else:
                semi_x_nominator=nom*difference_nominator
                semi_x_denominator=denom*difference_denominator

                x_nominator = semi_x_nominator * xlist_denominator[front_index] + semi_x_denominator * xlist_nominator[front_index]
                x_denominator = semi_x_denominator * xlist_denominator[front_index]
                print("X value: ",x_nominator,"/",x_denominator)
                print("X value in floating point: ",x_nominator/x_denominator)
                xgety(x_nominator, x_denominator, xlist_nominator, xlist_denominator, ylist_nominator, ylist_denominator, c_nominator, c_denominator,  n_points)

        # print("Time: ",time.time()-start_time)
        option=int(input("To test our polynomial: [1|x value] [2|index] : "))
    else:
        print("No such option")
        exit()

