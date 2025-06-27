
import React, { useState } from 'react';
import { Clock, Edit, Trash2, CheckCircle, Circle, PlayCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Task, TaskStatus } from '@/types/Task';
import EditTaskModal from './EditTaskModal';

interface TaskCardProps {
  task: Task;
  onUpdate: (taskId: string, updates: Partial<Task>) => void;
  onDelete: (taskId: string) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onUpdate, onDelete }) => {
  const [isEditOpen, setIsEditOpen] = useState(false);

  const getStatusColor = (status: TaskStatus) => {
    switch (status) {
      case 'completed': return 'bg-green-500';
      case 'in-progress': return 'bg-yellow-500';
      default: return 'bg-gray-400';
    }
  };

  const getCategoryColor = (category: string) => {
    switch (category) {
      case 'Programming': return 'bg-blue-500';
      case 'Ethical Hacking': return 'bg-red-500';
      case 'Game Development': return 'bg-purple-500';
      default: return 'bg-gray-500';
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high': return 'bg-red-100 text-red-800 border-red-200';
      case 'medium': return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'low': return 'bg-green-100 text-green-800 border-green-200';
      default: return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const handleStatusChange = () => {
    const statusMap: Record<TaskStatus, TaskStatus> = {
      'not-started': 'in-progress',
      'in-progress': 'completed',
      'completed': 'not-started'
    };
    onUpdate(task.id, { status: statusMap[task.status] });
  };

  const getStatusIcon = (status: TaskStatus) => {
    switch (status) {
      case 'completed': return <CheckCircle className="w-5 h-5 text-green-600" />;
      case 'in-progress': return <PlayCircle className="w-5 h-5 text-yellow-600" />;
      default: return <Circle className="w-5 h-5 text-gray-400" />;
    }
  };

  const isOverdue = new Date(task.dueDate) < new Date() && task.status !== 'completed';
  const isToday = task.dueDate === new Date().toISOString().split('T')[0];

  return (
    <>
      <Card className={`border-0 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 ${
        isOverdue ? 'ring-2 ring-red-200 bg-red-50' : 'bg-white'
      }`}>
        <CardHeader className="pb-3">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <CardTitle className="text-lg font-semibold text-gray-900 mb-2 line-clamp-2">
                {task.title}
              </CardTitle>
              <div className="flex flex-wrap gap-2">
                <Badge className={`${getCategoryColor(task.category)} text-white text-xs`}>
                  {task.category}
                </Badge>
                <Badge variant="outline" className={`text-xs ${getPriorityColor(task.priority)}`}>
                  {task.priority}
                </Badge>
                {isToday && (
                  <Badge className="bg-orange-500 text-white text-xs">
                    Due Today
                  </Badge>
                )}
                {isOverdue && (
                  <Badge className="bg-red-500 text-white text-xs">
                    Overdue
                  </Badge>
                )}
              </div>
            </div>
            <button
              onClick={handleStatusChange}
              className="ml-2 hover:scale-110 transition-transform duration-200"
            >
              {getStatusIcon(task.status)}
            </button>
          </div>
        </CardHeader>

        <CardContent className="pt-0">
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">
            {task.description}
          </p>

          <div className="flex items-center justify-between text-sm text-gray-500 mb-4">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-1">
                <Clock className="w-4 h-4" />
                <span>{task.estimatedTime}h</span>
              </div>
              <div>
                Due: {new Date(task.dueDate).toLocaleDateString()}
              </div>
            </div>
          </div>

          <div className={`w-full h-2 rounded-full mb-4 ${getStatusColor(task.status)} opacity-20`}>
            <div 
              className={`h-full rounded-full ${getStatusColor(task.status)} transition-all duration-500`}
              style={{ 
                width: task.status === 'completed' ? '100%' : 
                       task.status === 'in-progress' ? '50%' : '10%' 
              }}
            />
          </div>

          {task.notes && (
            <p className="text-xs text-gray-500 mb-4 italic">
              "{task.notes}"
            </p>
          )}

          <div className="flex gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setIsEditOpen(true)}
              className="flex-1 hover:bg-blue-50 hover:border-blue-300"
            >
              <Edit className="w-4 h-4 mr-1" />
              Edit
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => onDelete(task.id)}
              className="flex-1 hover:bg-red-50 hover:border-red-300 hover:text-red-600"
            >
              <Trash2 className="w-4 h-4 mr-1" />
              Delete
            </Button>
          </div>
        </CardContent>
      </Card>

      <EditTaskModal
        task={task}
        isOpen={isEditOpen}
        onClose={() => setIsEditOpen(false)}
        onUpdate={onUpdate}
      />
    </>
  );
};

export default TaskCard;
