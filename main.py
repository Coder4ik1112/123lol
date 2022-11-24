import config
import logging
 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
 
# log
logging.basicConfig(level=logging.INFO)
 
# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
 
# prices
PRICE2 = types.LabeledPrice(label="Аккаунт GTA 5", amount=500*100)

# start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "( Все команды бота: )")
        await bot.send_message(message.chat.id, "[ Аккаунт с PRIME, /prime ]")
        await bot.send_message(message.chat.id, "[ Аккаунт GTA-V Online, /gtaV ]")
        await bot.send_message(message.chat.id, "[ Читы для CS:GO, /cheats ]")
        await bot.send_message(message.chat.id, "[ Информация /info ]")
        await bot.send_message(message.chat.id, "( По всем вопросам к @nesneek )")

# info
@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "( Информация о боте и т.д: )")
        await bot.send_message(message.chat.id, "[ Создатель бота, NESNEEK ]")
        await bot.send_message(message.chat.id, "[ Сайт, https://nesneek.fun/ ]")
        await bot.send_message(message.chat.id, "[ Дискорд сервер: ]")
        await bot.send_message(message.chat.id, "[ discord.gg/H4V9spqttK ]")
        await bot.send_message(message.chat.id, "[ Скоро будет Ressel читов))) ]")
        await bot.send_message(message.chat.id, "( По всем вопросам к @nesneek )")

# cheats cs
@dp.message_handler(commands=['cheats'])
async def cheats(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "( Все читы которые можно купить )")
        await bot.send_message(message.chat.id, "[ Nesneek.fun, /Cnes ]")
        await bot.send_message(message.chat.id, "( По всем вопросам к @nesneek )")

# ОПЛАТЫ НЕС НЕЕК ТУТ ВСЁ ПОНЯТНО!!!
# gta
@dp.message_handler(commands=['gtaV'])
async def gtaV(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "Вы выбрали [АККАУНТ С GTA V Online]")
 
    await bot.send_invoice(message.chat.id,
                           title="Аккаунт GTA V Online",
                           description="Покупка аккаунта GTA V Online",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://i.ytimg.com/vi/5BnbY3WjNL4/maxresdefault.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE2],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")
 
# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
 
 
# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT (GTA):")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
 
    await bot.send_message(message.chat.id,
                           f"Вы успешно оплатили на сумму, {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пожалуста обратитесь к админстратору, @nesneek [Вам выдатут аккаунт]")
 
# prices
PRICE = types.LabeledPrice(label="Прайм аккаунт", amount=800*100)
 
#prime
@dp.message_handler(commands=['prime'])
async def prime(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "Вы выбрали [АККАУНТ С PRIME - CS:GO]")
 
    await bot.send_invoice(message.chat.id,
                           title="Аккаунт PRIME CS:GO",
                           description="Покупка аккаунта с PRIME",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://i0.wp.com/www.thexboxhub.com/wp-content/uploads/2021/02/csgo.jpeg?fit=665%2C373&ssl=1",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")
 
# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
 
 
# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT (PRIME)")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
 
    await bot.send_message(message.chat.id,
                           f"Вы успешно оплатили на сумму, {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пожалуста обратитесь к админстратору, @nesneek [Вам выдатут аккаунт]")

PRICE4 = types.LabeledPrice(label="Nesneek.fun чит", amount=150*100)

# cheat
@dp.message_handler(commands=['Cnes'])
async def Cnes(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':'):
        await bot.send_message(message.chat.id, "Вы выбрали [NESNEEK.FUN Чит для CS:GO]")
 
    await bot.send_invoice(message.chat.id,
                           title="NESNEEK.FUN Чит для CS:GO",
                           description="Покупка чита NESNEEK.FUN",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://cdn.discordapp.com/attachments/1038421062947459173/1042526994736369684/Screenshot_2.png",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE4],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")
 
# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
 
 
# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT (CHEAT):")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
 
    await bot.send_message(message.chat.id,
                           f"Вы успешно оплатили на сумму, {message.successful_payment.total_amount // 100} {message.successful_payment.currency} пожалуста обратитесь к админстратору, @nesneek [Вам выдатут подписку]")

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)