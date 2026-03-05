import { Command } from "commander";
import { reviewSkill } from "./skill/review.js";

export const skillCommand = new Command("skill")
  .description("Manage and review skills");

skillCommand
  .command("review")
  .description("Review a skill file for quality and best practices")
  .argument("<file>", "Path to the skill file to review")
  .option("--optimize", "Automatically optimize and improve the skill")
  .action(reviewSkill);
