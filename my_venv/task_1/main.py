from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB (змініть URI, якщо потрібно)
from pymongo import MongoClient

client = MongoClient("mongodb+srv://szafiroweecho:EndbH6zqajlJqJcM@marsianka.rffwu2u.mongodb.net/",  tls=True,
    tlsAllowInvalidCertificates=True)


db = client["cats_db"]
cats_collection = db["cats"]


print("Успішне підключення!")

# Створення (Create)
def add_cat(name, age, features):
    """Додає нового кота в базу даних."""
    cat = {"name": name, "age": age, "features": features}
    result = cats_collection.insert_one(cat)
    print(f"Додано кота з id: {result.inserted_id}")

# Читання (Read)
def get_all_cats():
    """Виводить всі записи з колекції."""
    for cat in cats_collection.find():
        print(cat)

def get_cat_by_name(name):
    """Знаходить та виводить інформацію про кота за ім'ям."""
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кота з таким ім'ям не знайдено.")

# Оновлення (Update)
def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям."""
    result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count:
        print("Вік оновлено.")
    else:
        print("Кота не знайдено.")

def add_feature_to_cat(name, feature):
    """Додає нову характеристику до списку features кота."""
    result = cats_collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.modified_count:
        print("Характеристику додано.")
    else:
        print("Кота не знайдено.")

# Видалення (Delete)
def delete_cat_by_name(name):
    """Видаляє кота з колекції за ім'ям."""
    result = cats_collection.delete_one({"name": name})
    if result.deleted_count:
        print("Кота видалено.")
    else:
        print("Кота не знайдено.")

def delete_all_cats():
    """Видаляє всі записи з колекції."""
    cats_collection.delete_many({})
    print("Всі коти видалені з бази даних.")

cats = [
(["Барсик", 3, "ходить в капці", "дає себе гладити", "рудий"]),
("Мурчик", 5, ["любить муркотіти", "спить на підвіконні", "сірий смугастий"]),
("Сніжок", 2, ["білий пухнастий", "обожнює сидіти на руках", "ганяється за лазером"]),
("Гарфілд", 4, ["ледачий", "любить їсти", "не терпить собак"]),
("Луна", 1, ["чорна", "грається з нитками", "ховається в коробках"]),
("Саймон", 6, ["дуже розумний", "відкриває двері лапами", "сірий"]),
("Буба", 8, ["товстий", "любить спати на клавіатурі", "хропе"]),
("Рижик", 3, ["дуже активний", "стрибає по шторах", "рудий"]),
("Василько", 7, ["спокійний", "обожнює сметану", "гладкошерстий"]),
("Пушок", 2.5, ["дуже пухнастий", "любить гратися з дітьми", "біло-сірий"]),
("Тиша", 9, ["тихий", "ніколи не дряпається", "обожнює сидіти біля вікна"])
]
    
    
# Приклад використання
if __name__ == "__main__":


   for cat in cats:
       add_cat(cat)  # Розпаковуємо кортеж у аргументи функції

    #get_all_cats()
    #get_cat_by_name("Barsik")
    #update_cat_age("Barsik", 4)
    #add_feature_to_cat("Barsik", "любить гратися")
    #delete_cat_by_name("Barsik")
    #delete_all_cats()
