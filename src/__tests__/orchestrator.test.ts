import { Orchestrator } from '../orchestrator/orchestrator';
import { Task, TaskStatus } from '../agents/types';

describe('Orchestrator', () => {
  let orchestrator: Orchestrator;

  beforeEach(() => {
    orchestrator = new Orchestrator();
  });

  it('should properly initialize with required components', () => {
    expect(orchestrator).toBeDefined();
  });

  it('should execute a workflow and decompose tasks', async () => {
    const mainTask: Task = {
      id: 'test-task-1',
      type: 'TEST',
      description: 'Test task',
      priority: 1,
      status: TaskStatus.PENDING
    };

    const result = await orchestrator.executeWorkflow(mainTask);

    expect(result).toBeDefined();
    expect(result.id).toBeDefined();
    expect(result.status).toBeDefined();
    expect(result.tasks).toBeInstanceOf(Array);
    expect(result.tasks.length).toBeGreaterThan(0);
  });

  it('should handle task assignment when no suitable agent is available', async () => {
    const mainTask: Task = {
      id: 'test-task-2',
      type: 'TEST',
      description: 'Test task without agent',
      priority: 1,
      status: TaskStatus.PENDING
    };

    const result = await orchestrator.executeWorkflow(mainTask);

    expect(result.status).toBe('FAILED');
    expect(result.error).toBeDefined();
  });
});
