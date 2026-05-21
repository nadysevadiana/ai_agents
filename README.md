# 📚 Руководство по CareerCoach Crew - Многоагентная Система Развития Карьеры

## Содержание

1. [Обзор системы](#обзор-системы)
2. [Архитектура агентов](#архитектура-агентов)
3. [Установка и настройка](#установка-и-настройка)
4. [Использование](#использование)
5. [Примеры](#примеры)
6. [API Документация](#api-документация)

---

## Обзор системы

CareerCoach Crew - это комплексная многоагентная система на базе Crew AI, которая помогает профессионалам в развитии карьеры. Система состоит из 8 специализированных агентов, каждый из которых отвечает за определенный аспект карьерного развития.

### Ключевые характеристики

✅ **8 специализированных агентов** - каждый с уникальной ролью и компетенциями
✅ **Многопроцессные рабочие потоки** - последовательные и иерархические процессы
✅ **Полная интеграция** - агенты работают вместе для достижения целей
✅ **Гибкость** - можно запускать отдельные сценарии или полный цикл
✅ **Масштабируемость** - легко добавлять новых агентов и задачи

---

## Архитектура агентов

### 1. 👔 Главный Коуч (Chief Career Coach)
**Роль:** Координатор и стратегический консультант
**Ответственность:**
- Разработка персонального плана развития
- Координация работы других агентов
- Мониторинг прогресса
- Итоговые рекомендации

**Процесс взаимодействия:**
```
Chief Coach
├── Запрашивает данные у пользователя
├── Координирует других агентов
├── Анализирует их результаты
└── Создает финальный план
```

### 2. 📄 Эксперт по Резюме (Resume Expert)
**Роль:** Специалист по оптимизации резюме
**Ответственность:**
- Анализ текущего резюме
- Оптимизация для ATS-систем
- Адаптация под требования работодателя
- Создание вариантов резюме

**Ключевые задачи:**
- `resume_analysis` - анализ резюме
- `resume_optimization` - оптимизация под вакансию
- `resume_generation` - создание нового резюме

### 3. 🔍 Охотник за Вакансиями (Job Hunter)
**Роль:** Специалист по поиску вакансий
**Ответственность:**
- Поиск подходящих вакансий
- Анализ требований
- Ранжирование по приоритету
- Исследование компаний

**Ключевые задачи:**
- `job_search` - поиск вакансий
- `job_requirements_analysis` - анализ требований
- `company_research` - исследование компании

### 4. ✅ Верификатор (Verification Specialist)
**Роль:** Контроль качества
**Ответственность:**
- Проверка грамматики и орфографии
- Валидация согласованности
- QA всех материалов
- Верификация фактов

**Ключевые задачи:**
- `content_verification` - проверка контента
- `consistency_check` - проверка согласованности

### 5. 🎯 Коуч по Навыкам (Skills Development Coach)
**Роль:** Советник по развитию компетенций
**Ответственность:**
- Выявление пробелов в навыках
- Рекомендации по обучению
- Подбор сертификаций
- Планирование развития

**Ключевые задачи:**
- `skills_gap_analysis` - анализ пробелов
- `learning_plan` - план обучения

### 6. 🗣️ Интервьюер-Ментор (Interview Mentor)
**Роль:** Подготовка к собеседованиям
**Ответственность:**
- Разработка стратегий ответов
- STAR-структурированные ответы
- Практика интервьюирования
- Поведенческая подготовка

**Ключевые задачи:**
- `interview_prep` - подготовка к интервью
- `interview_practice` - практикование

### 7. 📊 Аналитик Рынка (Market Analyst)
**Роль:** Анализ тенденций рынка
**Ответственность:**
- Анализ тенденций рынка труда
- Исследование зарплат
- Анализ требуемых навыков
- Прогнозирование развития

**Ключевые задачи:**
- `market_analysis` - анализ рынка
- `salary_research` - исследование зарплат

### 8. 🌟 Стратег Персонального Бренда (Personal Branding Strategist)
**Роль:** Развитие личного бренда
**Ответственность:**
- Стратегия персонального бренда
- Оптимизация LinkedIn
- Создание портфолио
- Развитие онлайн-присутствия

**Ключевые задачи:**
- `personal_brand_strategy` - стратегия бренда
- `linkedin_optimization` - оптимизация LinkedIn
- `portfolio_strategy` - стратегия портфолио

---

## Установка и настройка

### Требования

- Python 3.10+
- OpenAI API ключ (или другой LLM провайдер)
- 2+ ГБ RAM

### Установка

```bash
# Клонировать репозиторий
git clone <repo_url>
cd career_coach_crew

# Установить зависимости
pip install -r requirements.txt

# Настроить переменные окружения
cp .env.example .env
# Отредактировать .env и добавить ваш API ключ
```

### Конфигурация

Отредактируйте `.env`:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Альтернативные LLM провайдеры
# CLAUDE_API_KEY=...
# ANTHROPIC_API_KEY=...

# Поиск вакансий
JOB_SEARCH_API_KEY=...

# Логирование
LOG_LEVEL=INFO
```

---

## Использование

### Быстрый старт

```python
from career_coach_crew import CareerCoachCrew

# Инициализация
coach = CareerCoachCrew(model="gpt-4", temperature=0.7)

# Определение профиля пользователя
user_profile = {
    'name': 'Иван Петров',
    'current_position': 'Middle Python Developer',
    'experience_years': 5,
    'skills': ['Python', 'Django', 'PostgreSQL'],
    'goals': 'Стать Senior Developer и вести команду',
    'preferences': {
        'remote': True,
        'location': 'Moscow/Remote'
    }
}

# Запуск полной оценки
crew = coach.run_full_career_assessment(user_profile)
result = crew.kickoff()
print(result)
```

### Основные методы

#### 1. Полная оценка карьеры

```python
crew = coach.run_full_career_assessment(user_profile)
result = crew.kickoff()
```

**Возвращает:**
- Анализ профиля
- План развития
- Рекомендации по навыкам
- Стратегия личного бренда

#### 2. Оптимизация резюме

```python
crew = coach.run_resume_optimization(resume, job_posting)
result = crew.kickoff()
```

**Параметры:**
- `resume` - текущее резюме (строка)
- `job_posting` - описание вакансии (строка)

**Возвращает:**
- Анализ текущего резюме
- Анализ требований вакансии
- Оптимизированное резюме

#### 3. Поиск работы

```python
criteria = {
    'position': 'Senior Developer',
    'industry': 'IT/Tech',
    'location': 'Remote',
    'salary_range': (150000, 250000),
    'required_skills': ['Python', 'Django', 'AWS']
}
crew = coach.run_job_search(criteria)
result = crew.kickoff()
```

**Возвращает:**
- Список подходящих вакансий
- Анализ каждой вакансии
- Рекомендации по приоритету

#### 4. Подготовка к интервью

```python
crew = coach.run_interview_preparation(job_description, company_info)
result = crew.kickoff()
```

**Параметры:**
- `job_description` - описание должности
- `company_info` - информация о компании

**Возвращает:**
- Вероятные вопросы
- STAR-ответы
- Рекомендации по поведению

#### 5. Полный процесс применения

```python
crew = coach.run_full_job_application_workflow(
    user_profile,
    job_posting,
    company_info
)
result = crew.kickoff()
```

---

## Примеры

### Пример 1: Полная карьерная оценка

```python
from career_coach_crew import CareerCoachCrew

coach = CareerCoachCrew(model="gpt-4")

user_profile = {
    'name': 'Анна Сидорова',
    'current_position': 'Junior QA Engineer',
    'experience_years': 2,
    'skills': ['Python', 'Selenium', 'API Testing'],
    'education': 'Бакалавр IT',
    'goals': 'Перейти на Middle QA или Test Lead позицию',
    'preferences': {
        'remote': True,
        'salary_expectation': '80000-120000'
    }
}

# Запуск полной оценки
crew = coach.run_full_career_assessment(user_profile)
result = crew.kickoff()

# Результат включает:
# 1. Анализ текущего состояния
# 2. Требования рынка
# 3. Пробелы в навыках
# 4. План обучения
# 5. Стратегия личного бренда
# 6. Рекомендации по развитию
```

### Пример 2: Оптимизация резюме

```python
resume = """
АННА СИДОРОВА
Email: anna@example.com | Phone: +7-900-111-2222

ОПЫТ
QA Engineer at TechCompany (2022-2024)
- Тестирование веб-приложений
- Написание тестов на Python

ОБРАЗОВАНИЕ
Бакалавр IT, МГУ (2022)

НАВЫКИ
Python, Selenium, SQL, Git
"""

job_posting = """
Middle QA Engineer

Требуется:
- 3+ года опыта тестирования
- Python, Selenium, Pytest
- Опыт с CI/CD
- API Testing, REST
- Знание Agile
- Lead потенциал
"""

coach = CareerCoachCrew()
crew = coach.run_resume_optimization(resume, job_posting)
result = crew.kickoff()

# Результат: оптимизированное резюме с объяснениями
```

### Пример 3: Подготовка к интервью

```python
job_description = """
Middle Python Backend Developer

Требуется:
- 3+ лет опыта с Python
- Django/FastAPI
- PostgreSQL
- API design
- Experience with microservices
"""

company_info = """
TechCorp - растущая IT компания (200+ сотрудников)
Специализация: облачные решения и SaaS
Культура: инновационная, дружная команда
"""

coach = CareerCoachCrew()
crew = coach.run_interview_preparation(job_description, company_info)
result = crew.kickoff()

# Результат:
# 1. Список вероятных вопросов
# 2. STAR-структурированные ответы
# 3. Вопросы для интервьюера
# 4. Рекомендации по поведению
# 5. Информация о компании
```

---

## API Документация

### CareerCoachCrew

```python
class CareerCoachCrew:
    def __init__(
        self,
        model: str = "gpt-4",
        temperature: float = 0.7
    ) -> None:
        """
        Инициализация системы агентов
        
        Args:
            model: Модель LLM (gpt-4, gpt-3.5-turbo, claude-3-opus)
            temperature: Температура генерации (0-1)
        """
```

### Методы

#### `run_full_career_assessment(user_profile: dict) -> Crew`
Запускает полную оценку карьеры

#### `run_resume_optimization(resume: str, job_posting: str) -> Crew`
Оптимизирует резюме для вакансии

#### `run_job_search(criteria: dict) -> Crew`
Ищет подходящие вакансии

#### `run_interview_preparation(job_description: str, company_info: str) -> Crew`
Подготавливает к интервью

#### `run_full_job_application_workflow(...) -> Crew`
Полный процесс применения на работу

---

## Производительность

### Рекомендуемые настройки

| Сценарий | Модель | Температура | Время |
|----------|--------|-------------|-------|
| Быстрая оценка | gpt-3.5-turbo | 0.5 | 2-3 мин |
| Полная оценка | gpt-4 | 0.7 | 5-10 мин |
| Оптимизация резюме | gpt-4 | 0.6 | 1-2 мин |
| Подготовка к интервью | gpt-4 | 0.7 | 3-5 мин |

### Стоимость

Приблизительная стоимость на примере OpenAI API:

- Полная оценка: $0.50-1.50
- Оптимизация резюме: $0.10-0.30
- Подготовка к интервью: $0.30-0.80

---

## Расширение системы

### Добавление нового агента

```python
from crewai import Agent

class NewAgentName:
    def __init__(self, llm=None):
        self.llm = llm
        self.agent = self._create_agent()
    
    def _create_agent(self):
        return Agent(
            role="Роль агента",
            goal="Цель агента",
            backstory="История агента",
            llm=self.llm,
            verbose=True
        )
```

### Добавление новой задачи

```python
from crewai import Task

def create_new_task(agent, params):
    return Task(
        description="Описание задачи",
        agent=agent,
        expected_output="Ожидаемый результат"
    )
```

---

## Устранение проблем

### Проблема: API ошибки

```
OpenAI API Error: Invalid API key
```

**Решение:**
```bash
# Проверьте .env файл
echo $OPENAI_API_KEY

# Убедитесь, что ключ корректный
# Перезагрузитесь
source .env
```

### Проблема: Медленное выполнение

**Решение:**
- Используйте `gpt-3.5-turbo` вместо `gpt-4`
- Уменьшите `max_iter`
- Запускайте агентов параллельно

---

## Лицензия

MIT License

---

## Поддержка

Для вопросов и предложений свяжитесь с командой разработки.
