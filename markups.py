from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

menum = KeyboardButton('MAIN MENU')

b1 = KeyboardButton('Get Lab Manuals')
b2 = KeyboardButton('Help')
b3 = KeyboardButton('About')

# Main Menu Keyboard
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b1).add(b2).add(b3)

# Sem keys
s1= KeyboardButton('Sem 1')
s2= KeyboardButton('Sem 2')
s3= KeyboardButton('Sem 3')
s4= KeyboardButton('Sem 4')
s5= KeyboardButton('Sem 5')
s6= KeyboardButton('Sem 6')

#Sem boards
keyboard2= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(s1).add(s2).add(s3).add(s4).add(s5).add(s6).add(menum)

# subjects
cf=KeyboardButton('Computer Fundamentals')

clab=KeyboardButton('Programming in C Lab')

oop=KeyboardButton('Object Oriented Programming Lab')
dcp=KeyboardButton('DCP Lab')
dbms=KeyboardButton('DBMS Lab')
sql=KeyboardButton('Database and SQL Lab')

csh=KeyboardButton('Computer System Hardware Lab')
ds=KeyboardButton('Data Structure Lab')
sa=KeyboardButton('System Administration Lab')

cne=KeyboardButton('Computer Network Engineering Lab')
mp=KeyboardButton('Microprocessor Lab')
wp=KeyboardButton('Web Programming Lab')
np=KeyboardButton('Network Programming Lab')

sdp=KeyboardButton('Smart Device Programming Lab')



sem1=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cf).add(menum)

sem2=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(clab).add(menum)

sem3=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(oop).add(dcp).add(dbms).add(sql).add(menum)

sem4=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(csh).add(ds).add(sa).add(menum)

sem5=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cne).add(mp).add(wp).add(np).add(menum)


sem6=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(sdp).add(menum)


