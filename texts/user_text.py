GENDER_TEXT = """
    🕴️ <b>Jinsingizni tanlang:</b>\n
    👔 <b>Erkaklar uchun kolleksiya</b>
    👠 <b>Ayollar uchun kolleksiya</b>
    🧒 <b>Bolalar uchun kiyimlar</b>\n
    <b>Tanlang va davom eting 👇</b>
    """ 
    




CATEGORY_TEXT = """
😊 Ajoyib!
Siz jinsni tanladingiz ✅

Endi iltimos, quyidagi toifalardan birini tanlang:
👇 Sizga mos bo'lgan kategoriyani tanlang."""


SEASON_TEXT = """
🌟 *Ajoyib tanlov!* 🌟  
👕 Endi mavsumni belgilang!  

🧥 Har bir kiyim o‘z fasliga mos —  
shuning uchun, siz qaysi fasl uchun kiyim izlayotganingizni tanlang:  

🌸 *Bahor* — Yengil va qulay kiyimlar  
☀️ *Yoz* — Eng issiq kunlar uchun style  
🍂 *Kuz* — Sovuq shamollar uchun moda kiyimlar  
❄️ *Qish* — Iliq va zamonaviy liboslar  

👇 Quyidagi tugmalardan keraklisini tanlang.
"""



def select_filter(gender,category,season):
    return f"""
🛍️ Sizning tanlovingiz tayyor ✅

👤 Jinsi: {gender}
🧩 Kategoriya: {category}
🌤️ Mavsum: {season}

Ajoyib tamlov! 🎉
Endi siz uchun aynan shu yo'nalishda eng mos kiyimlarni topamiz 👕🩳👜

Iltimos, bir necha soniya keting - tavsiya etilgan mahsulotlar yuklanmoqda 🔎"""


def product_text(name,brand,category_name,gender,size,season,price):
    return f"""
    <b>{name}</b>\n
    🏷 Brand: <i>{brand}</i>\n
    📂 Kategoriya: <i>{category_name}</i>\n
    🧍 Gender: <i>{gender}</i>\n
    📏 O'lcham: <i>{size}</i>\n
    🍂 Fasl: <i>{season}</i>\n
    💰 Narx: <b>{price}</b> so'm\n
            """