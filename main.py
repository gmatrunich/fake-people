import file_operations
from faker import Faker
import random

SKILLS = [
  "Стремительный прыжок",
  "Электрический выстрел",
  "Ледяной удар",
  "Стремительный удар",
  "Кислотный взгляд",
  "Тайный побег",
  "Ледяной выстрел",
  "Огненный заряд"
]

ABC = {
  'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
  'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
  'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
  'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
  'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
  'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
  'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
  'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
  'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
  'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
  'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
  'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
  'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
  'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
  'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
  'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
  'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
  'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
  'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
  'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
  'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
  'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
  ' ': ' '
}

NUMBER_OF_FAKE_PERSONS = 10
MIN_RANDOM = 8
MAX_RANDOM = 14

FAKE = Faker("ru_RU")


for person in range(NUMBER_OF_FAKE_PERSONS):

    fake_name = FAKE.name()
    names_list = fake_name.split()
    name = names_list[1]
    last_name = names_list[0]

    three_random_skills = random.sample(SKILLS, 3)
    runic_skills = []

    for skill in three_random_skills:
        runic_skill = []
        for letter in skill:
            runic_skill.append(ABC[letter])
        runic_skills.append(''.join(runic_skill))

    context = {
      "first_name": name,
      "last_name": last_name,
      "job": FAKE.job(),
      "town": FAKE.city(),
      "strength": random.randint(MIN_RANDOM, MAX_RANDOM),
      "agility": random.randint(MIN_RANDOM, MAX_RANDOM),
      "endurance": random.randint(MIN_RANDOM, MAX_RANDOM),
      "intelligence": random.randint(MIN_RANDOM, MAX_RANDOM),
      "luck": random.randint(MIN_RANDOM, MAX_RANDOM),
      "skill_1": ''.join(runic_skills[0]),
      "skill_2": ''.join(runic_skills[1]),
      "skill_3": ''.join(runic_skills[2])
      }

    file_operations.render_template("charsheet.svg", "RESULTS/charsheet-{}.svg".format(person), context)
