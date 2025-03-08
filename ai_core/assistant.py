import torch
from transformers import pipeline
import nltk
import re
from typing import List, Dict

class AIAssistant:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.code_analyzer = pipeline("text-classification", device=self.device)
        self.sentiment_analyzer = pipeline("sentiment-analysis", device=self.device)
        nltk.download('punkt')
        
    def analyze_code(self, code: str) -> Dict:
        """Анализ кода и поиск потенциальных проблем"""
        return {
            'issues': self._find_code_issues(code),
            'suggestions': self._generate_suggestions(code)
        }
    
    def generate_joke(self, context: str) -> str:
        """Генерация контекстной шутки"""
        # TODO: Реализовать генерацию шуток на основе контекста
        return "Почему программисты не любят природу? Потому что там слишком много багов!"
    
    def _find_code_issues(self, code: str) -> List[str]:
        """Поиск проблем в коде"""
        issues = []
        
        # Проверка на пустые функции
        if re.search(r'def\s+\w+\s*\([^)]*\)\s*:', code) and not re.search(r'def\s+\w+\s*\([^)]*\)\s*:.*\n\s+\w+', code):
            issues.append("Обнаружены пустые функции")
            
        # Проверка на слишком длинные строки
        for line in code.split('\n'):
            if len(line.strip()) > 79:
                issues.append("Строка превышает рекомендуемую длину (79 символов)")
                
        # Проверка на отсутствие документации
        if re.search(r'def\s+\w+\s*\([^)]*\)\s*:', code) and not re.search(r'"""[\s\S]*?"""', code):
            issues.append("Отсутствует документация функций")
            
        # Проверка на неиспользуемые импорты
        imports = re.findall(r'import\s+(\w+)', code)
        for imp in imports:
            if imp not in code.replace(f'import {imp}', ''):
                issues.append(f"Неиспользуемый импорт: {imp}")
                
        # Проверка на множественные пробелы
        if re.search(r'  +', code):
            issues.append("Обнаружены множественные пробелы")
            
        return issues
    
    def _generate_suggestions(self, code: str) -> List[str]:
        """Генерация предложений по улучшению кода"""
        suggestions = []
        
        # Предложения по документации
        if not re.search(r'"""[\s\S]*?"""', code):
            suggestions.append("Добавьте документацию к функциям используя docstrings")
            
        # Предложения по именованию
        if re.search(r'[A-Z]+_*[A-Z]+', code):
            suggestions.append("Используйте snake_case для именования переменных и функций")
            
        # Предложения по структуре
        if len(code.split('\n')) > 20:
            suggestions.append("Рассмотрите возможность разделения кода на меньшие функции")
            
        # Предложения по импортам
        if 'import *' in code:
            suggestions.append("Избегайте использования 'import *', импортируйте конкретные модули")
            
        # Предложения по обработке ошибок
        if not re.search(r'try\s*:', code):
            suggestions.append("Добавьте обработку исключений с помощью try-except")
            
        # Предложения по комментариям
        if not re.search(r'#', code):
            suggestions.append("Добавьте комментарии к сложным участкам кода")
            
        return suggestions
    
    def process_voice_command(self, audio_data: bytes) -> str:
        """Обработка голосовых команд"""
        # TODO: Реализовать обработку голосовых команд
        return "Команда распознана" 