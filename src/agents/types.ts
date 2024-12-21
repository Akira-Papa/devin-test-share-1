export interface IAgent {
  id: string;
  type: AgentType;
  status: AgentStatus;
  capabilities: string[];
  handleTask(task: Task): Promise<TaskResult>;
  communicate(message: Message): Promise<void>;
}

export enum AgentType {
  PLANNER = 'PLANNER',
  CODER = 'CODER',
  REVIEWER = 'REVIEWER',
  TESTER = 'TESTER'
}

export enum AgentStatus {
  IDLE = 'IDLE',
  BUSY = 'BUSY',
  ERROR = 'ERROR'
}

export interface Task {
  id: string;
  type: string;
  description: string;
  priority: number;
  status: TaskStatus;
  assignedTo?: string;
  dependencies?: string[];
  metadata?: Record<string, unknown>;
}

export interface TaskResult {
  taskId: string;
  status: TaskStatus;
  result: unknown;
  error?: Error;
}

export enum TaskStatus {
  PENDING = 'PENDING',
  IN_PROGRESS = 'IN_PROGRESS',
  COMPLETED = 'COMPLETED',
  FAILED = 'FAILED'
}

export interface Message {
  id: string;
  from: string;
  to: string;
  type: MessageType;
  content: unknown;
  timestamp: Date;
}

export enum MessageType {
  TASK_ASSIGNMENT = 'TASK_ASSIGNMENT',
  TASK_UPDATE = 'TASK_UPDATE',
  TASK_COMPLETION = 'TASK_COMPLETION',
  ERROR = 'ERROR',
  INFO = 'INFO'
}
