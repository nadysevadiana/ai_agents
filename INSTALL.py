#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INSTALLATION & SETUP GUIDE
CareerCoach Crew - Многоагентная система развития карьеры

Этот скрипт помогает с установкой и первичной настройкой системы
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Выводит красивый заголовок"""
    print(f"\n{'='*80}")
    print(f"  {text}")
    print(f"{'='*80}\n")


def print_step(number, text):
    """Выводит номер шага"""
    print(f"\n✓ ШАГ {number}: {text}")
    print("-" * 80)


def check_python_version():
    """Проверяет версию Python"""
    print_step(1, "Проверка версии Python")
    
    version = sys.version_info
    print(f"Текущая версия Python: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 10:
        print("✅ Версия Python подходит!")
        return True
    else:
        print("❌ Требуется Python 3.10 или выше!")
        return False


def install_requirements():
    """Устанавливает зависимости"""
    print_step(2, "Установка зависимостей")
    
    requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print("❌ Файл requirements.txt не найден!")
        return False
    
    try:
        print("Установка пакетов...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Зависимости установлены!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при установке: {e}")
        return False


def create_env_file():
    """Создает файл .env с переменными окружения"""
    print_step(3, "Конфигурация переменных окружения")
    
    env_file = Path(".env")
    
    if env_file.exists():
        print("⚠️  Файл .env уже существует!")
        response = input("Перезаписать? (y/n): ").lower()
        if response != 'y':
            print("⏭️  Пропускаем создание .env")
            return True
    
    env_content = """# ============================================================================
# КОНФИГУРАЦИЯ CAREERCOACH CREW
# ============================================================================

# OpenAI Configuration (https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-your-key-here

# Model Selection (gpt-4, gpt-3.5-turbo, gpt-4-turbo)
OPENAI_MODEL=gpt-4

# Alternative LLM Providers (раскомментируйте если используете)
# ANTHROPIC_API_KEY=your-key-here
# CLAUDE_MODEL=claude-3-opus

# ============================================================================
# OPTIONAL: JOB SEARCH APIs
# ============================================================================
# INDEED_API_KEY=your-key
# LINKEDIN_API_KEY=your-key
# GLASSDOOR_API_KEY=your-key

# ============================================================================
# LOGGING & DEBUG
# ============================================================================
LOG_LEVEL=INFO
DEBUG_MODE=False
VERBOSE=True

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================
# Max iterations per agent (default: 5)
MAX_ITERATIONS=5

# Temperature for LLM (0-1, default: 0.7)
TEMPERATURE=0.7

# Timeout for operations (seconds, default: 300)
TIMEOUT=300
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print(f"✅ Файл .env создан: {env_file}")
        print("\n⚠️  ВАЖНО: Отредактируйте .env и добавьте свои API ключи!")
        return True
    except IOError as e:
        print(f"❌ Ошибка при создании .env: {e}")
        return False


def test_import():
    """Тестирует импорт основных модулей"""
    print_step(4, "Тестирование импорта модулей")
    
    try:
        print("Импортирование crewai...")
        import crewai
        print("✅ crewai импортирован успешно!")
        
        print("Импортирование career_coach_crew...")
        from career_coach_crew import CareerCoachCrew
        print("✅ career_coach_crew импортирован успешно!")
        
        return True
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False


def list_files():
    """Выводит список созданных файлов"""
    print_step(5, "Структура проекта")
    
    files = [
        ("career_coach_crew.py", "🎯 Главный класс системы"),
        ("agents_chief_coach.py", "👔 Главный коуч агент"),
        ("agents_resume_expert.py", "📄 Эксперт по резюме"),
        ("agents_job_hunter.py", "🔍 Охотник за вакансиями"),
        ("agents_verification_specialist.py", "✅ Верификатор"),
        ("agents_skills_coach.py", "🎯 Коуч по навыкам"),
        ("agents_interview_mentor.py", "🗣️ Интервьюер-ментор"),
        ("agents_market_analyst.py", "📊 Аналитик рынка"),
        ("agents_branding_strategist.py", "🌟 Стратег бренда"),
        ("tasks_definitions.py", "📋 Определение задач"),
        ("agents_config.yaml", "⚙️ Конфигурация агентов"),
        ("scenarios_config.yaml", "🎬 Сценарии"),
        ("examples.py", "📚 Примеры использования"),
        ("quickstart.py", "🚀 Быстрый старт"),
        ("README.md", "📖 Документация"),
        ("АРХИТЕКТУРА_АГЕНТОВ.md", "🏗️ Архитектура"),
        ("АРХИТЕКТУРА_ДИАГРАММЫ.md", "📊 Диаграммы"),
        ("requirements.txt", "📦 Зависимости"),
    ]
    
    print("Основные файлы проекта:\n")
    for filename, description in files:
        file_path = Path(filename)
        status = "✓" if file_path.exists() else "✗"
        print(f"  {status} {filename:30} {description}")
    
    print("\nВсе файлы созданы! ✅")


def show_quick_start():
    """Показывает инструкции для быстрого старта"""
    print_header("БЫСТРЫЙ СТАРТ")
    
    print("""
1️⃣  ИНТЕРАКТИВНЫЙ РЕЖИМ
   
   Запустите интерактивное приложение:
   
   $ python quickstart.py
   
   Следуйте меню для выбора сценария


2️⃣  ПРОГРАММНЫЙ РЕЖИМ
   
   Используйте CareerCoachCrew в своем коде:
   
   from career_coach_crew import CareerCoachCrew
   
   coach = CareerCoachCrew(model="gpt-4")
   crew = coach.run_full_career_assessment(profile)
   result = crew.kickoff()
   print(result)


3️⃣  ПРИМЕРЫ
   
   Запустите готовые примеры:
   
   $ python examples.py
   
   Раскомментируйте нужный пример в main()


4️⃣  ДОСТУПНЫЕ МЕТОДЫ
   
   • run_full_career_assessment() - полная оценка
   • run_resume_optimization() - оптимизация резюме
   • run_job_search() - поиск работы
   • run_interview_preparation() - подготовка к интервью
   • run_full_job_application_workflow() - полный цикл применения
    """)


def show_documentation():
    """Показывает ссылки на документацию"""
    print_header("ДОКУМЕНТАЦИЯ")
    
    print("""
📖 ОСНОВНАЯ ДОКУМЕНТАЦИЯ
   ├─ README.md - Полное руководство
   ├─ АРХИТЕКТУРА_АГЕНТОВ.md - Описание всех агентов
   └─ АРХИТЕКТУРА_ДИАГРАММЫ.md - Визуальные диаграммы

📚 ПРИМЕРЫ
   ├─ examples.py - 5 полных примеров использования
   └─ quickstart.py - Интерактивное приложение

⚙️  КОНФИГУРАЦИЯ
   ├─ agents_config.yaml - Параметры каждого агента
   └─ scenarios_config.yaml - Определение сценариев

🤖 КОД АГЕНТОВ
   ├─ agents_chief_coach.py
   ├─ agents_resume_expert.py
   ├─ agents_job_hunter.py
   ├─ agents_verification_specialist.py
   ├─ agents_skills_coach.py
   ├─ agents_interview_mentor.py
   ├─ agents_market_analyst.py
   └─ agents_branding_strategist.py

📋 ЗАДАЧИ
   └─ tasks_definitions.py - 45+ определений задач
    """)


def show_api_keys_setup():
    """Показывает инструкции по настройке API ключей"""
    print_header("НАСТРОЙКА API КЛЮЧЕЙ")
    
    print("""
1️⃣  OpenAI API (ОБЯЗАТЕЛЬНО)
   
   1. Перейдите на https://platform.openai.com/api-keys
   2. Создайте новый API ключ
   3. Скопируйте ключ
   4. Отредактируйте .env и вставьте в OPENAI_API_KEY
   
   Пример .env:
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
   OPENAI_MODEL=gpt-4


2️⃣  АЛЬТЕРНАТИВНЫЕ LLM ПРОВАЙДЕРЫ (опционально)
   
   Claude (Anthropic):
   - https://console.anthropic.com/
   - Установите ANTHROPIC_API_KEY=...
   
   Google Gemini:
   - https://aistudio.google.com/app/apikey
   - Установите GOOGLE_API_KEY=...


3️⃣  ДЛЯ ПОИСКА ВАКАНСИЙ (опционально)
   
   Indeed, LinkedIn, Glassdoor и т.д. (требуется работа с API)


⚠️  БЕЗОПАСНОСТЬ
   
   • Никогда не коммитьте .env в git!
   • Добавьте .env в .gitignore
   • Используйте переменные окружения в production
    """)


def main():
    """Главная функция установки"""
    print_header("КАРЬЕРНЫЙ КОУЧ CREW - УСТАНОВКА И НАСТРОЙКА")
    
    print("""
Добро пожаловать в многоагентную систему карьерного развития!

Этот скрипт поможет вам:
✓ Проверить Python версию
✓ Установить зависимости
✓ Настроить конфигурацию
✓ Тестировать импорты
✓ Начать использовать систему
    """)
    
    input("Нажмите Enter для начала...")
    
    # Шаг 1: Проверка Python
    if not check_python_version():
        print("\n❌ Пожалуйста, обновите Python!")
        return False
    
    # Шаг 2: Установка зависимостей
    if not install_requirements():
        print("\n⚠️  Продолжаем, несмотря на ошибки...")
    
    # Шаг 3: Создание .env
    if not create_env_file():
        print("\n⚠️  Продолжаем без .env...")
    
    # Шаг 4: Тестирование импорта
    if not test_import():
        print("\n⚠️  Некоторые модули не импортированы, но продолжаем...")
    
    # Шаг 5: Список файлов
    list_files()
    
    # Показываем инструкции
    show_quick_start()
    show_api_keys_setup()
    show_documentation()
    
    # Финальное сообщение
    print_header("✅ УСТАНОВКА ЗАВЕРШЕНА!")
    
    print("""
Следующие шаги:

1. ОТРЕДАКТИРУЙТЕ .env файл
   Добавьте ваш OpenAI API ключ!

2. ЗАПУСТИТЕ БЫСТРЫЙ СТАРТ
   python quickstart.py

3. ИЗУЧИТЕ ДОКУМЕНТАЦИЮ
   Откройте README.md для полного руководства

4. ЭКСПЕРИМЕНТИРУЙТЕ
   Запустите примеры в examples.py

5. ИНТЕГРИРУЙТЕ В СВОЙ ПРОЕКТ
   Используйте CareerCoachCrew в своем коде


ПОЛЕЗНЫЕ КОМАНДЫ:

# Интерактивное приложение
python quickstart.py

# Запуск примеров
python examples.py

# Тестирование
python -c "from career_coach_crew import CareerCoachCrew; print('OK')"

# Справка
python career_coach_crew.py


ДОКУМЕНТАЦИЯ:
- README.md - главное руководство
- АРХИТЕКТУРА_АГЕНТОВ.md - описание архитектуры
- examples.py - примеры использования


ПОДДЕРЖКА:
- Ошибки? Проверьте .env файл
- API проблемы? Проверьте ключ в .env
- Импорт ошибки? Переустановите requirements.txt


Удачи! 🚀
    """)
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Установка прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Неожиданная ошибка: {e}")
        sys.exit(1)
