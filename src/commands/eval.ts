import { Command } from "commander";
import { listEvalRuns } from "./eval/list";

export const evalCommand = new Command("eval")
  .description("Manage evaluation runs");

evalCommand
  .command("list")
  .description("List recent evaluation runs")
  .option("-n, --limit <number>", "Number of runs to display", "10")
  .action(async (options) => {
    await listEvalRuns({ limit: parseInt(options.limit, 10) });
  });
