import { IAgent, Task, TaskStatus } from '../agents/types';

export class TaskManager {
  private tasks: Map<string, Task>;

  constructor() {
    this.tasks = new Map();
  }

  async assignTask(task: Task, agents: IAgent[]): Promise<IAgent | null> {
    // エージェントの能力とタスクの要件をマッチング
    const suitableAgent = agents.find(agent =>
      agent.status === 'IDLE' &&
      agent.capabilities.some(cap => task.type.includes(cap))
    );

    if (suitableAgent) {
      task.assignedTo = suitableAgent.id;
      task.status = TaskStatus.IN_PROGRESS;
      this.tasks.set(task.id, task);
      return suitableAgent;
    }

    return null;
  }

  async updateTaskStatus(taskId: string, status: TaskStatus): Promise<void> {
    const task = this.tasks.get(taskId);
    if (task) {
      task.status = status;
      this.tasks.set(taskId, task);
    }
  }

  getTask(taskId: string): Task | undefined {
    return this.tasks.get(taskId);
  }
}
