"""
CareerCoach Crew - Главная точка входа для многоагентной системы карьерного развития
"""

from crewai import Crew, Process
from crewai.llm import LLM

# Импортируем все агенты
from agents_chief_coach import ChiefCoachAgent
from agents_resume_expert import ResumeExpertAgent
from agents_job_hunter import JobHunterAgent
from agents_verification_specialist import VerificationSpecialistAgent
from agents_skills_coach import SkillsDevelopmentCoachAgent
from agents_interview_mentor import InterviewMentorAgent
from agents_market_analyst import MarketAnalystAgent
from agents_branding_strategist import BrandingStrategistAgent

# Импортируем задачи
from tasks_definitions import (
    create_chief_coach_assessment_task,
    create_career_strategy_task,
    create_progress_monitoring_task,
    create_resume_analysis_task,
    create_resume_optimization_task,
    create_job_search_task,
    create_job_requirements_analysis_task,
    create_skills_gap_analysis_task,
    create_interview_prep_task,
    create_market_analysis_task,
    create_personal_brand_strategy_task,
    create_linkedin_optimization_task,
)


class CareerCoachCrew:
    """Главный класс для управления многоагентной системой"""
    
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        """
        Инициализация системы агентов
        
        Args:
            model: Модель LLM (gpt-4, gpt-3.5-turbo, claude-3-opus и т.д.)
            temperature: Температура для генерации (0-1)
        """
        self.model = model
        self.temperature = temperature
        
        # Создаем LLM конфигурацию
        self.llm = LLM(model=model, temperature=temperature)
        
        # Инициализируем агентов
        self.chief_coach = ChiefCoachAgent(llm=self.llm).agent
        self.resume_expert = ResumeExpertAgent(llm=self.llm).agent
        self.job_hunter = JobHunterAgent(llm=self.llm).agent
        self.verification_specialist = VerificationSpecialistAgent(llm=self.llm).agent
        self.skills_coach = SkillsDevelopmentCoachAgent(llm=self.llm).agent
        self.interview_mentor = InterviewMentorAgent(llm=self.llm).agent
        self.market_analyst = MarketAnalystAgent(llm=self.llm).agent
        self.branding_strategist = BrandingStrategistAgent(llm=self.llm).agent
    
    def run_full_career_assessment(self, user_profile: dict) -> Crew:
        """
        Запускает полную оценку карьеры и разработку стратегии
        
        Args:
            user_profile: Словарь с информацией о пользователе
                {
                    'name': str,
                    'current_position': str,
                    'experience_years': int,
                    'skills': list,
                    'education': str,
                    'goals': str,
                    'preferences': dict
                }
        
        Returns:
            Crew: Объект Crew с задачами
        """
        tasks = [
            create_chief_coach_assessment_task(self.chief_coach, user_profile),
            create_career_strategy_task(self.chief_coach, user_profile),
            create_market_analysis_task(self.market_analyst, user_profile.get('specialization', 'IT')),
            create_skills_gap_analysis_task(
                self.skills_coach,
                user_profile.get('skills', []),
                user_profile.get('goals', '')
            ),
            create_personal_brand_strategy_task(self.branding_strategist, user_profile),
        ]
        
        crew = Crew(
            agents=[
                self.chief_coach,
                self.market_analyst,
                self.skills_coach,
                self.branding_strategist,
                self.verification_specialist,
            ],
            tasks=tasks,
            process=Process.hierarchical,
            manager_agent=self.chief_coach,
            verbose=True,
        )
        
        return crew
    
    def run_resume_optimization(self, resume: str, job_posting: str) -> Crew:
        """
        Оптимизирует резюме для конкретной вакансии
        
        Args:
            resume: Текущее резюме
            job_posting: Описание вакансии
        
        Returns:
            Crew: Объект Crew с задачами
        """
        tasks = [
            create_resume_analysis_task(self.resume_expert, resume),
            create_job_requirements_analysis_task(self.job_hunter, job_posting),
            create_resume_optimization_task(self.resume_expert, resume, job_posting),
        ]
        
        crew = Crew(
            agents=[
                self.resume_expert,
                self.job_hunter,
                self.verification_specialist,
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
        )
        
        return crew
    
    def run_job_search(self, criteria: dict) -> Crew:
        """
        Запускает процесс поиска работы
        
        Args:
            criteria: Критерии поиска работы
                {
                    'position': str,
                    'industry': str,
                    'location': str,
                    'salary_range': (min, max),
                    'required_skills': list
                }
        
        Returns:
            Crew: Объект Crew с задачами
        """
        tasks = [
            create_job_search_task(self.job_hunter, criteria),
            create_market_analysis_task(self.market_analyst, criteria.get('position')),
        ]
        
        crew = Crew(
            agents=[
                self.job_hunter,
                self.market_analyst,
                self.verification_specialist,
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
        )
        
        return crew
    
    def run_interview_preparation(self, job_description: str, company_info: str) -> Crew:
        """
        Подготавливает кандидата к интервью
        
        Args:
            job_description: Описание должности
            company_info: Информация о компании
        
        Returns:
            Crew: Объект Crew с задачами
        """
        tasks = [
            create_interview_prep_task(self.interview_mentor, job_description, company_info),
            create_market_analysis_task(self.market_analyst, job_description),
        ]
        
        crew = Crew(
            agents=[
                self.interview_mentor,
                self.market_analyst,
                self.verification_specialist,
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
        )
        
        return crew
    
    def run_full_job_application_workflow(self, user_profile: dict, job_posting: str, company: str) -> Crew:
        """
        Полный процесс подготовки к применению на работу
        
        Args:
            user_profile: Профиль пользователя
            job_posting: Описание вакансии
            company: Информация о компании
        
        Returns:
            Crew: Объект Crew с задачами
        """
        tasks = [
            create_job_requirements_analysis_task(self.job_hunter, job_posting),
            create_resume_optimization_task(self.resume_expert, user_profile.get('resume', ''), job_posting),
            create_interview_prep_task(self.interview_mentor, job_posting, company),
            create_market_analysis_task(self.market_analyst, job_posting),
            create_personal_brand_strategy_task(self.branding_strategist, user_profile),
        ]
        
        crew = Crew(
            agents=[
                self.job_hunter,
                self.resume_expert,
                self.interview_mentor,
                self.market_analyst,
                self.branding_strategist,
                self.verification_specialist,
                self.chief_coach,
            ],
            tasks=tasks,
            process=Process.hierarchical,
            manager_agent=self.chief_coach,
            verbose=True,
        )
        
        return crew


# ============== ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ==============

def example_full_assessment():
    """Пример: Полная оценка карьеры"""
    print("\n" + "="*80)
    print("ПРИМЕР: Полная оценка и стратегия развития карьеры")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    user_profile = {
        'name': 'Иван Петров',
        'current_position': 'Middle Python Developer',
        'experience_years': 5,
        'skills': ['Python', 'Django', 'PostgreSQL', 'REST API', 'Git'],
        'education': 'Бакалавр Computer Science',
        'specialization': 'Backend Development',
        'goals': 'Получить позицию Senior Developer и возглавить команду',
        'preferences': {
            'remote': True,
            'salary_expectation': '150000-200000',
            'location': 'Russia or Remote'
        },
        'resume': 'Краткое резюме разработчика...'
    }
    
    crew = coach.run_full_career_assessment(user_profile)
    result = crew.kickoff()
    
    print("\n" + "="*80)
    print("РЕЗУЛЬТАТ ОЦЕНКИ:")
    print("="*80)
    print(result)


def example_resume_optimization():
    """Пример: Оптимизация резюме"""
    print("\n" + "="*80)
    print("ПРИМЕР: Оптимизация резюме для вакансии")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    resume = """
    ИВАН ПЕТРОВ
    Email: ivan@example.com | Phone: +7-900-123-4567
    
    ОПЫТ
    Middle Python Developer at TechCorp (2020-2024)
    - Разработка REST API
    - Работа с Django и PostgreSQL
    
    НАВЫКИ
    Python, Django, PostgreSQL, Git, Docker
    """
    
    job_posting = """
    Senior Backend Developer
    Требуется:
    - 5+ лет опыта с Python
    - Опыт с Django и PostgreSQL
    - Leadership skills и опыт работы в команде
    - Опыт с микросервисной архитектурой
    - Опыт с DevOps и Docker/Kubernetes
    """
    
    crew = coach.run_resume_optimization(resume, job_posting)
    result = crew.kickoff()
    
    print("\n" + "="*80)
    print("ОПТИМИЗИРОВАННОЕ РЕЗЮМЕ:")
    print("="*80)
    print(result)


def example_full_job_application():
    """Пример: Полный процесс подготовки к применению"""
    print("\n" + "="*80)
    print("ПРИМЕР: Полный процесс подготовки к применению на работу")
    print("="*80 + "\n")
    
    coach = CareerCoachCrew(model="gpt-4")
    
    user_profile = {
        'name': 'Анна Сидорова',
        'current_position': 'Middle QA Engineer',
        'experience_years': 4,
        'skills': ['Python', 'Selenium', 'Jest', 'API Testing', 'Test Automation'],
        'education': 'Бакалавр IT',
        'goals': 'Перейти в Senior QA или в Test Lead позицию',
        'resume': 'Резюме QA инженера...'
    }
    
    job_posting = """
    Senior QA Engineer (Test Lead)
    Компания: InnovateTech
    
    Требуется:
    - 5+ лет опыта в QA
    - Опыт автоматизации тестирования
    - Python или Java
    - Опыт с CI/CD и DevOps
    - Leadership опыт
    - Знание Agile методологии
    """
    
    company_info = """
    InnovateTech - молодая IT компания, специализирующаяся на облачных решениях.
    Около 200 сотрудников, быстрое развитие.
    """
    
    crew = coach.run_full_job_application_workflow(user_profile, job_posting, company_info)
    result = crew.kickoff()
    
    print("\n" + "="*80)
    print("РЕЗУЛЬТАТ ПОДГОТОВКИ К ПРИМЕНЕНИЮ:")
    print("="*80)
    print(result)


if __name__ == "__main__":
    # Раскомментируйте нужный пример для запуска
    
    # Пример 1: Полная оценка карьеры
    # example_full_assessment()
    
    # Пример 2: Оптимизация резюме
    # example_resume_optimization()
    
    # Пример 3: Полный процесс подготовки к применению
    # example_full_job_application()
    
    print("""
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║       CAREER COACH CREW - Многоагентная система развития карьеры         ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    
    Эта система содержит 8 специализированных агентов:
    
    1. 👔 Главный Коуч (Chief Career Coach)
       - Координирует все процессы
       - Разрабатывает стратегию развития
       - Мониторит прогресс
    
    2. 📄 Эксперт по Резюме (Resume Expert)
       - Создает и оптимизирует резюме
       - ATS-оптимизация
       - Адаптация под вакансии
    
    3. 🔍 Охотник за Вакансиями (Job Hunter)
       - Ищет подходящие вакансии
       - Анализирует требования
       - Исследует компании
    
    4. ✅ Верификатор (Verification Specialist)
       - Проверяет качество
       - Валидирует согласованность
       - QA всех материалов
    
    5. 🎯 Коуч по Навыкам (Skills Coach)
       - Выявляет пробелы
       - Рекомендует обучение
       - Планирует развитие
    
    6. 🗣️ Интервьюер-Ментор (Interview Mentor)
       - Подготавливает к интервью
       - STAR-ответы
       - Практикование
    
    7. 📊 Аналитик Рынка (Market Analyst)
       - Анализирует тренды
       - Исследует зарплаты
       - Дает рыночный контекст
    
    8. 🌟 Стратег Бренда (Branding Strategist)
       - Развивает персональный бренд
       - Оптимизирует LinkedIn
       - Создает портфолио
    
    ═══════════════════════════════════════════════════════════════════════════
    
    ИСПОЛЬЗОВАНИЕ:
    
    from career_coach_crew import CareerCoachCrew
    
    # Инициализация
    coach = CareerCoachCrew(model="gpt-4")
    
    # Запуск полной оценки
    crew = coach.run_full_career_assessment(user_profile)
    result = crew.kickoff()
    
    # Запуск оптимизации резюме
    crew = coach.run_resume_optimization(resume, job_posting)
    result = crew.kickoff()
    
    # Запуск поиска работы
    crew = coach.run_job_search(criteria)
    result = crew.kickoff()
    
    # Подготовка к интервью
    crew = coach.run_interview_preparation(job_desc, company_info)
    result = crew.kickoff()
    
    # Полный процесс применения на работу
    crew = coach.run_full_job_application_workflow(profile, job, company)
    result = crew.kickoff()
    
    ═══════════════════════════════════════════════════════════════════════════
    """)
