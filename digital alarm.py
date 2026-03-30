# digital alarm and raminder system

import time
import datetime
# list to store reminders
reminders=[]
# display current date and time
def show_time():
   now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   print('current date and time:',now)
#function to validate time format
def validate_time(input_time):
     try:
         datetime.datetime.strptime(input_time, '%H:%M') 
         return True
     except ValueError:
       return False 
# function to add reminder
def add_reminder ():
   reminder=input("enter the reminder:").strip()
   if reminder=="":
      print('reminder cannot be empty')
      return
   reminder_time=input('enter the reminder time').strip()
   if not validate_time(reminder_time):
      print('invalid format, enter in HH:MM format')
      return
   reminders.append({'time':reminder_time,'message':reminder})
   print('reminder added successfully')
# function to check alarm
def check_alarm():
   print('alarm system started')
   while True: 
      now=datetime.datetime.now().strftime('%H:%M')
      for reminder in reminders:
         if reminder['time']==now:
            print('Reminder Alert!')
            print('Message:',reminder['message'])
            print('Time:',reminder['time'])
            reminders.remove(reminder)
      time.sleep(60) 
# main function
def checking():
   while True:
        print("Digital Alarm & Reminder System ")
        print("1. Show Current Time")
        print("2. Add Reminder")
        print("3. Start Alarm Checking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_time()
        elif choice == "2":
            add_reminder()
        elif choice == "3":
            if len(reminders) == 0:
                print("No reminders set")
            else:
                check_alarm()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print(" Invalid choice! Please try again.")

checking()



        

          


  


