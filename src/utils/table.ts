import Table from "cli-table3";
import chalk from "chalk";
import { EvalRun } from "../types";

export function formatStatus(status: EvalRun["status"]): string {
  switch (status) {
    case "completed":
      return chalk.green(status);
    case "running":
      return chalk.blue(status);
    case "pending":
      return chalk.yellow(status);
    case "failed":
      return chalk.red(status);
    default:
      return status;
  }
}

export function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleString();
}

export function formatPassRate(passed: number, total: number): string {
  if (total === 0) return chalk.gray("-");
  const rate = (passed / total) * 100;
  const formatted = `${passed}/${total} (${rate.toFixed(0)}%)`;
  if (rate === 100) return chalk.green(formatted);
  if (rate >= 80) return chalk.yellow(formatted);
  return chalk.red(formatted);
}

export function createEvalRunsTable(runs: EvalRun[]): string {
  const table = new Table({
    head: [
      chalk.bold("ID"),
      chalk.bold("Name"),
      chalk.bold("Status"),
      chalk.bold("Pass Rate"),
      chalk.bold("Created"),
    ],
    style: {
      head: [],
      border: [],
    },
  });

  for (const run of runs) {
    table.push([
      chalk.cyan(run.id.slice(0, 8)),
      run.name,
      formatStatus(run.status),
      formatPassRate(run.passedTests, run.totalTests),
      formatDate(run.createdAt),
    ]);
  }

  return table.toString();
}
