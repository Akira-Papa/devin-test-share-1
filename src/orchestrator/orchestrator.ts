import { IAgent, Task, TaskResult } from '../agents/types';
import { TaskManager } from './taskManager';
import { WorkflowEngine } from './workflowEngine';
import { WorkflowResult, WorkflowStatus } from '../models/workflow';

export class Orchestrator {
  private agents: Map<string, IAgent>;
  private taskManager: TaskManager;
  private workflowEngine: WorkflowEngine;

  constructor() {
    this.agents = new Map();
    this.taskManager = new TaskManager();
    this.workflowEngine = new WorkflowEngine();
  }

  async executeWorkflow(task: Task): Promise<WorkflowResult> {
    try {
      // ワークフローの初期化
      const workflow: WorkflowResult = {
        id: `workflow-${Date.now()}`,
        status: WorkflowStatus.RUNNING,
        tasks: [task]
      };

      // タスクの分解と依存関係の解析
      const subtasks = await this.workflowEngine.decomposeTasks(task);
      workflow.tasks = [...workflow.tasks, ...subtasks];

      // タスクの実行と進捗管理
      for (const subtask of subtasks) {
        const agent = await this.taskManager.assignTask(subtask, Array.from(this.agents.values()));
        if (!agent) {
          throw new Error(`No suitable agent found for task: ${subtask.id}`);
        }

        const result = await agent.handleTask(subtask);
        await this.taskManager.updateTaskStatus(subtask.id, result.status);
      }

      // ワークフローの完了
      workflow.status = WorkflowStatus.COMPLETED;
      return workflow;
    } catch (error) {
      return {
        id: `workflow-${Date.now()}`,
        status: WorkflowStatus.FAILED,
        tasks: [],
        error: error instanceof Error ? error : new Error(String(error))
      };
    }
  }

  registerAgent(agent: IAgent): void {
    this.agents.set(agent.id, agent);
  }

  removeAgent(agentId: string): void {
    this.agents.delete(agentId);
  }
}
