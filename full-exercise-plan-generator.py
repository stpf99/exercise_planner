import json
import random
from datetime import datetime, timedelta

class ExerciseDatabase:
    def __init__(self):
        # Ćwiczenia dla różnych partii ciała i poziomów trudności
        self.exercises = {
            # Ćwiczenia rozgrzewkowe i rozciągające
            'warm_up_and_stretch': {
                'light': [
                    "Rozciąganie całego ciała 5 minut",
                    "Delikatne krążenia ramion 2 minuty",
                    "Skręty tułowia w miejscu 5 razy",
                    "Pochylenia głowy na boki 5 razy",
                    "Głębokie oddychanie 3 minuty",
                    "Marsz w miejscu 3 minuty",
                    "Wymachy ramion w przód i tył 10 razy"
                ],
                'moderate': [
                    "Dynamiczne rozciąganie całego ciała 7 minut",
                    "Krążenia ramion i nadgarstków 3 minuty",
                    "Skręty tułowia z lekkim wyprostowaniem 10 razy",
                    "Przysiad w miejscu bez obciążenia 10 razy",
                    "Podskoki na jednej nodze 5 razy",
                    "Bieg w miejscu 5 minut"
                ],
                'advanced': [
                    "Pełny stretching z elementami jogi 10 minut",
                    "Dynamiczne rozgrzanie stawów 5 minut",
                    "Kompleksowe rozciąganie mięśni 8 minut"
                ]
            },
            
            # Ćwiczenia na górną połowę ciała
            'upper_body': {
                'light': [
                    "Pompki przy ścianie 5 razy",
                    "Unoszenie rąk w górę 10 razy",
                    "Krążenia ramion 2 minuty",
                    "Delikatne ruchy ramion w przód i tył 10 razy"
                ],
                'moderate': [
                    "Pompki na kolanach 8 razy",
                    "Podciąganie się pod framugą drzwi 5 razy",
                    "Wypychanie ramion w przód 12 razy",
                    "Krążenia ramion z delikatnym obciążeniem 3 minuty"
                ],
                'advanced': [
                    "Pompki klasyczne 10 razy",
                    "Przysiady z unoszeniem ramion 8 razy",
                    "Dynamiczne pompki 6 razy"
                ]
            },
            
            # Ćwiczenia na dolną połowę ciała
            'lower_body': {
                'light': [
                    "Wstań i usiądź na krześle 10 razy",
                    "Marsz w miejscu 5 minut",
                    "Delikatne przysiady 5 razy",
                    "Unoszenie nóg w pozycji siedzącej 10 razy"
                ],
                'moderate': [
                    "Przysiady bez obciążenia 12 razy",
                    "Wypady w przód 8 razy na każdą nogę",
                    "Podskoki w miejscu 10 razy",
                    "Wchodzenie na palce i powrót 15 razy"
                ],
                'advanced': [
                    "Przysiady głębokie 15 razy",
                    "Podskoki na jednej nodze 10 razy",
                    "Wypady dynamiczne 12 razy"
                ]
            },
            
            # Ćwiczenia na brzuch i core
            'core': {
                'light': [
                    "Leżenie tyłem, unoszenie głowy 5 razy",
                    "Skręty tułowia w pozycji siedzącej 8 razy",
                    "Delikatne unoszenie nóg w pozycji leżącej 5 razy"
                ],
                'moderate': [
                    "Deska na przedramionach 20 sekund",
                    "Unoszenie nóg w pozycji leżącej 10 razy",
                    "Skręty tułowia z lekkim uniesieniem 12 razy",
                    "Rowerek w powietrzu 15 sekund"
                ],
                'advanced': [
                    "Pełna deska 30 sekund",
                    "Unoszenie przeciwległej ręki i nogi 10 razy",
                    "Skręty dynamiczne z uniesieniem 15 razy"
                ]
            },
            
            # Ćwiczenia na równowagę
            'balance': {
                'light': [
                    "Stanie na jednej nodze 10 sekund",
                    "Marsz po prostej linii 2 minuty",
                    "Delikatne kołysanie w przód i tył 5 razy"
                ],
                'moderate': [
                    "Stanie na jednej nodze z zamkniętymi oczami 15 sekund",
                    "Chodzenie na palcach 1 minutę",
                    "Przejście po wyimaginowanej linii 3 minuty"
                ],
                'advanced': [
                    "Stanie na jednej nodze z wykonywaniem skrętów 20 sekund",
                    "Dynamiczne zmiany pozycji równoważnych 10 razy"
                ]
            },
            
            # Ćwiczenia relaksacyjne
            'relaxation': {
                'light': [
                    "Głębokie oddychanie 5 minut",
                    "Medytacja siedząca 3 minuty",
                    "Rozluźnienie mięśni 2 minuty"
                ],
                'moderate': [
                    "Medytacja z koncentracją na oddechu 5 minut",
                    "Progresywne rozluźnianie mięśni 7 minut",
                    "Wizualizacja spokoju 4 minuty"
                ],
                'advanced': [
                    "Pełna medytacja uważności 10 minut",
                    "Zaawansowane techniki oddechowe 6 minut"
                ]
            }
        }

    def get_exercises_by_category_and_level(self, category, level):
        """
        Zwraca listę ćwiczeń dla danej kategorii i poziomu trudności
        
        :param category: Kategoria ćwiczeń (np. 'warm_up_and_stretch')
        :param level: Poziom trudności ('light', 'moderate', 'advanced')
        :return: Lista ćwiczeń
        """
        return self.exercises.get(category, {}).get(level, [])

    def get_all_categories(self):
        """
        Zwraca listę wszystkich kategorii ćwiczeń
        
        :return: Lista kategorii
        """
        return list(self.exercises.keys())

    def get_random_exercise(self, category=None, level=None):
        """
        Zwraca losowe ćwiczenie
        
        :param category: Opcjonalna kategoria
        :param level: Opcjonalny poziom trudności
        :return: Losowe ćwiczenie
        """
        if category and level:
            return random.choice(self.get_exercises_by_category_and_level(category, level))
        
        if category:
            levels = list(self.exercises.get(category, {}).keys())
            level = random.choice(levels)
            return random.choice(self.get_exercises_by_category_and_level(category, level))
        
        if level:
            categories = [cat for cat in self.exercises.keys() 
                          if level in self.exercises[cat]]
            category = random.choice(categories)
            return random.choice(self.get_exercises_by_category_and_level(category, level))
        
        # Całkowicie losowe ćwiczenie
        category = random.choice(list(self.exercises.keys()))
        level = random.choice(list(self.exercises[category].keys()))
        return random.choice(self.get_exercises_by_category_and_level(category, level))


class ExercisePlanGenerator:
    def __init__(self):
        # Inicjalizacja bazy ćwiczeń
        self.exercise_db = ExerciseDatabase()

        # Godziny do wyboru dla ćwiczeń
        self.hours = [
            '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', 
            '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', 
            '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', 
            '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', 
            '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00'
        ]

    def calculate_bmi(self, weight, height):
        """Oblicza BMI"""
        return weight / ((height/100) ** 2)

    def determine_exercise_level(self, bmi, age, gender):
        """Określa poziom trudności ćwiczeń"""
        if bmi < 18.5:
            return 'light'
        elif 18.5 <= bmi < 25:
            return 'moderate'
        elif 25 <= bmi < 30:
            return 'challenging'
        elif bmi >= 30:
            if age > 50 or gender == 'female':
                return 'light'
            return 'moderate'

    def generate_plan(self, days, weight, height, age, gender):
        """Generuje plan ćwiczeń"""
        bmi = self.calculate_bmi(weight, height)
        exercise_level = self.determine_exercise_level(bmi, age, gender)

        plan = {}
        categories = [
            'warm_up_and_stretch', 
            'upper_body', 
            'lower_body', 
            'core', 
            'balance', 
            'relaxation'
        ]

        for day in range(1, days + 1):
            day_exercises = {}
            used_hours = set()

            # Losowa liczba ćwiczeń (4-7)
            num_exercises = random.randint(4, 7)

            # Upewnij się, że każdy dzień ma rozciąganie na początku i końcu
            day_exercises['06:00'] = "Rozciąganie całego ciała 5 minut"
            used_hours.add('06:00')
            day_exercises['21:00'] = "Rozciąganie całego ciała 5 minut"
            used_hours.add('21:00')

            for _ in range(num_exercises - 2):  # -2 bo już mamy rozciąganie na początku i końcu
                # Wybierz godzinę która nie była jeszcze użyta
                available_hours = [h for h in self.hours if h not in used_hours]
                hour = random.choice(available_hours)
                used_hours.add(hour)

                # Wybierz kategorię i poziom ćwiczeń
                category = random.choice(categories)
                exercise = self.exercise_db.get_random_exercise(
                    category=category, 
                    level=exercise_level
                )
                day_exercises[hour] = exercise

            # Sortuj ćwiczenia wg godzin
            sorted_exercises = dict(sorted(day_exercises.items()))
            plan[str(day)] = sorted_exercises

        return {
            "reference_date": datetime.now().strftime("%Y-%m-%d"),
            "plan": plan
        }

    def save_plan(self, plan, filename):
        """Zapisuje plan do pliku JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)

# Przykładowe użycie
def main():
    generator = ExercisePlanGenerator()
    plan = generator.generate_plan(
        days=30,       # Liczba dni
        weight=150,     # Waga w kg
        height=180,    # Wzrost w cm
        age=43,        # Wiek
        gender='male'  # Płeć
    )

    # Zapisz plan do pliku
    generator.save_plan(plan, 'exercise_plan.json')

    # Wyświetl plan
    print(json.dumps(plan, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
