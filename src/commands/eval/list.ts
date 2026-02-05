import chalk from "chalk";
import { listEvalRuns as fetchEvalRuns } from "../../api/client";
import { createEvalRunsTable } from "../../utils/table";

interface ListOptions {
  limit: number;
}

export async function listEvalRuns(options: ListOptions): Promise<void> {
  try {
    console.log(chalk.gray(`Fetching recent evaluation runs...`));
    console.log();

    const runs = await fetchEvalRuns(options.limit);

    if (runs.length === 0) {
      console.log(chalk.yellow("No evaluation runs found."));
      console.log();
      console.log("Run an evaluation with:");
      console.log(chalk.cyan("  tessl eval run <spec-file>"));
      return;
    }

    console.log(createEvalRunsTable(runs));
    console.log();
    console.log(
      chalk.gray(`Showing ${runs.length} most recent evaluation runs`)
    );
    console.log();
    console.log("View details of a run with:");
    console.log(chalk.cyan("  tessl eval show <run-id>"));
  } catch (error) {
    if (error instanceof Error) {
      console.error(chalk.red(`Error: ${error.message}`));
    } else {
      console.error(chalk.red("An unexpected error occurred"));
    }
    process.exit(1);
  }
}
