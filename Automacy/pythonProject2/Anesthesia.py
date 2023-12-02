from termcolor import colored
import time
from plyer import notification
import pyqrcode
import png

from pyqrcode import QRCode


start=str(input("Turn on the machine on/off?"))
if start == "on" or start=="ON" or start=="on":
    d="ON"
    txt = (colored("""
    "AUTOMACY BOYLE'S CONTROL IS TURING {}"
     """, "yellow"))
    print(txt.format(d))

else:
    d="off"
    txt =(colored(""" "AUTOMACY BOYLE'S CONTROL IS TURING {} "
    ""","red"))
    print(txt.format(d))
    notification.notify(
        title="ALERT!!!",
        message="press on to start ",
        timeout=5
    )
    time.sleep(10)
        

    exit()


a = int(input("How old are you ?"))
b = int(input("what is your weight in kg?"))
h=int(input("enter the height in cm:"))
print(colored("""                                select the surgery
      1.cardiac surgery
      2.Breast cancer surgery
      3.Brain surgery
      4.Neuro surgery
      5.Hand surgery
      6.Cataract surgery
      7.Gynocology surgery
      8.Orthopedic surgery
      9.Endrocrine surgery
      10.Urologic surgery""","green"))
surgery=int(input("select the surgery:"))
if surgery ==1:
    surgery="cardiac surgery"
elif surgery==2:
    surgery="Breast cancer"
elif surgery==3:
    surgery="Brain surgery"
elif surgery==4:
    surgery="Neuro surgery"
elif surgery==5:
    surgery="Hand surgery"
elif surgery==6:
    surgery="Cataract surgery"
elif surgery==7:
    surgery=="Gynocology surgery"
elif surgery==8:
   surgery= "Orthopedic surgery"
elif surgery==9:
    surgery="Endrocrine surgery"
elif surgery==10:
    surgery="Urologic surgery"
else:
    print(colored("""   please select the applicable surgery""","red"))
    print(colored("""                                select the surgery
          1.cardiac surgery
          2.Breast cancer surgery
          3.Brain surgery
          4.Neuro surgery
          5.Hand surgery
          6.Cataract surgery
          7.Gynocology surgery
          8.Orthopedic surgery
          9.Endrocrine surgery
          10.Urologic surgery""", "green"))
    surgery = int(input("select the surgery:"))
    if surgery == 1:
        surgery = "cardiac surgery"
    elif surgery == 2:
        surgery = "Breast cancer"
    elif surgery == 3:
        surgery = "Brain surgery"
    elif surgery == 4:
        surgery = "Neuro surgery"
    elif surgery == 5:
        surgery = "Hand surgery"
    elif surgery == 6:
        surgery = "Cataract surgery"
    elif surgery == 7:
        surgery == "Gynocology surgery"
    elif surgery == 8:
        surgery = "Orthopedic surgery"
    elif surgery == 9:
        surgery = "Endrocrine surgery"
    elif surgery == 10:
        surgery = "Urologic surgery"

#print(surgery)
c = float(input("set the Mac value:"))
print(colored("""
                Getting biomedical paramter value by the help of patient monitoring system""","blue"))
systolic_pressure=int(input("enter the pressure in mmHg:"))
diastolic_pressure=int(input("enter the pressure in mmHg:"))
if (systolic_pressure>=180) and (diastolic_pressure>=120):
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "patient having hypertension crisis",
            timeout = 30
        )
        time.sleep(5)
        print(colored("""
                          Sending bp reports to the doctor""","red"))
        exit()
elif(systolic_pressure>=140) and (diastolic_pressure>=90):
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "patient having hypertension stage-II",
            timeout = 30
        )
        time.sleep(5)
        print(colored("""
                         sending bp reports to the doctor.....""","red"))
        exit()
elif(systolic_pressure>=130) and  (diastolic_pressure>=80):
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "patient having hypertension-I",
            timeout = 30
        )
        time.sleep(5)
        print(colored("""
                         patient having hypertension-I reporting to doctor""","red"))
elif(systolic_pressure<=100) and (diastolic_pressure<=60):
    while(True):
        notification.notify(
            title="emergency",
            message="patient having hypotension",
            timeout=30
        )
        time.sleep(5)
        print(colored("""
        patient having Hypotension reporting to doctor""","red"))
elif(systolic_pressure == 120) and (diastolic_pressure == 80) :
    while(True):
        notification.notify(
           title="NO PROBLEM in BP",
           message="patient is bp normal",
           timeout=30
        )
        time.sleep(5)
        break;
SPO2=int(input("enter the spo2 in(%):"))
if 85 <= SPO2 <= 93:
    while (True):
        notification.notify(
            title="Alert",
            message="Patient having Hypoxia",
            timeout=10
        )
        time.sleep(1)
        print(colored("""
                      patient having hypoxia reporting to doctor""","red"))
        exit()
elif SPO2 < 85:
    while (True):
        notification.notify(
            title="Emergency",
            message="patient having severe Hypoxia",
            timeout=30
        )
        time.sleep(5)
        print("patient having severe Hypoxia reporting to doctor")
        exit()
else:
    while (True):
        notification.notify(
            title="NO PROBLEM",
            message="patient having no problem in blood oxygen level",
            timeout=30
        )
        time.sleep(5)
        break;
hb = int(input("enter the heart beat(BPM):"))
if hb>100:
    while (True):
        notification.notify(
            title="Alert",
            message="Abnormal Heart beat",
            timeout=30
        )
        time.sleep(5)
        print(colored("""
        Reporting to Anesthesiologist about abnormal heart beat""","red"))
        exit()
elif 70<hb and 90>hb:
    while (True):
        notification.notify(
            title="Alert",
            message="Patient heart beat is normal",
            timeout=30
        )
        time.sleep(5)
        break;
else:
    while (True):
        notification.notify(
            title="Emergency",
            message="Patient having very low heart beat",
            timeout=30
        )
        time.sleep(5)
        print(colored("""
                         sharing the abnormal heart beat report to Anesthesiologist""","red"))
        exit()
bt = int(input("enter the body temperature:"))
if bt<32 and bt>38:
    while (True):
        notification.notify(
            title="Alert",
            message="Abnormal body temperature",
            timeout=30
        )
        time.sleep(5)
        print(colored("""
                        Reporting to Anesthesiologist about body temperature""","red"))
        exit()
else:
    while (True):
        notification.notify(
            title="Alert",
            message="Patient body temperature is normal as per range",
            timeout=30
        )
        time.sleep(5)
        print(colored("""
                        All biomedical parameters are as per range the process proceeds""","green"))
        break;

def parameters(age, weight, Mac,systolic_pressure,diastolic_pressure,hb,SPO2,bt):
    #print("age=", age,"weight=", weight,"Mac=", Mac,"SPO2=",SPO2,"Heart_beat=",hb,"Body_Temperature=",bt)
    txt = """
    surgery:{}
    Details:
    patient's age is {} and 
    their weight is {} and 
    you have to set the value of {}
    for {}/{} in mmHg and their heart beat is {} BPM &SPO2 range is {}% in blood
    patient body temperature is {}°C
"""
    printer=(txt.format(surgery,age, weight, Mac,systolic_pressure,diastolic_pressure,hb,SPO2,bt))
    print(printer)

    txt = """
        surgery:{}
        Details:age={},weight={},Mac={},BP= {}/{} in mmHg, hb={},BPM &SPO2 range is {}% in blood,body temperature={}°C
    """
    pri = (txt.format(surgery, age, weight, Mac, systolic_pressure, diastolic_pressure, hb, SPO2, bt))
    s=pri
    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale=8)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale=6)

    while True:
        notification.notify(
            title = "ALERT!!!",
            message =(pri),
            timeout = 10
        )
        time.sleep(5)
        break

parameters(a, b, c,systolic_pressure,diastolic_pressure,hb,SPO2,bt)
def bmi_calculator(weight, height):
    bmi = (weight / (height / 100) ** 2)
    answer = "underweight" if bmi < 18.5 else "normal" if bmi >= 18.5 and bmi <= 24.9 else "overweight" if bmi >= 25 and bmi <= 29.9 \
        else "obese"

    print("your BMI is " + str(int(round(bmi, 0))) + " this is considered " + str(answer) +
          """ so need to give anesthesia for """ + str(answer))


bmi_calculator(b,h)

def anesthesia(d):
   if d !=0:
      print(colored("""
      process starting....""","green"))
   else:
      print(colored("""
      press to start...⭕""","red"))

anesthesia(c)
notification.notify(
    title="ALERT!!!",
    message="starts working ",
    timeout=30
)
time.sleep(5)

def menu():
    choice=int(input("welcome.Thanks for calling us.please select from menu\n1.SPO2\n2.BLOOD-PRESSURE\n3.HEARTBEAT\n4.BODYTEMPERATURE"))
    switcher={
    1:"SPO2",
    2:"BLOOD PRESSURE",
    3:"HEART BEAT",
    4:"BODY TEMPERATURE"
    }
    print("Taking you to "+switcher.get(choice,"please enter a valid choice"))
    if choice == 4:
        print(colored(
            """
            checking the body temperature by using temperature sensor""","green"))
        bt = int(input("enter the body temperature:"))
        if bt < 32 and bt > 38:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Abnormal body temperature",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                Reporting to Anesthesiologist about body temperature""", "red"))
                exit()
        else:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Patient body temperature is normal as per range",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                All biomedical parameters are as per range the process proceeds""", "green"))
                break;
                exit()


    elif choice == 1:
        print(colored("""
        checking Spo2 value by patient monitoring system""","green"))
        SPO2 = int(input("enter the spo2 in(%):"))
        if 85 <= SPO2 <= 93:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Patient having Hypoxia",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                              patient having hypoxia reporting to doctor""", "red"))
                exit()
        elif SPO2 < 85:
            while (True):
                notification.notify(
                    title="Emergency",
                    message="patient having severe Hypoxia",
                    timeout=30
                )
                time.sleep(5)
                print("patient having severe Hypoxia reporting to doctor")
                exit()
        else:
            while (True):
                notification.notify(
                    title="NO PROBLEM",
                    message="patient having no problem in blood oxygen level",
                    timeout=30
                )
                time.sleep(5)
                break;
                exit()
    elif choice==2:
        print(colored("""
                checking the Blood pressure of the patient""", "green"))
        systolic_pressure = int(input("enter the pressure in mmHg:"))
        diastolic_pressure = int(input("enter the pressure in mmHg:"))
        if (systolic_pressure >= 180) and (diastolic_pressure >= 120):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension crisis",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                  Sending bp reports to the doctor""", "red"))
                exit()
        elif (systolic_pressure >= 140) and (diastolic_pressure >= 90):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension stage-II",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                 sending bp reports to the doctor.....""", "red"))
                exit()
        elif (systolic_pressure >= 130) and (diastolic_pressure >= 80):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension-I",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                 patient having hypertension-I reporting to doctor""", "red"))
        elif (systolic_pressure <= 100) and (diastolic_pressure <= 60):
            while (True):
                notification.notify(
                    title="emergency",
                    message="patient having hypotension",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                patient having Hypotension reporting to doctor""", "red"))
        elif (systolic_pressure == 120) and (diastolic_pressure == 80):
            while (True):
                notification.notify(
                    title="NO PROBLEM in BP",
                    message="patient is bp normal",
                    timeout=30
                )
                time.sleep(5)
                break;
                exit()
    else:
        print(colored("""
        checking the heart beat of the patient""","green"))
        hb = int(input("enter the heart beat(BPM):"))
        if hb > 100:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Abnormal Heart beat",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                Reporting to Anesthesiologist about abnormal heart beat""", "red"))
                break


def vitals():
    option = str(input("Do you want to check any other parameter:"))
    if option == "yes" or option == "YES" or option == "Yes":
        choice=int(input("welcome.Thanks for calling us.please select from menu\n1.SPO2\n2.BLOOD-PRESSURE\n3.HEARTBEAT\n4.BODYTEMPERATURE"))
    switcher={
    1:"SPO2",
    2:"BLOOD PRESSURE",
    3:"HEART BEAT",
    4:"BODY TEMPERATURE"
    }
    print("Taking you to "+switcher.get(choice,"please enter a valid choice"))
    if choice == 4:
        print(colored(
            """
            checking the body temperature by using temperature sensor""","green"))
        bt = int(input("enter the body temperature:"))
        if bt < 32 and bt > 38:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Abnormal body temperature",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                Reporting to Anesthesiologist about body temperature""", "red"))
                exit()
        else:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Patient body temperature is normal as per range",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                All biomedical parameters are as per range the process proceeds""", "green"))
                break;
                exit()


    elif choice == 1:
        print(colored("""
        checking Spo2 value by patient monitoring system""","green"))
        SPO2 = int(input("enter the spo2 in(%):"))
        if 85 <= SPO2 <= 93:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Patient having Hypoxia",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                              patient having hypoxia reporting to doctor""", "red"))
                exit()
        elif SPO2 < 85:
            while (True):
                notification.notify(
                    title="Emergency",
                    message="patient having severe Hypoxia",
                    timeout=30
                )
                time.sleep(5)
                print("patient having severe Hypoxia reporting to doctor")
                exit()
        else:
            while (True):
                notification.notify(
                    title="NO PROBLEM",
                    message="patient having no problem in blood oxygen level",
                    timeout=30
                )
                time.sleep(5)
                break;
                exit()
    elif choice==2:
        print(colored("""
                checking the Blood pressure of the patient""", "green"))
        systolic_pressure = int(input("enter the pressure in mmHg:"))
        diastolic_pressure = int(input("enter the pressure in mmHg:"))
        if (systolic_pressure >= 180) and (diastolic_pressure >= 120):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension crisis",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                  Sending bp reports to the doctor""", "red"))
                exit()
        elif (systolic_pressure >= 140) and (diastolic_pressure >= 90):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension stage-II",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                 sending bp reports to the doctor.....""", "red"))
                exit()
        elif (systolic_pressure >= 130) and (diastolic_pressure >= 80):
            while True:
                notification.notify(
                    title="ALERT!!!",
                    message="patient having hypertension-I",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                                 patient having hypertension-I reporting to doctor""", "red"))
        elif (systolic_pressure <= 100) and (diastolic_pressure <= 60):
            while (True):
                notification.notify(
                    title="emergency",
                    message="patient having hypotension",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                patient having Hypotension reporting to doctor""", "red"))
        elif (systolic_pressure == 120) and (diastolic_pressure == 80):
            while (True):
                notification.notify(
                    title="NO PROBLEM in BP",
                    message="patient is bp normal",
                    timeout=30
                )
                time.sleep(5)
                break;
                exit()
    else:
        print(colored("""
        checking the heart beat of the patient""","green"))
        hb = int(input("enter the heart beat(BPM):"))
        if hb > 100:
            while (True):
                notification.notify(
                    title="Alert",
                    message="Abnormal Heart beat",
                    timeout=30
                )
                time.sleep(5)
                print(colored("""
                Reporting to Anesthesiologist about abnormal heart beat""", "red"))

        else:
            print(" ")
    exit()



menu()
vitals()





exit()

