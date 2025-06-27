
import React from 'react';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Task } from '@/types/Task';

interface WeeklyCalendarProps {
  tasks: Task[];
  onDaySelect: (date: string) => void;
  selectedDay: string;
}

const WeeklyCalendar: React.FC<WeeklyCalendarProps> = ({ tasks, onDaySelect, selectedDay }) => {
  const getWeekDays = () => {
    const today = new Date();
    const currentDay = today.getDay();
    const startOfWeek = new Date(today);
    startOfWeek.setDate(today.getDate() - currentDay + 1); // Start from Monday

    const days = [];
    for (let i = 0; i < 7; i++) {
      const day = new Date(startOfWeek);
      day.setDate(startOfWeek.getDate() + i);
      days.push(day);
    }
    return days;
  };

  const weekDays = getWeekDays();
  const dayNames = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

  const getTasksForDay = (date: Date) => {
    const dateString = date.toISOString().split('T')[0];
    return tasks.filter(task => task.dueDate === dateString);
  };

  const getCategoryColor = (category: string) => {
    switch (category) {
      case 'Programming': return 'bg-blue-500';
      case 'Ethical Hacking': return 'bg-red-500';
      case 'Game Development': return 'bg-purple-500';
      default: return 'bg-gray-500';
    }
  };

  const isToday = (date: Date) => {
    const today = new Date();
    return date.toDateString() === today.toDateString();
  };

  return (
    <div className="grid grid-cols-7 gap-2">
      {weekDays.map((day, index) => {
        const dayTasks = getTasksForDay(day);
        const completedTasks = dayTasks.filter(task => task.status === 'completed').length;
        const dateString = day.toISOString().split('T')[0];
        const isSelected = selectedDay === dateString;

        return (
          <Card
            key={index}
            onClick={() => onDaySelect(isSelected ? '' : dateString)}
            className={`p-3 cursor-pointer transition-all duration-200 hover:shadow-md ${
              isSelected ? 'ring-2 ring-blue-500 bg-blue-50' : 'hover:bg-gray-50'
            } ${isToday(day) ? 'border-orange-300 bg-orange-50' : ''}`}
          >
            <div className="text-center">
              <div className="text-xs font-medium text-gray-500 mb-1">
                {dayNames[index]}
              </div>
              <div className={`text-lg font-bold mb-2 ${
                isToday(day) ? 'text-orange-600' : 'text-gray-900'
              }`}>
                {day.getDate()}
              </div>
              
              {dayTasks.length > 0 && (
                <div className="space-y-1">
                  <div className="text-xs text-gray-600">
                    {completedTasks}/{dayTasks.length} completed
                  </div>
                  <div className="flex flex-wrap justify-center gap-1">
                    {dayTasks.slice(0, 3).map((task, taskIndex) => (
                      <div
                        key={taskIndex}
                        className={`w-2 h-2 rounded-full ${getCategoryColor(task.category)} ${
                          task.status === 'completed' ? 'opacity-100' : 'opacity-50'
                        }`}
                      />
                    ))}
                    {dayTasks.length > 3 && (
                      <div className="text-xs text-gray-500">
                        +{dayTasks.length - 3}
                      </div>
                    )}
                  </div>
                </div>
              )}
              
              {dayTasks.length === 0 && (
                <div className="text-xs text-gray-400">
                  No tasks
                </div>
              )}
            </div>
          </Card>
        );
      })}
    </div>
  );
};

export default WeeklyCalendar;
