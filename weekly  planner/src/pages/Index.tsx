
import React, { useState, useEffect } from 'react';
import { Calendar, Plus, Filter, TrendingUp, CheckCircle, Clock, AlertCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import TaskCard from '@/components/TaskCard';
import AddTaskModal from '@/components/AddTaskModal';
import WeeklyCalendar from '@/components/WeeklyCalendar';
import { Task, TaskStatus, TaskCategory } from '@/types/Task';

const Index = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isAddTaskOpen, setIsAddTaskOpen] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState<TaskCategory | 'all'>('all');
  const [selectedDay, setSelectedDay] = useState<string>('');

  // Sample tasks for demonstration
  useEffect(() => {
    const sampleTasks: Task[] = [
      {
        id: '1',
        title: 'Complete React Authentication System',
        description: 'Implement user login and signup functionality',
        category: 'Programming',
        status: 'in-progress',
        priority: 'high',
        estimatedTime: 4,
        dueDate: new Date().toISOString().split('T')[0],
        notes: 'Focus on JWT token implementation'
      },
      {
        id: '2',
        title: 'Study Web Application Security',
        description: 'Review OWASP Top 10 vulnerabilities',
        category: 'Ethical Hacking',
        status: 'not-started',
        priority: 'medium',
        estimatedTime: 2,
        dueDate: new Date(Date.now() + 86400000).toISOString().split('T')[0],
        notes: 'Prepare for security assessment'
      },
      {
        id: '3',
        title: 'Design Game Character Sprites',
        description: 'Create pixel art characters for indie game',
        category: 'Game Development',
        status: 'completed',
        priority: 'medium',
        estimatedTime: 3,
        dueDate: new Date(Date.now() - 86400000).toISOString().split('T')[0],
        notes: 'Completed 8 character variations'
      }
    ];
    setTasks(sampleTasks);
  }, []);

  const addTask = (newTask: Omit<Task, 'id'>) => {
    const task: Task = {
      ...newTask,
      id: Date.now().toString()
    };
    setTasks(prev => [...prev, task]);
  };

  const updateTask = (taskId: string, updates: Partial<Task>) => {
    setTasks(prev => prev.map(task => 
      task.id === taskId ? { ...task, ...updates } : task
    ));
  };

  const deleteTask = (taskId: string) => {
    setTasks(prev => prev.filter(task => task.id !== taskId));
  };

  const filteredTasks = tasks.filter(task => {
    const categoryMatch = selectedCategory === 'all' || task.category === selectedCategory;
    const dayMatch = !selectedDay || task.dueDate === selectedDay;
    return categoryMatch && dayMatch;
  });

  const completedTasks = tasks.filter(task => task.status === 'completed').length;
  const totalTasks = tasks.length;
  const completionPercentage = totalTasks > 0 ? (completedTasks / totalTasks) * 100 : 0;

  const todaysTasks = tasks.filter(task => 
    task.dueDate === new Date().toISOString().split('T')[0]
  );

  const categories: { label: string; value: TaskCategory | 'all'; color: string }[] = [
    { label: 'All Tasks', value: 'all', color: 'bg-gray-500' },
    { label: 'Programming', value: 'Programming', color: 'bg-blue-500' },
    { label: 'Ethical Hacking', value: 'Ethical Hacking', color: 'bg-red-500' },
    { label: 'Game Development', value: 'Game Development', color: 'bg-purple-500' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
          <div>
            <h1 className="text-4xl font-bold text-gray-900 mb-2">Weekly Planner</h1>
            <p className="text-gray-600">Plan, track, and achieve your coding goals</p>
          </div>
          <Button 
            onClick={() => setIsAddTaskOpen(true)}
            className="mt-4 md:mt-0 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white shadow-lg hover:shadow-xl transition-all duration-300"
            size="lg"
          >
            <Plus className="w-5 h-5 mr-2" />
            Add Task
          </Button>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300 bg-gradient-to-br from-blue-500 to-blue-600 text-white">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium opacity-90">Total Tasks</CardTitle>
              <CheckCircle className="h-4 w-4 opacity-80" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{totalTasks}</div>
              <p className="text-xs opacity-80 mt-1">Active planning items</p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300 bg-gradient-to-br from-green-500 to-green-600 text-white">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium opacity-90">Completed</CardTitle>
              <TrendingUp className="h-4 w-4 opacity-80" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{completedTasks}</div>
              <p className="text-xs opacity-80 mt-1">{completionPercentage.toFixed(0)}% completion rate</p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300 bg-gradient-to-br from-orange-500 to-orange-600 text-white">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium opacity-90">Today's Tasks</CardTitle>
              <Clock className="h-4 w-4 opacity-80" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{todaysTasks.length}</div>
              <p className="text-xs opacity-80 mt-1">Due today</p>
            </CardContent>
          </Card>

          <Card className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300 bg-gradient-to-br from-purple-500 to-purple-600 text-white">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium opacity-90">Weekly Progress</CardTitle>
              <AlertCircle className="h-4 w-4 opacity-80" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{completionPercentage.toFixed(0)}%</div>
              <Progress value={completionPercentage} className="mt-2 bg-purple-400/30" />
            </CardContent>
          </Card>
        </div>

        {/* Weekly Calendar */}
        <Card className="mb-8 border-0 shadow-xl">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-xl">
              <Calendar className="w-6 h-6 text-blue-600" />
              Weekly Overview
            </CardTitle>
          </CardHeader>
          <CardContent>
            <WeeklyCalendar 
              tasks={tasks} 
              onDaySelect={setSelectedDay}
              selectedDay={selectedDay}
            />
          </CardContent>
        </Card>

        {/* Category Filters */}
        <div className="flex flex-wrap gap-3 mb-6">
          {categories.map((category) => (
            <Badge
              key={category.value}
              variant={selectedCategory === category.value ? "default" : "secondary"}
              className={`cursor-pointer px-4 py-2 text-sm transition-all duration-200 hover:scale-105 ${
                selectedCategory === category.value 
                  ? `${category.color} text-white shadow-lg` 
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
              onClick={() => setSelectedCategory(category.value)}
            >
              <Filter className="w-4 h-4 mr-2" />
              {category.label}
            </Badge>
          ))}
        </div>

        {/* Tasks Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTasks.map((task) => (
            <TaskCard
              key={task.id}
              task={task}
              onUpdate={updateTask}
              onDelete={deleteTask}
            />
          ))}
        </div>

        {filteredTasks.length === 0 && (
          <Card className="border-0 shadow-lg bg-gradient-to-br from-gray-50 to-gray-100">
            <CardContent className="text-center py-12">
              <div className="text-gray-400 mb-4">
                <CheckCircle className="w-16 h-16 mx-auto" />
              </div>
              <h3 className="text-xl font-semibold text-gray-600 mb-2">No tasks found</h3>
              <p className="text-gray-500">
                {selectedCategory === 'all' 
                  ? "Start by adding your first task!" 
                  : `No tasks in ${selectedCategory} category`
                }
              </p>
            </CardContent>
          </Card>
        )}

        <AddTaskModal
          isOpen={isAddTaskOpen}
          onClose={() => setIsAddTaskOpen(false)}
          onAdd={addTask}
        />
      </div>
    </div>
  );
};

export default Index;
