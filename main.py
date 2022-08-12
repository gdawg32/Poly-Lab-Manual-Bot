
# Import modules


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import markups as nav

# API declarartion 
bot = Bot(token='INSERT BOT TOKE HERE')
dp = Dispatcher(bot)


#Links
cflink = "https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=1008"
clink="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=2139"

oop="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=3137"
dcp="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=3138"
sql="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=3159"
dbms="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=3139"

csh="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=4137"
ds="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=4138"
sa="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=4139"

cne="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=5137"
mp="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=5138"
np="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=5159"
wp="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=5139"
sdp="https://www.sitttrkerala.ac.in/index.php?r=site%2Fdiploma-lab-manual-courses-show&course=6138"



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hi!\nI'm Poly LabManual Bot! I provide you with lab manuals for CT and CHE students of Kerala Polytechnic Colleges\n", reply_markup=nav.keyboard1)
    
    

@dp.message_handler()
async def mmenu(message: types.Message):
    if message.text == "Get Lab Manuals":
       await message.reply("Choose your Semester", reply_markup=nav.keyboard2)

    if message.text == "Help":    
       await message.reply("Click on /start or /help to return to the main menu. Contact @Welmo_W for any assistances")
        
    if message.text == "About":
       await message.reply("This bot was made as a college project. Feedbacks can be sent to @Welmo_W")

    if message.text == "MAIN MENU":
       await message.reply("Main Menu",reply_markup=nav.keyboard1)
 
    # Sem 1
    if message.text == 'Sem 1':
       await bot.send_message(message.chat.id, "Choose Subject", reply_markup=nav.sem1)
            

    if message.text == 'Computer Fundamentals':
        await message.reply_document(document=cflink, caption="CF")

    if message.text == 'Main Menu':
        await bot.send_message(message.from_user.id, "MAIN MENU", reply_markup=nav.keyboard1)    

# Sem 2
    
    if message.text == 'Sem 2':
            await bot.send_message(message.from_user.id, "Choose Subject", reply_markup=nav.sem2)

    if message.text == 'Programming in C Lab':
             await message.reply_document(document=clink, caption="Programming in C Lab")


# Sem 3
    
    if message.text == 'Sem 3':
            await bot.send_message(message.from_user.id, "Choose Subject", reply_markup=nav.sem3)

    if message.text == 'Object Oriented Programming Lab':
             await message.reply_document(document=oop, caption="Object Oriented Programming Lab")

    elif message.text == 'DCP Lab':
             await message.reply_document(document=dcp, caption="DCP Lab")

    elif message.text == 'DBMS Lab':
             await message.reply_document(document=dbms, caption="DBMS Lab for CT")

    elif message.text == 'Database and SQL Lab':
             await message.reply_document(document=sql, caption="Database and SQL Lab for CHE")

 # Sem 4                   

    
    if message.text == 'Sem 4':
            await bot.send_message(message.from_user.id, "Choose Subject", reply_markup=nav.sem4)

    if message.text == 'Computer System Hardware Lab':
             await message.reply_document(document=csh, caption="CSH Lab")

    elif message.text == 'Data Structure Lab':
             await message.reply_document(document=ds, caption="DS Lab")

    elif message.text == 'System Administration Lab':
             await message.reply_document(document=sa, caption="SA Lab")         

 # Sem 5
 
 
    
    if message.text == 'Sem 5':
            await bot.send_message(message.from_user.id, "Choose Subject", reply_markup=nav.sem5)

    if message.text == 'Computer Network Engineering Lab':
             await message.reply_document(document=cne, caption="CNE Lab")

    elif message.text == 'Microprocessor Lab':
             await message.reply_document(document=mp, caption="MP Lab")           

    elif message.text == 'Web Programming Lab':
             await message.reply_document(document=wp, caption="WP Lab")

    elif message.text == 'Network Programming Lab':
             await message.reply_document(document=np, caption="NP Lab")

 # Sem 6
    
    if message.text == 'Sem 6':
            await bot.send_message(message.from_user.id, "Choose Subject", reply_markup=nav.sem6)

    if message.text == 'Smart Device Programming Lab':
             await message.reply_document(document=sdp, caption="SDP Lab")               


    
    if message.text!= 'Sem 1' or 'Sem 2' or 'Sem 3' or 'Sem 4' or 'Sem 5' or 'Sem 6' :
        pass
    else:
        await bot.send_message(message.from_user.id, "If you have chosen a wrong option, click /start") 







#echo bot

#@dp.message_handler()
#async def echo(message: types.Message):
#    await message.answer(message.text)
   
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

