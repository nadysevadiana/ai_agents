"""
ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ - CareerCoach Crew

Этот файл содержит готовые примеры для разных сценариев
"""

from career_coach_crew import CareerCoachCrew
import json


# ==============================================================================
# ПРИМЕР 1: Полная оценка карьеры для Junior разработчика
# ==============================================================================

def example_junior_developer_assessment():
    """
    Сценарий: Молодой разработчик (2 года опыта) хочет перейти на middle позицию
    """
    print("\n" + "="*80)
    print("ПРИМЕР 1: Полная оценка карьеры для Junior разработчика")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4", temperature=0.7)
    
    user_profile = {
        'name': 'Максим Иванов',
        'current_position': 'Junior Python Developer',
        'experience_years': 2,
        'skills': ['Python', 'Django', 'HTML/CSS', 'JavaScript', 'Git'],
        'education': 'Бакалавр Computer Science, МГУ (2022)',
        'specialization': 'Backend Development',
        'goals': 'Стать Middle Backend Developer за 1.5 года и вести небольшой проект',
        'preferences': {
            'remote': True,
            'salary_expectation': '80000-120000',
            'location': 'Moscow/Remote',
            'company_type': 'Startup или Growth-stage',
            'learning_willing': True
        },
        'resume': '''
МАКСИМ ИВАНОВ
Email: maksim@example.com | Phone: +7-900-123-4567 | GitHub: github.com/maksim

ОПЫТ
Junior Python Developer at StartupXYZ (2022-2024)
- Разработка REST API на Django
- Работа с PostgreSQL
- Участие в code reviews
- Решение багов и оптимизация кода

Freelance Projects (2021-2022)
- Создание веб-приложений на Django

ОБРАЗОВАНИЕ
Бакалавр Computer Science, МГУ (2022)

НАВЫКИ
Python, Django, PostgreSQL, REST API, HTML/CSS, JavaScript, Git, Docker (basics)

ПРОЕКТЫ
- E-commerce Platform: Django, PostgreSQL, REST API
- Blog System: Django with comments and authentication
        '''
    }
    
    try:
        crew = coach.run_full_career_assessment(user_profile)
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nСимуляция результата:\n")
        print("""
ПОЛНАЯ ОЦЕНКА КАРЬЕРЫ
=====================

ТЕКУЩЕЕ СОСТОЯНИЕ
- Позиция: Junior Python Developer (2 года)
- Основные навыки: Python, Django, PostgreSQL
- Рынок: В спросе, растущий спрос

АНАЛИЗ РЫНКА
- Спрос на Middle Backend Developers: ЛЫ очень высокий
- Средняя зарплата Middle: 120-180k руб
- Требуемые навыки: Python (advanced), FastAPI/Django, Microservices, Docker/K8s

ПРОБЕЛЫ В НАВЫКАХ
1. Advanced Python (metaclasses, decorators, asyncio) - КРИТИЧНО
2. Асинхронное программирование (asyncio, aiohttp)
3. Микросервисная архитектура
4. Docker и Kubernetes basics
5. Системное дизайн и архитектурные паттерны

ПЛАН ОБУЧЕНИЯ (1.5 года)
Месяцы 1-3: Advanced Python
- Metaclasses, decorators, context managers
- Асинхронное программирование (asyncio)
- Курс: "Advanced Python" на Coursera
- Время: 15-20 часов/неделю

Месяцы 4-6: FastAPI и асинхронность
- FastAPI framework
- Async/await patterns
- Курс + практический проект
- Время: 15 часов/неделю

Месяцы 7-9: Микросервисы и Docker
- Микросервисная архитектура
- Docker, Docker Compose
- Курсы на Udemy
- Практика с реальными проектами

Месяцы 10-18: Системное дизайн и лидерство
- Системное дизайн интервью
- Лидерство и менторство
- Опыт работы с более крупными системами

РЕКОМЕНДАЦИИ ПО ПОИСКУ РАБОТЫ
1. Целевые компании: Яндекс, МТС, VK, Авито
2. Уровень: Junior-Middle переход
3. Фокус: Компании, готовые развивать junior'ов

СТРАТЕГИЯ ЛИЧНОГО БРЕНДА
1. GitHub Portfolio - создать 2-3 значимых проекта
2. LinkedIn - регулярный контент о обучении
3. Medium/Habr - написание статей о изученных темах
4. Открытые контрибьюции в open-source проекты

МЕТРИКИ УСПЕХА
- Получить Middle позицию за 1.5 года ✓
- Зарплата 120k+ ✓
- Вести проект с 1-2 junior разработчиками ✓
        """)


# ==============================================================================
# ПРИМЕР 2: Оптимизация резюме для конкретной вакансии
# ==============================================================================

def example_resume_optimization():
    """
    Сценарий: Оптимизация резюме для вакансии Senior QA Engineer
    """
    print("\n" + "="*80)
    print("ПРИМЕР 2: Оптимизация резюме для вакансии")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    current_resume = """
АННА ПЕТРОВА
Email: anna.petrova@example.com
Phone: +7-900-222-3333
GitHub: github.com/anna-qa

WORK EXPERIENCE

QA Engineer at TechCorp LLC (2019-2024)
- Тестирование веб и мобильных приложений
- Написание test cases
- Баг репортинг

Senior QA Engineer at StartupABC (2024-present)
- Управление QA процессом
- Тестирование

EDUCATION
Техникум в области IT (2017)

SKILLS
Python, Selenium, SQL, Jira, Postman, Git, TestNG (Java basics)

LANGUAGES
Russian (native), English (intermediate)
    """
    
    job_posting = """
Senior QA Engineer / Test Lead

Requirements:
- 5+ years in QA (mandatory)
- Proficiency in Python and Java
- Selenium, TestNG, Pytest
- Rest API testing (Postman, RestAssured)
- CI/CD knowledge (Jenkins, GitLab)
- SQL and database testing
- Test automation frameworks design
- Team leading experience is a plus
- Agile/Scrum methodology

Responsibilities:
- Design test automation strategy
- Lead QA team of 2-3 engineers
- Mentor junior QA engineers
- Improve testing processes
- API and UI test automation
    """
    
    try:
        crew = coach.run_resume_optimization(current_resume, job_posting)
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nСимуляция результата:\n")
        print("""
АНАЛИЗ ТЕКУЩЕГО РЕЗЮМЕ
======================
✓ Наличие опыта в QA
✓ Базовые технологии упомянуты
✗ Недостаточно деталей о достижениях
✗ Нет метрик (кол-во багов, покрытие и т.д.)
✗ Слабое описание обязанностей
✗ Нет упоминания о лидерстве и менторстве
✗ Java не упоминается

АНАЛИЗ ТРЕБОВАНИЙ ВАКАНСИИ
============================
- 5+ лет опыта: у вас есть ✓
- Python: есть, но не акцентировано ⚠
- Java: НЕТ - КРИТИЧНО ✗
- Selenium: есть, но базово ⚠
- TestNG: НЕТ ✗
- REST API: есть (Postman) ✓
- CI/CD: НЕ УПОМИНАЕТСЯ ✗
- SQL: упоминается, но слабо ⚠
- Leadership: есть, но не подчеркнуто ⚠

ОПТИМИЗИРОВАННОЕ РЕЗЮМЕ
=========================

АННА ПЕТРОВА
Senior QA Engineer | Test Automation Lead | Python & Java
Email: anna.petrova@example.com | +7-900-222-3333
LinkedIn: linkedin.com/in/anna-petrova | GitHub: github.com/anna-qa

PROFESSIONAL SUMMARY
Experienced Senior QA Engineer with 5+ years in test automation and team leadership.
Expert in designing test automation frameworks and implementing comprehensive testing
strategies. Proven track record of reducing testing time by 40% through automation.
Strong Python/Java skills with REST API and UI testing expertise.

PROFESSIONAL EXPERIENCE

Senior QA Engineer | StartupABC (2024-Present)
- Leading QA team of 2 junior engineers, mentoring and performance reviews
- Designed and implemented test automation framework using Python + Selenium
- Reduced regression testing time by 40% through comprehensive automation
- REST API testing using Postman and Python (requests library)
- CI/CD integration with GitLab CI/Jenkins for automated test execution
- Improved code quality through code reviews and QA process optimization

QA Engineer | TechCorp LLC (2019-2024)
- Developed automated tests in Python using Selenium WebDriver and Pytest
- Implemented SQL-based test data validation and database testing
- Performed manual and automated testing for web and mobile applications
- 200+ test cases written and maintained, average bug discovery rate 25%
- Collaborated with development team in Agile/Scrum environment

TECHNICAL SKILLS
Languages: Python (Advanced), Java (Intermediate)
Testing Frameworks: Selenium WebDriver, Pytest, TestNG (basics)
API Testing: Postman, Python requests library, REST Assured
Databases: SQL (MySQL, PostgreSQL), database testing expertise
CI/CD: GitLab CI, Jenkins, automated test pipeline configuration
Tools: Jira, Git, Docker, AWS basics
Methodologies: Agile/Scrum, TDD, BDD

CERTIFICATIONS & EDUCATION
Professional Certifications
- ISTQB Certified Test Automation Engineer (expected Q2 2025)
- Google QA Professional Certificate (2023)

Education
- Техникум IT, специализация "Testing" (2017)

LANGUAGES
Russian (Native), English (Intermediate - professional level)

ACHIEVEMENTS
✓ Designed test automation strategy reducing regression time by 40%
✓ Successfully mentored 2 junior QA engineers to mid-level positions
✓ Implemented 500+ automated tests with 95% pass rate stability
✓ Reduced bug escape rate from 15% to 5% through improved testing process
        """)


# ==============================================================================
# ПРИМЕР 3: Подготовка к интервью
# ==============================================================================

def example_interview_preparation():
    """
    Сценарий: Подготовка к интервью на позицию Senior Backend Developer
    """
    print("\n" + "="*80)
    print("ПРИМЕР 3: Подготовка к интервью")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    job_description = """
Senior Backend Developer / Architect

Requirements:
- 5+ years backend development experience
- Python/Go/Java expertise
- Microservices architecture knowledge
- System design skills
- Team leadership experience
- REST API design
- Database optimization (SQL)
    """
    
    company_info = """
TechCorp - FAANG-like компания
- 500+ employees
- Strong engineering culture
- Работают на Python, Go, Kubernetes
- Растущая компания (IPO в 2025)
- Офисы в Москве и San Francisco
    """
    
    try:
        crew = coach.run_interview_preparation(job_description, company_info)
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nСимуляция результата:\n")
        print("""
ПОДГОТОВКА К ИНТЕРВЬЮ
======================

ВЕРОЯТНЫЕ ВОПРОСЫ И STAR-ОТВЕТЫ

1. "Расскажите о вашем самом значительном проекте"
   
   STAR ОТВЕТ:
   Situation: Работал в стартапе, платформа обрабатывала 1M+ событий/день, 
             API начала деградировать при такой нагрузке
   
   Task: Нужно было переработать архитектуру, чтобы обработать 10M событий/день
         с задержкой не более 100ms
   
   Action:
   - Провел анализ bottleneck'ов (обнаружил неэффективные запросы к БД)
   - Спроектировал микросервисную архитектуру на Python с FastAPI
   - Использовал Redis для кэширования часто запрашиваемых данных
   - Внедрил асинхронную обработку через Celery
   - Настроил load testing и continuous monitoring
   
   Result:
   - Увеличили пропускную способность до 15M событий/день
   - Снизили p95 latency с 500ms до 50ms
   - Улучшили стабильность системы на 99.95% uptime
   - Сэкономили 40% инфраструктурных затрат через оптимизацию

2. "Как вы проектируете систему с нуля?"
   
   ОТВЕТ:
   - Понимание требований (функциональные и нефункциональные)
   - Оценка scale и performance requirements
   - Выбор архитектурного паттерна (монолит vs микросервисы)
   - Дизайн основных компонентов
   - Выбор технологий и баз данных
   - Планирование scalability и reliability
   - Определение monitoring и logging стратегии

3. "Как вы бы оптимизировали медленный SQL запрос?"
   
   ОТВЕТ:
   - Анализ EXPLAIN PLAN для понимания execution strategy
   - Проверка индексов на используемых колонках
   - Оптимизация JOIN'ов и подзапросов
   - Рассмотрение денормализации и кэширования
   - Анализ query pattern'ов
   - Использование database profiling tools
   - Тестирование оптимизаций с реальными данными

4. "Опишите конфликт в команде и как вы его решили"
   
   ОТВЕТ:
   - Был конфликт между Backend и Frontend разработчиками относительно API
   - Инициировал встречу с обеими сторонами для понимания требований
   - Предложил API design session с участием обеих команд
   - Документировали согласованные спецификации
   - Установили процесс для избежания подобных конфликтов

ПОВЕДЕНЧЕСКИЕ РЕКОМЕНДАЦИИ
✓ Говорите уверенно, но не самоуверенно
✓ Используйте конкретные примеры с метриками
✓ Показывайте лидерские качества
✓ Демонстрируйте желание учиться
✓ Задавайте умные вопросы интервьюеру

ВОПРОСЫ ДЛЯ ИНТЕРВЬЮЕРА
1. "Каким вызовам сейчас сталкивается ваша backend команда?"
2. "Как устроена техническая культура компании?"
3. "Какие возможности для роста и лидерства?"
4. "Как выглядит процесс разработки? Agile?"
5. "Какой стек технологий используется в команде?"

ИНФОРМАЦИЯ О КОМПАНИИ (TechCorp)
- FAANG-like компания, быстро растет
- Strong engineering culture с фокусом на качество
- Используют Python, Go, Kubernetes
- IPO в планах на 2025
- Офисы в Москве и SF
- Конкурентная зарплата + акции
- Отличный пакет бенефитов

РЕКОМЕНДАЦИИ
✓ Показать知識 о микросервисной архитектуре
✓ Демонстрировать опыт работы с большими масштабами
✓ Подчеркнуть лидерские качества
✓ Рассказать о инициативности и непрерывном обучении
        """)


# ==============================================================================
# ПРИМЕР 4: Поиск работы
# ==============================================================================

def example_job_search():
    """
    Сценарий: Поиск подходящих вакансий для Middle Backend Developer
    """
    print("\n" + "="*80)
    print("ПРИМЕР 4: Поиск подходящих вакансий")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    criteria = {
        'position': 'Middle/Senior Backend Developer',
        'experience_required': '3-5 years',
        'industry': 'IT/Tech/SaaS',
        'location': 'Moscow/Remote',
        'salary_range': (120000, 200000),
        'required_skills': ['Python', 'Django', 'PostgreSQL', 'REST API', 'Docker'],
        'nice_to_have': ['Kubernetes', 'Microservices', 'Go', 'AWS'],
        'company_stage': ['Startup', 'Growth', 'Public'],
        'work_environment': 'Remote preferred',
        'culture_preferences': ['Learning-focused', 'Innovative', 'Good team']
    }
    
    try:
        crew = coach.run_job_search(criteria)
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nСимуляция результата:\n")
        print("""
РЕЗУЛЬТАТЫ ПОИСКА РАБОТЫ
=========================

Найдено 12 подходящих вакансий. Топ-5 рекомендаций:

1. ⭐⭐⭐⭐⭐ Senior Backend Developer at Yandex
   Совпадение: 95%
   Зарплата: 200000-250000 руб + льготы + акции
   Требования: Python, Go, Microservices (отлично совпадает)
   Команда: 40+ backend engineers
   Growth: Огромные возможности
   Минусы: Жесткий отбор, офис в Москве
   
   РЕКОМЕНДАЦИЯ: Подавайте! Идеально совпадает с вашим профилем
   
2. ⭐⭐⭐⭐⭐ Middle Backend Developer at Avito
   Совпадение: 92%
   Зарплата: 150000-180000 руб + бонусы
   Требования: Python, Django (идеально)
   Команда: Стартап внутри большой компании
   Remote: Полностью удаленно!
   Growth: Отличные возможности
   
   РЕКОМЕНДАЦИЯ: Отличная возможность с удаленкой
   
3. ⭐⭐⭐⭐ Middle Backend Developer at Booking.com (Moscow)
   Совпадение: 88%
   Зарплата: 160000-200000 руб + акции
   Требования: Python/Go, PostgreSQL (хорошо совпадает)
   Команда: Международная, 100+ engineers
   Плюсы: Глобальная компания, отличная репутация
   Минусы: Собеседование на английском, офис
   
   РЕКОМЕНДАЦИЯ: Хороший выбор для развития в крупной компании
   
4. ⭐⭐⭐⭐ Backend Developer at Revolut (Remote)
   Совпадение: 85%
   Зарплата: 140000-180000 EUR/year (эквивалент ~14-18M руб)
   Требования: Python/Go, Microservices
   Команда: FinTech, быстро растет
   Remote: Полностью удаленно
   Плюсы: FinTech опыт, высокие масштабы
   Минусы: Высокие требования к алгоритмическим знаниям
   
   РЕКОМЕНДАЦИЯ: Рассмотрите как стрейчевую цель
   
5. ⭐⭐⭐⭐ Senior Python Developer at VK (Mail.ru Group)
   Совпадение: 83%
   Зарплата: 170000-220000 руб + акции
   Требования: Python (expert), Django (хорошо совпадает)
   Команда: Русская IT компания, 500+ engineers
   Growth: Огромная
   Плюсы: Русский интерфейс, известная компания
   Минусы: Российская компания, могут быть санкции
   
   РЕКОМЕНДАЦИЯ: Хороший вариант если вас интересует роста в РФ

АНАЛИЗ РЫНКА
=============

Спрос:
- Очень высокий спрос на Python developers
- Middle level зарплата растет на 15-20% год/год
- 80+ открытых вакансий на hh.ru для вашего профиля

Средние зарплаты по опыту:
- Junior (1-2 лет): 80-120k руб
- Middle (3-5 лет): 140-200k руб ← ВЫ ЗДЕСЬ
- Senior (5+ лет): 200-300k+ руб

Тренды:
- Спрос на Go и Rust растет (но Python остается лидером)
- Микросервисы - стандарт для крупных компаний
- Remote работа остается популярной (60% вакансий)

РЕКОМЕНДАЦИЯ ПО ПРИМЕНЕНИЮ
============================

ПРИОРИТЕТ 1 (Идеальные матчи):
1. Yandex - Senior Backend Dev
2. Avito - Middle Backend Dev (remote!)
3. Booking.com - Middle Backend Dev

ПРИОРИТЕТ 2 (Хорошие варианты):
1. VK/Mail.ru - Senior Python Dev
2. Revolut - Backend Dev (стрейч)

СТРАТЕГИЯ:
1. Обновите резюме для каждой компании (адаптируйте под требования)
2. Начните с Priority 1 компаний
3. Готовьтесь к интервью (system design вопросы важны)
4. Проведите research на каждую компанию перед интервью
5. Нацельтесь на зарплату 160-200k руб в переговорах

СРОК: С такой квалификацией, вы получите оффер за 2-3 недели
        """)


# ==============================================================================
# ПРИМЕР 5: Полный процесс применения на работу
# ==============================================================================

def example_full_job_application():
    """
    Сценарий: Полный процесс применения на вакансию Senior QA Engineer
    """
    print("\n" + "="*80)
    print("ПРИМЕР 5: Полный процесс применения на работу")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    user_profile = {
        'name': 'Сергей Смирнов',
        'current_position': 'Middle QA Engineer',
        'experience_years': 4,
        'skills': ['Python', 'Selenium', 'TestNG', 'Postman', 'SQL', 'Jira'],
        'goals': 'Senior QA Engineer / Test Lead позиция',
        'resume': 'Резюме QA инженера...'
    }
    
    job_posting = """
Senior QA Engineer / Test Lead

We are looking for an experienced Test Lead to join our growing QA team.

Requirements:
- 5+ years of QA experience
- Strong Python and Java skills
- Selenium, TestNG, Pytest expertise
- REST API testing (Postman, RestAssured)
- CI/CD knowledge (Jenkins, GitLab)
- SQL and database testing
- Test automation frameworks design
- Team leading and mentoring experience
- Agile/Scrum methodology knowledge
    """
    
    company_info = """
InnovateLabs - Software development company
- 150+ employees globally
- Focus on quality and engineering excellence
- Modern tech stack: Java, Python, JavaScript
- Strong testing culture
- Growth stage (Series B, ~$30M funding)
- Offices in Moscow and San Francisco
- Company values: Quality, Innovation, Collaboration
    """
    
    try:
        crew = coach.run_full_job_application_workflow(
            user_profile,
            job_posting,
            company_info
        )
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nСимуляция результата:\n")
        print("""
ПОЛНЫЙ ПРОЦЕСС ПРИМЕНЕНИЯ НА РАБОТУ
======================================

ШАГ 1: АНАЛИЗ ВАКАНСИИ
========================

Требуемые навыки:
✓ 5+ лет QA опыта: У вас 4 года - БЛИЗКО
✓ Python: Есть ✓
✓ Java: НЕТ - ПРОБЕЛ
✓ Selenium: Есть ✓
✓ TestNG: Есть ✓
✓ Pytest: Есть ✓
✗ REST API: Имеется (Postman) ✓
✓ CI/CD: Есть ✓
✓ SQL: Есть ✓
✓ Team leading: Развивается
✓ Agile: Есть ✓

Общее совпадение: 88% - ОТЛИЧНЫЙ КАНДИДАТ!

ШАГ 2: ОПТИМИЗАЦИЯ РЕЗЮМЕ
==========================

Текущее резюме (краткое):
Сергей Смирнов - Middle QA Engineer

Оптимизированное резюме:
---

СЕРГЕЙ СМИРНОВ
Senior QA Engineer | Test Automation Specialist | Python & Java
Email: sergey@example.com | +7-900-333-4444
GitHub: github.com/sergey-qa

PROFESSIONAL SUMMARY
Experienced QA Engineer with 4 years specializing in test automation and quality assurance.
Proficient in Python and Java with expertise in Selenium and TestNG frameworks.
Proven track record in designing robust test automation strategies and reducing testing
time by 35%. Strong foundation in REST API testing, database validation, and CI/CD
integration. Seeking Senior QA Engineer position to lead QA initiatives and mentor teams.

PROFESSIONAL EXPERIENCE

QA Engineer | TechCorp LLC (2020-2024)
- Designed and implemented Python-based test automation framework using Selenium
- Developed 300+ automated test cases using Python pytest and Java TestNG
- REST API testing using Postman and Java RestAssured
- Improved test coverage from 40% to 80%, reducing regression time by 35%
- CI/CD pipeline setup with Jenkins for automated test execution
- SQL database testing and validation
- Mentored junior QA engineers on test automation best practices
- Achieved 99% test pass rate stability in production releases

TECHNICAL SKILLS
Languages: Python (Strong), Java (Intermediate)
Testing Frameworks: Selenium WebDriver, Pytest, TestNG
API Testing: Postman, RestAssured, Python requests
Databases: SQL (MySQL, PostgreSQL), Database testing expertise
CI/CD: Jenkins, GitLab CI, automated testing pipelines
Tools: Jira, Git, Docker, Linux
Methodologies: Agile/Scrum, Test-Driven Development

---

ШАГ 3: ИССЛЕДОВАНИЕ КОМПАНИИ
=============================

InnovateLabs Profile:
- 150+ employees, растущая компания (Series B)
- Фокус на качество - отличный fit для QA специалиста
- Современный стек технологий
- Офисы в Москве и San Francisco
- Сильная инженерная культура

Вероятные вопросы компании:
1. Опыт лидерства и менторства
2. Масштабирование test automation
3. Система дизайн для test infrastructure
4. Как вы бы улучшили QA процесс?

ШАГ 4: ПОДГОТОВКА К ИНТЕРВЬЮ
==============================

STAR-ОТВЕТЫ ГОТОВЫ:

Q: "Расскажите о вашем опыте с автоматизацией"
A: [STAR ответ с метриками и результатами]

Q: "Как вы лидировали QA инициативы?"
A: [STAR ответ о менторстве и улучшениях]

Q: "Система дизайн test infrastructure?"
A: [Архитектурный ответ с примерами]

ВОПРОСЫ ДЛЯ ИНТЕРВЬЮЕРА:
- Как выглядит текущий QA процесс?
- Какие challenges стоят перед QA команой?
- Есть ли возможности для лидерства?
- Какой стек используется для automation?

ШАГ 5: СТРАТЕГИЯ ЛИЧНОГО БРЕНДА
==================================

LinkedIn Optimization:
- Обновить headline: "QA Engineer | Test Automation | Python/Java"
- Написать summary о опыте в test automation
- Добавить ключевые достижения (метрики!)

GitHub:
- Загрузить примеры test framework'ов
- Показать качество кода и best practices

ШАГ 6: ФИНАЛЬНАЯ СТРАТЕГИЯ
=============================

РЕКОМЕНДАЦИЯ: ✅ ПОДАВАЙТЕ!
- 88% совпадение с требованиями
- Вы очень близки к нужному уровню опыта
- Java можно выучить на job
- Компания ценит качество - ваш фокус

ПРОЦЕСС:
1. Отправить оптимизированное резюме
2. Ожидание интервью (1-2 дня)
3. Техническое интервью (2-3 часа подготовки)
4. Интервью с лидом (1 час подготовки)
5. HR интервью (обсуждение зарплаты)

ОЖИДАЕМЫЕ РЕЗУЛЬТАТЫ:
- Зарплата: 120-150k USD в год
- Роль: Senior QA Engineer / Test Lead
- Рост: Огромные возможности в растущей компании

СРОКИ:
- Весь процесс: 2-3 недели
- Ожидаемый оффер: В течение месяца
        """)


# ==============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ==============================================================================

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║    ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ - CareerCoach Crew Многоагентная Система        ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
    
    Доступные примеры:
    
    1. example_junior_developer_assessment()
       - Полная оценка карьеры для Junior Developer
       - Выявление пробелов в навыках
       - План развития на 1.5 года
    
    2. example_resume_optimization()
       - Оптимизация резюме для вакансии
       - ATS-оптимизация
       - Адаптация под требования
    
    3. example_interview_preparation()
       - Подготовка к интервью
       - STAR-ответы
       - Поведенческие рекомендации
    
    4. example_job_search()
       - Поиск подходящих вакансий
       - Анализ рынка
       - Рекомендации по приоритету
    
    5. example_full_job_application()
       - Полный процесс применения на работу
       - Все этапы подготовки
       - Финальная стратегия
    
    ИСПОЛЬЗОВАНИЕ:
    
    from examples import example_junior_developer_assessment
    example_junior_developer_assessment()
    
    """)
    
    # Раскомментируйте нужный пример для запуска:
    
    # example_junior_developer_assessment()
    # example_resume_optimization()
    # example_interview_preparation()
    # example_job_search()
    # example_full_job_application()
