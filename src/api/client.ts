import { getApiConfig } from "./config";
import { EvalRun, ListEvalRunsResponse } from "../types";

class ApiError extends Error {
  constructor(
    message: string,
    public statusCode?: number
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const config = getApiConfig();
  const url = `${config.baseUrl}${endpoint}`;

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(options.headers as Record<string, string>),
  };

  if (config.apiKey) {
    headers["Authorization"] = `Bearer ${config.apiKey}`;
  }

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    if (response.status === 401) {
      throw new ApiError(
        "Authentication required. Please run `tessl login` to authenticate.",
        response.status
      );
    }
    const errorText = await response.text();
    throw new ApiError(
      `API request failed: ${response.status} ${errorText}`,
      response.status
    );
  }

  return response.json() as Promise<T>;
}

export async function listEvalRuns(limit: number = 10): Promise<EvalRun[]> {
  const response = await request<ListEvalRunsResponse>(
    `/v1/eval/runs?limit=${limit}`
  );
  return response.runs;
}

export async function getEvalRun(id: string): Promise<EvalRun> {
  return request<EvalRun>(`/v1/eval/runs/${id}`);
}
