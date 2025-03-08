import pandas as pd
from datetime import datetime
from typing import Dict, List, Any

class ActivityTracker:
    def __init__(self):
        self.activities = []
        
    def track_activity(self, activity_type: str, details: Dict[str, Any]) -> None:
        """Отслеживание активности пользователя"""
        self.activities.append({
            'timestamp': datetime.now(),
            'type': activity_type,
            'details': details
        })
    
    def get_activity_report(self, start_date: datetime = None, end_date: datetime = None) -> pd.DataFrame:
        """Получение отчета об активности"""
        df = pd.DataFrame(self.activities)
        
        if start_date:
            df = df[df['timestamp'] >= start_date]
        if end_date:
            df = df[df['timestamp'] <= end_date]
            
        return df
    
    def get_productivity_stats(self) -> Dict[str, Any]:
        """Получение статистики продуктивности"""
        if not self.activities:
            return {'message': 'Нет данных для анализа'}
            
        df = pd.DataFrame(self.activities)
        stats = {
            'total_activities': len(df),
            'activity_by_type': df['type'].value_counts().to_dict(),
            'daily_activity': df.groupby(df['timestamp'].dt.date).size().to_dict()
        }
        return stats
    
    def get_recommendations(self) -> List[str]:
        """Получение рекомендаций по улучшению продуктивности"""
        # TODO: Реализовать более сложную логику рекомендаций
        return [
            "Попробуйте делать короткие перерывы каждые 25 минут",
            "Используйте горячие клавиши для частых операций",
            "Документируйте код по мере его написания"
        ] 