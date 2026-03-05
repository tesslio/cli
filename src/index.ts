#!/usr/bin/env node

import { Command } from "commander";
import { skillCommand } from "./commands/skill.js";

const program = new Command();

program
  .name("tessl")
  .description("Tessl CLI - Agent Enablement Platform")
  .version("0.1.0");

program.addCommand(skillCommand);

program.parse(process.argv);
