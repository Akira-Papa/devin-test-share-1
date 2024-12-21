import { Task, TaskStatus } from '../agents/types';

export interface WorkflowResult {
  id: string;
  status: WorkflowStatus;
  tasks: Task[];
  error?: Error;
}

export enum WorkflowStatus {
  PENDING = 'PENDING',
  RUNNING = 'RUNNING',
  COMPLETED = 'COMPLETED',
  FAILED = 'FAILED'
}
