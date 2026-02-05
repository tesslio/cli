export interface EvalRun {
  id: string;
  name: string;
  status: "pending" | "running" | "completed" | "failed";
  createdAt: string;
  completedAt?: string;
  totalTests: number;
  passedTests: number;
  failedTests: number;
}

export interface ApiConfig {
  baseUrl: string;
  apiKey?: string;
}

export interface ListEvalRunsResponse {
  runs: EvalRun[];
  total: number;
}
