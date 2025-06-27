
export type TaskStatus = 'not-started' | 'in-progress' | 'completed';
export type TaskCategory = 'Programming' | 'Ethical Hacking' | 'Game Development';
export type TaskPriority = 'low' | 'medium' | 'high';

export interface Task {
  id: string;
  title: string;
  description: string;
  category: TaskCategory;
  status: TaskStatus;
  priority: TaskPriority;
  estimatedTime: number; // in hours
  dueDate: string; // YYYY-MM-DD format
  notes?: string;
  createdAt?: string;
  updatedAt?: string;
}
