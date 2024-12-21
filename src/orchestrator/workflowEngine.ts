import { Task, TaskStatus } from '../agents/types';

export class WorkflowEngine {
  async decomposeTasks(mainTask: Task): Promise<Task[]> {
    // メインタスクをサブタスクに分解
    const subtasks: Task[] = [];

    // 計画フェーズ
    subtasks.push({
      id: `${mainTask.id}-planning`,
      type: 'PLANNING',
      description: `Create plan for: ${mainTask.description}`,
      priority: mainTask.priority,
      status: TaskStatus.PENDING,
      dependencies: []
    });

    // 実装フェーズ
    subtasks.push({
      id: `${mainTask.id}-implementation`,
      type: 'CODING',
      description: `Implement: ${mainTask.description}`,
      priority: mainTask.priority,
      status: TaskStatus.PENDING,
      dependencies: [`${mainTask.id}-planning`]
    });

    // レビューフェーズ
    subtasks.push({
      id: `${mainTask.id}-review`,
      type: 'REVIEW',
      description: `Review implementation of: ${mainTask.description}`,
      priority: mainTask.priority,
      status: TaskStatus.PENDING,
      dependencies: [`${mainTask.id}-implementation`]
    });

    // テストフェーズ
    subtasks.push({
      id: `${mainTask.id}-testing`,
      type: 'TESTING',
      description: `Test implementation of: ${mainTask.description}`,
      priority: mainTask.priority,
      status: TaskStatus.PENDING,
      dependencies: [`${mainTask.id}-implementation`]
    });

    return subtasks;
  }
}
